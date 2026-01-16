# Expense Tracker – Backend

## Live Links

Frontend: https://expense-tracker-frontend-jyotsanas-projects-9c35b39a.vercel.app  
Backend API: https://expense-tracker-backend-thhy.onrender.com/api/expenses/  
Dashboard: https://expense-tracker-frontend-jyotsanas-projects-9c35b39a.vercel.app/dashboard  

---

## Project Overview

This is a full-stack Expense Tracker web application built using Django REST Framework for the backend and Next.js for the frontend.

Users can:
- Add expenses
- View expenses
- Edit expenses
- Delete expenses
- View reports on a dashboard
- Convert total amount into different currencies

---

## Tech Stack

Backend:
- Django
- Django REST Framework
- PostgreSQL (Supabase)
- Render (deployment)

Frontend:
- Next.js (React)
- Axios
- Recharts
- Vercel (deployment)

---

## Features

- Full CRUD operations
- REST APIs
- PostgreSQL database
- Dashboard with charts
- Currency conversion using third-party API
- Fully deployed

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|------------|
| GET | /api/expenses/ | Get all expenses |
| POST | /api/expenses/ | Create expense |
| PUT | /api/expenses/:id/ | Update expense |
| DELETE | /api/expenses/:id/ | Delete expense |
| GET | /api/convert/ | Currency conversion |

---

## How to Run Locally

### Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Demo Steps
	1.	Open frontend
	2.	Add an expense
	3.	Edit the expense
	4.	Delete the expense
	5.	Go to dashboard
	6.	View chart
	7.	Convert currency

Author

Jyotsana Priyadarsini
