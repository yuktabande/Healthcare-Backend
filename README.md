Healthcare Backend

A Healthcare Management Backend built with Django, Django REST Framework, PostgreSQL, and JWT Authentication.

Features

- JWT-based Authentication
- Patient Management (CRUD)
- Doctor Management (CRUD)
- Patient-Doctor Mapping
- PostgreSQL Database
- Django Admin Panel
- Configuration via pyproject.toml

⸻

Project Structure

healthcare_backend/
├── pyproject.toml
├── manage.py
├── healthcare_backend/
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ └── wsgi.py
├── authentication/
├── patients/
├── doctors/
├── mappings/
└── README.md

⸻

Prerequisites

- Python 3.12+
- PostgreSQL 15+
- pip

⸻

Setup & Run

1. Clone the Repository

git clone <repository-url>
cd healthcare_backend

2. Create Virtual Environment

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies

pip install django djangorestframework djangorestframework-simplejwt psycopg2-binary

4. Configure Database and JWT Settings

Update pyproject.toml:

[tool.django]
secret_key = "your-secret-key"
debug = true
[tool.django.database]
name = "healthcare_db"
user = "your_postgres_username"
password = "your_postgres_password"
host = "localhost"
port = "5432"
[tool.django.jwt]
access_token_lifetime_minutes = 60
refresh_token_lifetime_days = 7

Note: Use your local PostgreSQL username. On many macOS Homebrew installations this is your system username rather than postgres.

5. Create PostgreSQL Database

createdb healthcare_db

Verify:

psql -l

6. Run Migrations

python manage.py migrate

7. Create Admin User (Optional)

python manage.py createsuperuser

8. Start Development Server

python manage.py runserver

Server:

http://127.0.0.1:8000/

Admin Panel:

http://127.0.0.1:8000/admin/

⸻

Authentication

Register

POST

/api/auth/register/

Request:

{
"name": "Jane Doe",
"email": "jane@example.com",
"password": "Pass@1234",
"password2": "Pass@1234"
}

Response:

{
"access": "<jwt_access_token>",
"refresh": "<jwt_refresh_token>"
}

Login

POST

/api/auth/login/

Request:

{
"username": "jane@example.com",
"password": "Pass@1234"
}

Refresh Token

POST

/api/auth/token/refresh/

Request:

{
"refresh": "<refresh_token>"
}

Protected Routes

Include:

Authorization: Bearer <access_token>

⸻

Patients API

Create Patient

POST

/api/patients/

Request:

{
"name": "John Smith",
"date_of_birth": "1990-05-15",
"gender": "M",
"contact_number": "+919876543210",
"email": "john@example.com",
"address": "123 Main St, Pune",
"medical_history": "Hypertension"
}

Other Endpoints

GET /api/patients/
GET /api/patients/<id>/
PUT /api/patients/<id>/
DELETE /api/patients/<id>/

⸻

Doctors API

Create Doctor

POST

/api/doctors/

Request:

{
"name": "Dr. Priya Sharma",
"specialization": "Cardiology",
"contact_number": "+911234567890",
"email": "priya@hospital.com",
"experience_years": 10,
"qualification": "MBBS, MD",
"available": true
}

Other Endpoints

GET /api/doctors/
GET /api/doctors/<id>/
PUT /api/doctors/<id>/
DELETE /api/doctors/<id>/

⸻

Patient-Doctor Mapping API

Create Mapping

POST

/api/mappings/

Request:

{
"patient": 1,
"doctor": 2,
"notes": "Primary cardiologist"
}

Other Endpoints

GET /api/mappings/
GET /api/mappings/<patient_id>/
DELETE /api/mappings/delete/<id>/

⸻

Available Routes

/admin/
/api/auth/
/api/patients/
/api/doctors/
/api/mappings/
