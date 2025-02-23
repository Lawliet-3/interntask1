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


python -m venv venv
.\venv\Scripts\activate


pip install django


python manage.py migrate


python manage.py createsuperuser

python manage.py runserver


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