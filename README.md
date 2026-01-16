# Expense Tracker – Backend

## Live Links

Frontend: https://expense-tracker-frontend-jyotsanas-projects-9c35b39a.vercel.app  
Backend API: https://expense-tracker-backend-thhy.onrender.com/api/expenses/  
Dashboard: https://expense-tracker-frontend-jyotsanas-projects-9c35b39a.vercel.app/dashboard  

---

## Project Overview

This is the backend of the Expense Tracker application built using Django and Django REST Framework.  
It provides REST APIs to perform full CRUD operations on expenses and integrates a third-party API for currency conversion.

---

## Tech Stack

- Django
- Django REST Framework
- PostgreSQL (Supabase)
- Render (Deployment)

---

## Database

Database: PostgreSQL (hosted on Supabase)

---

## Models

Expense Model:

| Field | Type |
|------|------|
| title | CharField |
| amount | DecimalField |
| category | CharField |
| date | DateField |
| payment_method | CharField |
| notes | TextField |

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|------------|
| GET | /api/expenses/ | Fetch all expenses |
| POST | /api/expenses/ | Create a new expense |
| PUT | /api/expenses/:id/ | Update an expense |
| DELETE | /api/expenses/:id/ | Delete an expense |
| GET | /api/convert/ | Currency conversion |

---

## Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=your_supabase_host
DB_PORT=5432
```

---

## How to Run Backend Locally

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Start Server

```bash
python manage.py runserver
```

Backend will run at:
http://127.0.0.1:8000/api/expenses/

---

## Deployment

Backend is deployed on **Render**.

Steps:
1. GitHub connected to Render
2. Build command: `pip install -r requirements.txt`
3. Start command: `gunicorn config.wsgi:application`
4. Environment variables added on Render
5. Database connected from Supabase

---

## How to Test (Backend)

1. Open backend API:  
   https://expense-tracker-backend-thhy.onrender.com/api/expenses/

2. Use POST to create a new expense  
3. Use PUT to update an expense  
4. Use DELETE to delete an expense  

---

## Author

Jyotsana Priyadarsini
