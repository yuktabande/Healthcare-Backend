# Healthcare Backend

A Healthcare Management Backend built with Django, Django REST Framework (DRF), PostgreSQL, and JWT Authentication.

## Features

- JWT-based Authentication
- Patient Management (CRUD)
- Doctor Management (CRUD)
- Patient-Doctor Mapping
- PostgreSQL Database
- Django Admin Panel
- Configuration via `pyproject.toml`

---

## Project Structure

```text
healthcare_backend/
├── pyproject.toml
├── manage.py
├── healthcare_backend/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── authentication/
├── patients/
├── doctors/
├── mappings/
└── README.md
```

---

## Prerequisites

- Python 3.12+
- PostgreSQL 15+
- pip

---

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/Healthcare-Backend.git
cd Healthcare-Backend
```

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install django djangorestframework djangorestframework-simplejwt psycopg2-binary
```

### 4. Configure Database

Update the database configuration inside `pyproject.toml`.

```toml
[tool.django.database]
name = "healthcare_db"
user = "your_postgres_username"
password = "your_postgres_password"
host = "localhost"
port = "5432"
```

> **Note:** On macOS/Homebrew PostgreSQL installations, your PostgreSQL username is often your system username rather than `postgres`.

### 5. Create PostgreSQL Database

```bash
createdb healthcare_db
```

Verify:

```bash
psql -l
```

### 6. Run Database Migrations

```bash
python manage.py migrate
```

### 7. Create Admin User (Optional)

```bash
python manage.py createsuperuser
```

### 8. Start Development Server

```bash
python manage.py runserver
```

Server:

```text
http://127.0.0.1:8000/
```

Admin Panel:

```text
http://127.0.0.1:8000/admin/
```

---

## Authentication

### Register

**POST** `/api/auth/register/`

#### Request Body

```json
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "password": "Pass@1234",
  "password2": "Pass@1234"
}
```

#### Response

```json
{
  "access": "<jwt_access_token>",
  "refresh": "<jwt_refresh_token>"
}
```

---

### Login

**POST** `/api/auth/login/`

#### Request Body

```json
{
  "username": "jane@example.com",
  "password": "Pass@1234"
}
```

---

### Refresh Token

**POST** `/api/auth/token/refresh/`

#### Request Body

```json
{
  "refresh": "<refresh_token>"
}
```

---

### Authorization Header

All protected endpoints require:

```http
Authorization: Bearer <access_token>
```

---

## Patients API

### Create Patient

**POST** `/api/patients/`

#### Request Body

```json
{
  "name": "John Smith",
  "date_of_birth": "1990-05-15",
  "gender": "M",
  "contact_number": "+919876543210",
  "email": "john@example.com",
  "address": "123 Main St, Pune",
  "medical_history": "Hypertension"
}
```

### Other Patient Endpoints

```http
GET     /api/patients/
GET     /api/patients/<id>/
PUT     /api/patients/<id>/
DELETE  /api/patients/<id>/
```

---

## Doctors API

### Create Doctor

**POST** `/api/doctors/`

#### Request Body

```json
{
  "name": "Dr. Priya Sharma",
  "specialization": "Cardiology",
  "contact_number": "+911234567890",
  "email": "priya@hospital.com",
  "experience_years": 10,
  "qualification": "MBBS, MD",
  "available": true
}
```

### Other Doctor Endpoints

```http
GET     /api/doctors/
GET     /api/doctors/<id>/
PUT     /api/doctors/<id>/
DELETE  /api/doctors/<id>/
```

---

## Patient-Doctor Mapping API

### Create Mapping

**POST** `/api/mappings/`

#### Request Body

```json
{
  "patient": 1,
  "doctor": 2,
  "notes": "Primary cardiologist"
}
```

### Other Mapping Endpoints

```http
GET     /api/mappings/
GET     /api/mappings/<patient_id>/
DELETE  /api/mappings/delete/<id>/
```

---

## Available Routes

```text
/admin/
/api/auth/
/api/patients/
/api/doctors/
/api/mappings/
```

---

## Testing Workflow

1. Register a user using `/api/auth/register/`
2. Login using `/api/auth/login/`
3. Copy the access token
4. Add the token to the Authorization header:

```http
Authorization: Bearer <access_token>
```

5. Create Patients
6. Create Doctors
7. Create Patient-Doctor Mappings
8. Verify CRUD operations through Postman or any API client
