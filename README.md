# NEXIS LOGIX

### Inventory Management System

A Django-based inventory management application for managing products, monitoring inventory records, and handling user accounts through a web interface.

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Django-Framework-092E20?style=flat-square&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL"/>
  <img src="https://img.shields.io/badge/Cloudinary-Media%20Storage-3448C5?style=flat-square" alt="Cloudinary"/>
  <img src="https://img.shields.io/badge/Deployment-Render-46E3B7?style=flat-square&logo=render&logoColor=black" alt="Render"/>
</p>

**NEXIS LOGIX** is a web-based inventory management project developed with Python and Django. It provides functionality for managing products, maintaining inventory records, and handling user accounts.

The project uses PostgreSQL for production database management and Cloudinary for profile image storage.

---

## Overview

Managing inventory manually can make product tracking and record management difficult.

NEXIS LOGIX aims to simplify these operations through a centralized web application with user authentication and inventory management functionality.

### Key Features

- **User Authentication** — User registration and login.
- **Profile Management** — Manage user profile information.
- **Image Upload** — Store profile images using Cloudinary.
- **Product Management** — Add, view, update, and delete products.
- **Inventory Dashboard** — View and manage product records.
- **Database Integration** — PostgreSQL for production and SQLite for development.
- **Responsive Interface** — Interface built with Bootstrap.
- **Deployment Support** — Configured for deployment using Render.

---

## Screenshots

Explore the project's screenshot collection:

[View Project Screenshots](https://github.com/mdsagurali/nexis-logix/tree/main/screenshots)

---

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend Framework | Django |
| Frontend | HTML5, CSS3, Bootstrap 5, JavaScript |
| Production Database | PostgreSQL |
| Development Database | SQLite |
| Media Storage | Cloudinary |
| Static File Handling | WhiteNoise |
| Hosting | Render |
| Version Control | Git & GitHub |

---

## Project Structure

```text
nexis-logix/
│
├── authApp/             # Authentication and user-related functionality
├── invApp/              # Inventory management functionality
├── invProject/          # Django project configuration
├── screenshots/         # Project screenshots
│
├── manage.py            # Django management utility
├── requirements.txt     # Python dependencies
├── .gitignore
└── README.md
```

---

## Getting Started

Follow these steps to run the project locally.

### Prerequisites

- Python
- pip
- Git
- A database configured for the project

### 1. Clone the Repository

```bash
git clone https://github.com/mdsagurali/nexis-logix.git

cd nexis-logix
```

### 2. Create a Virtual Environment

**Linux / Ubuntu**

```bash
python3 -m venv .venv

source .venv/bin/activate
```

**Windows**

```powershell
python -m venv .venv

.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```

### 4. Configure the Database

Configure the database settings according to the project's Django settings.

For local development, the project supports SQLite. PostgreSQL is used for production.

Configure any required environment variables and Cloudinary credentials before running the application.

Never commit secret keys, database passwords, or API credentials to GitHub.

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Create an Administrator Account

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

## Deployment

The project has been deployed using the following services:

| Service | Purpose |
|---|---|
| Render | Application hosting |
| PostgreSQL | Production database |
| Cloudinary | Profile image storage |
| WhiteNoise | Static file serving |

Production deployment requires appropriate environment variables, database configuration, and static/media storage settings.

---

## Security Considerations

The application includes:

- Django user authentication.
- Login-protected views.
- CSRF protection.
- Environment-based configuration.
- Cloud-based media storage.

For production use, sensitive credentials must remain outside the source code, and Django's production security settings must be configured appropriately.

---

## Future Improvements

Potential areas for further development:

- REST API integration using Django REST Framework.
- Role-based access control.
- Advanced inventory search and filtering.
- Stock-level monitoring and low-stock alerts.
- Inventory reporting and analytics.
- Automated testing.
- Docker-based deployment.

---

## About the Developer

**Md Sagur Ali**

Python Backend Developer

I enjoy building practical backend applications using Python and Django, with an interest in REST APIs, database design, application security, and deployment.

**Connect with me:**

- GitHub: [mdsagurali](https://github.com/mdsagurali)
- LinkedIn: [Md Sagur Ali](https://www.linkedin.com/in/mdsagurali/)
- Portfolio: [mdsagurali.github.io](https://mdsagurali.github.io/)
- Email: [mdsagurali.bd@gmail.com](mailto:mdsagurali.bd@gmail.com)

---

<p align="center">
  <strong>Built with Python and Django.</strong>
  <br/>
  <sub>Learning, building, testing, and improving.</sub>
</p>

<p align="center">
  <a href="https://github.com/mdsagurali/nexis-logix">View Repository</a>
</p>
