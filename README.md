
# NEXIS LOGIX — Inventory Management System

A modern Django-based inventory management application designed to simplify product management, organize stock records, and manage inventory operations through a clean and user-friendly interface.

NEXIS LOGIX provides secure user authentication, profile management, and complete product CRUD functionality using Python and Django.

---

## Overview

Managing product information manually can become difficult as inventory grows. NEXIS LOGIX provides a centralized system to manage product records efficiently.

Users can securely access the application, create product entries, view inventory, update product information, and delete records.

## Features

### Authentication & User Management
- User registration and login.
- Secure logout functionality.
- Login-protected inventory pages.
- User profile management.
- Profile image and bio management.
- Django password validation.
- Safe post-login redirect handling.

### Inventory Management
- Create new products.
- Display all available products.
- Update existing product information.
- Delete products with confirmation.
- Unique SKU validation.
- Product price validation.
- Stock quantity management.
- Supplier information management.

### Additional Features
- Django ORM and database migrations.
- Environment-based configuration.
- Static file management with WhiteNoise.
- Cloudinary integration for media storage.
- Responsive web interface.
- Automated application tests.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| Django ORM | Database operations |
| HTML5 | Web page structure |
| CSS3 | Styling |
| Bootstrap | UI components |
| JavaScript | Frontend interactions |
| WhiteNoise | Static file serving |
| Cloudinary | Media storage integration |
| Git & GitHub | Version control |

---

## Project Structure

```text
nexis-logix/
│
├── authApp/
│   ├── migrations/
│   ├── tests.py
│   ├── forms.py
│   ├── models.py
│   ├── signals.py
│   ├── urls.py
│   └── views.py
│
├── invApp/
│   ├── migrations/
│   ├── templates/
│   │   └── invApp/
│   ├── tests.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── invProject/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── templates/
│   └── accounts/
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## Installation & Setup

Follow these steps to run NEXIS LOGIX locally.

### 1. Clone the Repository

```bash
git clone https://github.com/mdsagurali/nexis-logix.git

cd nexis-logix
```

### 2. Create a Virtual Environment

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```bash
py -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=your-database-url
```

If Cloudinary is configured in your settings, add the required Cloudinary credentials using the exact environment variable names expected by the project.

**Important:**
- Never upload `.env` to GitHub.
- Never expose secret keys or database credentials.
- Generate your own Django secret key.
- Use `DEBUG=False` in production.
- Configure a valid production database URL.

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Create an Admin Account

```bash
python manage.py createsuperuser
```

### 7. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open your browser:

```text
http://127.0.0.1:8000/
```

---

## Application Routes

| Feature | URL |
|---|---|
| Login | `/login/` |
| Registration | `/register/` |
| Logout | `/logout/` |
| User Profile | `/profile/` |
| Admin Panel | `/admin/` |
| Inventory Dashboard | `/inv/` |

Product CRUD routes are configured inside the inventory application.

---

## Product Model

The Product model contains the following fields:

| Field | Description |
|---|---|
| `product_id` | Primary key |
| `name` | Product name |
| `sku` | Unique product identifier |
| `price` | Product price |
| `quantity` | Available stock |
| `supplier` | Supplier name |

### Data Validation
- SKU values must be unique.
- Product prices cannot be negative.
- Quantity uses a non-negative integer field.
- Server-side form validation is applied.

---

## Testing

NEXIS LOGIX includes automated tests for inventory and authentication functionality.

Run all tests:

```bash
python manage.py test
```

Run inventory tests:

```bash
python manage.py test invApp
```

Run authentication tests:

```bash
python manage.py test authApp
```

### Test Coverage

**Inventory Tests**
- Product listing.
- Product creation.
- Product updating.
- Product deletion.
- Login protection.

**Authentication & Profile Tests**
- User registration.
- Valid login.
- Invalid login.
- User logout.
- Profile access protection.
- Profile page functionality.

### Latest Test Result

```text
Found 11 test(s).

Ran 11 tests

OK
```

All 11 tests passed in the latest reported local test run.

---

## Security Considerations

- Django authentication and authorization.
- CSRF protection for form submissions.
- Login-required decorators for protected views.
- POST-based logout and delete operations.
- Server-side form validation.
- Environment-based secret management.
- Safe redirect URL validation.

Production deployment still requires a complete security configuration review.

---

## Development Commands

Check Django configuration:

```bash
python manage.py check
```

Check for model changes:

```bash
python manage.py makemigrations --check --dry-run
```

Create migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

Collect static files:

```bash
python manage.py collectstatic --noinput
```

Run automated tests:

```bash
python manage.py test
```

---

## Project Status

| Component | Status |
|---|---|
| User Authentication | Implemented |
| Profile Management | Implemented |
| Product CRUD | Implemented |
| Database Migrations | Verified |
| Static File Collection | Verified |
| Automated Tests | 11/11 Passed |
| Django System Check | Passed |

*Status reflects the latest reported local verification.*

---

## Author

**Md Sagur Ali**

Python Backend Developer

- **GitHub:** [@mdsagurali](https://github.com/mdsagurali)
- **LinkedIn:** [Md Sagur Ali](https://www.linkedin.com/in/mdsagurali/)
- **Portfolio:** [mdsagurali.github.io](https://mdsagurali.github.io/)

---

## License

No license has been specified yet. All rights are reserved by default unless a license is added to this repository.
