# FAQ Management System

## Overview
This is a Django-based FAQ Management System with multi-language translation support and a WYSIWYG editor for formatted answers. The API allows users to fetch FAQs in different languages dynamically.

## Features
- **WYSIWYG Editor Support** using `django-ckeditor`
- **Multi-Language Translation** (Supports English, Hindi, Bengali, etc.)
- **REST API for FAQs** with language selection via query parameter
- **Caching with Redis** for optimized performance
- **Admin Panel** for easy FAQ management
- **Unit Tests** to ensure functionality

## Installation
### Prerequisites
- Python 3.12+
- Django 5+
- PostgreSQL or SQLite (default)
- Redis (for caching)

### Steps
1. Clone the repository:
   ```sh
   git clone <your-repo-url>
   cd <your-project-folder>
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```sh
   python manage.py migrate
   ```
5. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```sh
   python manage.py runserver
   ```

## API Usage
### Fetch FAQs in English (Default)
```sh
curl http://localhost:8000/api/faqs/
```
### Fetch FAQs in Hindi
```sh
curl http://localhost:8000/api/faqs/?lang=hi
```
### Fetch FAQs in Bengali
```sh
curl http://localhost:8000/api/faqs/?lang=bn
```

## Multi-Language Support
- FAQs are automatically translated using Google Translate API (`googletrans` package).
- The translated fields (`question_hi`, `question_bn`, etc.) are precomputed and stored in the database.

## Running Tests
Run unit tests using `pytest`:
```sh
pytest
```

## Author
Developed by **PARA HARIKA NAGASUDHA** as part of the BharatFD Backend Developer Hiring Test.

