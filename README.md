# Resume Screener (Ongoing Project)

An AI-powered web application to automatically screen resumes based on job descriptions using NLP. This tool helps recruiters shortlist candidates efficiently by comparing candidate resumes with the job role requirements.

## Ì≥Å Project Structure

resume_screener/
‚îú‚îÄ‚îÄ backend/ # FastAPI backend with SQLAlchemy
‚îú‚îÄ‚îÄ frontend/ # React-based frontend
‚îî‚îÄ‚îÄ README.md


---

## Ì∫Ä Features

- Upload job descriptions and candidate resumes.
- Automatically ranks resumes based on similarity.
- FastAPI backend with REST APIs.
- React frontend interface.
- SQLAlchemy for database interaction.

---

## Ì¥ß Tech Stack

- **Frontend:** React.js, Bootstrap
- **Backend:** FastAPI, Python, SQLAlchemy
- **Database:** SQLite (currently), easily upgradable to PostgreSQL
- **NLP:** spaCy / Scikit-learn for text similarity (implementation ongoing)

---

## Ì≥¶ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/my_projects.git
cd my_projects/resume_screener

cd backend
python -m venv venv
.\venv\Scripts\activate      # For Windows PowerShell
pip install -r requirements.txt
uvicorn main:app --reload

cd ../frontend
npm install
npm start
