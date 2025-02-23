I'll help you fix the code blocks in the README.md. The issue is that each command should be in its own code block.

```markdown:c:\Users\kaung\Interntask1\README.md
# Data Submission Portal

A Django-based web application for managing and reviewing text and image URL entries with filtering, search, and review functionality.

## Features

- Create entries with text content or image URLs
- Filter entries by category
- Search functionality
- Entry review system with HTMX integration
- Pagination
- Real-time statistics

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/Lawliet-3/interntask1.git
cd interntask1
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
```
```bash
.\venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install django
```

4. Apply database migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Access the application at `http://127.0.0.1:8000`

## Technologies Used
- Django
- Bootstrap 5
- HTMX
- SQLite

## AI Usage Report
The following components were developed with AI assistance:

1. Frontend Templates:
   - Base template structure
   - Entry form layout
   - Entry list view with filtering and pagination
   - HTMX integration for review functionality

2. Styling:
   - Bootstrap implementation
   - Responsive design elements

3. Documentation:
   - Setup instructions
