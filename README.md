# Application Portfolio Hub

A personal portfolio website built with FastAPI, Jinja2, HTML, and CSS to showcase my professional background, skills, projects, and application materials.

## Features

- Professional introduction and About Me section
- Technical and operations skills displayed as responsive labels
- Project listings generated from Python dictionaries using Jinja loops
- GitHub links displayed only when a project has a repository URL
- Resume and cover letter PDFs
- Introduction video shared through Loom
- GitHub profile and email contact links
- Responsive card layout and styled buttons

## Technologies

- Python
- FastAPI
- Jinja2
- HTML
- CSS
- Uvicorn

## Project Files

| File or folder | Purpose |
| --- | --- |
| `main.py` | FastAPI application, homepage route, and portfolio data |
| `templates/home.html` | Jinja template for the homepage |
| `static/style.css` | Page layout and styling |
| `static/resume.pdf` | Resume document |
| `static/cover-letter.pdf` | Cover letter document |
| `requirements.txt` | Python packages and installed versions |
| `.gitignore` | Files and folders excluded from Git |

## Run Locally

Install Python and download or clone this repository. Open a terminal in the project folder containing `main.py`.

### 1. Create a virtual environment

On Windows:

```cmd
py -m venv .venv
```

On macOS or Linux:

```bash
python3 -m venv .venv
```

### 2. Activate the virtual environment

On Windows using Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the development server

Run this from the project root:

```bash
python -m uvicorn main:app --reload
```

### 5. Open the website

Visit http://127.0.0.1:8000 in your browser.

Press Ctrl+C in the terminal to stop the server.

## Customization

- Update profile information, skills, and projects inside `home()` in `main.py`.
- Edit page content and structure in `templates/home.html`.
- Adjust colors, spacing, and layout in `static/style.css`.
- Replace the PDFs in `static/` with your own application materials.
- Update the email, GitHub profile, and Loom links in the HTML template.
- Set a project's `github_url` to `None` to hide its repository link.

## What I Practiced

- Serving an HTML page with FastAPI
- Passing Python data into Jinja templates
- Using template loops and conditions
- Serving static files
- Structuring pages with semantic HTML
- Styling responsive layouts with CSS and Flexbox
- Using Git to track project changes

## Author

Xavier Grant Rosales

GitHub: https://github.com/xgrantrosales