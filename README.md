# 🚗 Auto Service Management System

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-green.svg)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.x-purple.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-orange.svg)](LICENSE)

A Django web application for managing **customers**, **cars**, and **services** in an auto service workshop.  
Supports user registration, authentication, car management, and service history tracking.

---

## ✨ Features

- 👤 **User Authentication**
  - Registration, Login, Logout
  - Password Change & Reset via email
  - Only authenticated users can add/edit cars and services

- 🚗 **Car Management**
  - Add, update, and delete cars
  - Each car is linked to its owner (customer)
  - Car images supported

- 🛠 **Service Management**
  - Track service descriptions, dates, and costs
  - Each service is tied to a car

- 👨‍👩‍👦 **Customer Management**
  - Customer profile automatically linked to `User`
  - View details and related cars

- 📊 **Dashboard**
  - Shows counts of customers, cars, and services

---

## 🛠 Technology Stack

- **Backend:** Django 4.x  
- **Frontend:** Bootstrap 5, custom CSS animations  
- **Database:** SQLite (default, can be replaced with PostgreSQL/MySQL)  
- **Auth:** Django built-in `auth` system  
- **Email:** Gmail SMTP or console backend for development  
- **Tools:** PyCharm / VS Code, Git

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/Osiakosia/Final_project.git
cd autoservice
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Create superuser
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

### 7. Accounts settings for test purposes 

#### Admin user : Login : Admin&&    Pass  admin
#### Simple user : Login Tina&&      Pass kjuikjui

## 📧 Email Setup

By default, password reset uses Django’s **console backend** (emails appear in terminal).

To use **Gmail SMTP**:

1. Enable **2-Step Verification** in Google Account  
2. Generate a **16-character App Password**  
3. Add to `.env` file in project root:

```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_16_char_app_password
```

---

## 📂 Project Structure

```
final_project/
│── finalapp/
│   ├── models.py        # Customer, Car, Service models
│   ├── views.py         # Class-based views with LoginRequiredMixin
│   ├── urls.py          # App routes
│   ├── forms.py         # Model forms
│   ├── templates/
│   │   ├── base.html    # Bootstrap base template with navbar
│   │   ├── index.html   # Dashboard
│   │   ├── customers/   # Customer templates
│   │   ├── cars/        # Car templates
│   │   ├── parts/       # Parts templates
│   │   └── services/    # Service templates
│   └── static/
│       └── finalapp/
│           └── css/
│               └── style.css
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🚀 Future Improvements

- Export service history to PDF/CSV  
- REST API for mobile clients  
- Role-based permissions (Admin / Staff / Customer)  
- Car service reminders via email

---

## 👨‍💻 Author

Built with ❤️ using Django & Bootstrap.
