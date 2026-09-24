from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get(
    "/",
    response_class=HTMLResponse
)

def home(request: Request):

    full_name = "Xavier Grant Rosales"
    professional_title = "Operations & Technical Support Professional"
    technical_skills = [
        "Python",
        "FastAPI",
        "SQLite",
        "Pydantic",
        "Git/GitHub",
        "HTML",
        "CSS",
        "Jinja2"
    ]
    projects = [
        {
            "name": "Cigarette Tracker REST API",
            "description": "Tracks daily cigarette consumption, manages smoking records, and calculates remaining allowances and daily limit status.",
            "technologies": ["Python", "FastAPI", "SQLite", "Pydantic", "Git/GitHub"],
            "github_url": "https://github.com/xgrantrosales/cigarette-tracker-api"
        },
        {
            "name": "Application Portfolio Hub",
            "description": "A portfolio website presenting my skills, projects, and application materials, built with FastAPI and Jinja templates.",
            "technologies": ["Python", "FastAPI", "Jinja2", "HTML", "CSS"],
            "github_url": "https://github.com/xgrantrosales/application-portfolio-hub"
        }
    ]
    operations_skills = [
        "Team Leadership",
        "Customer Service Operations",
        "KPI Monitoring",
        "Quality Assurance",
        "SOP Development",
        "Process Improvement",
        "Performance Management",
        "Coaching & Training",
        "Escalation Management",
        "Technical Troubleshooting",
        "Cross-functional Collaboration"
    ]

    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={
            "full_name": full_name,
            "professional_title": professional_title,
            "technical_skills": technical_skills,
            "projects": projects,
            "operations_skills": operations_skills
        }
    )

    