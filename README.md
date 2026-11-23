# Django eLearning Platform

A Django-based eLearning website project built to explore the development of an online learning platform with separate student, teacher, and administrator workflows.

## Project overview

The repository contains a web application built with Django, SQLite, and Bootstrap. The original project documentation describes functionality for student registration and login, lesson publishing, lesson discussions, quizzes, and management of student, teacher, and lesson records.

This is an earlier learning project. It has not yet been recently tested, so the listed workflows should be treated as intended or previously documented functionality rather than a claim of current production readiness.

## Technology stack

- **Backend:** Python, Django
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Dependency management:** pip and `requirements.txt`

## Documented application areas

- Student registration and authentication
- Teacher-facing lesson publishing
- Student lesson access and learning pages
- Lesson comments and discussions
- Quiz participation
- Administrative management of student, teacher, and lesson records

## Repository structure

- `manage.py` — Django management entry point
- `requirements.txt` — Python dependencies
- `learning_site/` — Django project configuration
- Application templates, static assets, and supporting project files

## Local setup

The dependencies are from an older Django project and may require compatibility adjustments on modern Python versions.

1. Clone the repository:

   ```bash
   git clone https://github.com/isaacini23/elearning-with-django.git
   cd elearning-with-django
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

   On Windows, activate it with:

   ```powershell
   venv\\Scripts\\activate
   ```

3. Install the pinned dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations and start the development server:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. Open `http://127.0.0.1:8000/` in your browser.

If dependency installation fails, review the legacy package versions before changing them. The project has not yet been upgraded or verified against a current Django release.

## Current status

**Legacy project — review and testing pending.**

This repository is retained as evidence of Django web application practice. Before production use, it needs dependency review, security configuration, and end-to-end testing of its authentication, lesson, discussion, and quiz workflows.

## Screenshots

See the `assets/ss/` directory for the screenshots included with the project.

---

This repository retains attribution to the original project where applicable.