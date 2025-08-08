# Resume Screener (Ongoing Project)

An AI-powered web application to automatically screen resumes based on job descriptions using NLP. This tool helps recruiters shortlist candidates efficiently by comparing candidate resumes with the job role requirements.

## � Project Structure

resume_screener/
├── backend/ # FastAPI backend with SQLAlchemy
├── frontend/ # React-based frontend
└── README.md


---

## � Features

- Upload job descriptions and candidate resumes.
- Automatically ranks resumes based on similarity.
- FastAPI backend with REST APIs.
- React frontend interface.
- SQLAlchemy for database interaction.

---

## � Tech Stack

- **Frontend:** React.js, Bootstrap
- **Backend:** FastAPI, Python, SQLAlchemy
- **Database:** SQLite (currently), easily upgradable to PostgreSQL
- **NLP:** spaCy / Scikit-learn for text similarity (implementation ongoing)

---

## � Installation

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
