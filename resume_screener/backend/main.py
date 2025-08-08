from fastapi import FastAPI, File, UploadFile, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import fitz  # PyMuPDF
import re
import os
import sqlite3
import spacy
import json

# Initialize spaCy English model (run: python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
load_dotenv()

# Predefined API keys (for authentication)
API_KEYS = set(os.getenv("API_KEYS", "").split(","))


# Predefined skill keywords
SKILL_KEYWORDS = {
    "python", "java", "sql", "c++", "c", "javascript", "react", "nodejs",
    "mongodb", "html", "css", "django", "flask", "fastapi", "git", "github",
    "data analysis", "machine learning", "deep learning", "nlp", "opencv",
    "pandas", "numpy", "matplotlib", "tensorflow", "keras", "docker",
    "linux", "aws", "azure", "power bi", "tableau"
}

# Ensure SQLite DB exists
def init_db():
    conn = sqlite3.connect("resumes.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resumes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        email TEXT,
        skills TEXT,
        entities TEXT,
        score INTEGER,
        label TEXT
    )
""")

    conn.commit()
    conn.close()

init_db()

@app.get("/")
def root():
    return {"message": "Resume Screener API is running"}

@app.post("/upload-resume/")
async def upload_resume(
    file: UploadFile = File(...),
    x_api_key: str = Header(None)
):
    # Authentication
    if x_api_key not in API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")

    if not file.filename.endswith(".pdf"):
        return JSONResponse(status_code=400, content={"error": "Only PDF files are supported."})

    # Save the file temporarily
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb") as buffer:
        buffer.write(await file.read())

    # Extract text
    try:
        text = extract_text_from_pdf(file_location)
    except Exception as e:
        os.remove(file_location)
        return JSONResponse(status_code=500, content={"error": str(e)})

    os.remove(file_location)

    # Extract email
    email = extract_email(text)

    # Extract skills
    extracted_skills = extract_skills(text)

    # NLP entities
    entities = extract_entities(text)
    score, label = score_resume(text,extracted_skills)

    # Save to DB
    save_to_db(file.filename, email, extracted_skills, entities, score, label)

    return {
        "filename": file.filename,
        "email": email,
        "skills": list(extracted_skills),
        "entities": entities,
        "score": score,
        "label": label 
    }
def score_resume(text, skills):
    score = 0

    # Base scoring rules
    if "education" in text.lower():
        score += 1
    if "experience" in text.lower():
        score += 1
    if "projects" in text.lower():
        score += 1
    if "certifications" in text.lower():
        score += 1
    if "internship" in text.lower():
        score += 1

    # Skill-based scoring
    if len(skills) > 5:
        score += 2
    elif len(skills) > 2:
        score += 1

    # Labeling
    if score >= 6:
        label = "Excellent"
    elif score >= 4:
        label = "Good"
    else:
        label = "Average"

    return score, label

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def extract_email(text):
    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return emails[0] if emails else None

def extract_skills(text):
    lower = text.lower()
    return {skill for skill in SKILL_KEYWORDS if skill in lower}

def extract_entities(text):
    doc = nlp(text)
    result = []
    for ent in doc.ents:
        result.append({"text": ent.text, "label": ent.label_})
    return result

def save_to_db(filename, email, skills, entities, score, label):
    conn = sqlite3.connect("resumes.db")
    c = conn.cursor()
    c.execute(
        '''
        INSERT INTO resumes (filename, email, skills, entities, score, label)
        VALUES (?, ?, ?, ?, ?, ?)
        ''',
        (
            filename,
            email,
            json.dumps(list(skills)),
            json.dumps(entities),
            score,
            label
        )
    )
    conn.commit()
    conn.close()

