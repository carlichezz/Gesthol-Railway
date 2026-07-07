# Gesthol

Hotel reservation and activity management REST API, built with Django 5 and Django REST Framework. Configured for deployment on [Railway](https://railway.app/).

## Features

- **Reservations** — Create, read, update, and delete hotel reservations with client name, room type, dates, guest count, and room count
- **Activities** — Manage hotel activities with name, location, date/time, photo, and description (public read-only, authenticated write)
- **Authentication** — User registration, login, and token-based authentication via DRF Token Auth
- **CORS** — Enabled for all origins (development-friendly)

## Tech Stack

- Python 3
- Django 5.0
- Django REST Framework 3.15
- PostgreSQL (production) / SQLite (development)
- Gunicorn / Uvicorn
- Whitenoise (static files)

## API Endpoints

### Authentication (Token-based)

| Method | Endpoint      | Description          |
| ------ | ------------- | -------------------- |
| POST   | `/register`   | Create a new user    |
| POST   | `/login`      | Authenticate and get token |
| GET    | `/profile`    | View current user (auth)   |
| GET    | `/logout`     | Delete auth token (auth)   |

### Reservas (auth required)

| Method | Endpoint                 | Description           |
| ------ | ------------------------ | --------------------- |
| GET    | `/api/reservas/`         | List all reservations |
| POST   | `/api/reservas/`         | Create a reservation  |
| GET    | `/api/reservas/{id}/`    | Retrieve a reservation |
| PUT    | `/api/reservas/{id}/`    | Update a reservation  |
| PATCH  | `/api/reservas/{id}/`    | Partial update        |
| DELETE | `/api/reservas/{id}/`    | Delete a reservation  |

### Actividades (read-only public, write auth)

| Method | Endpoint                   | Description         |
| ------ | -------------------------- | ------------------- |
| GET    | `/api/actividades/`         | List all activities |
| POST   | `/api/actividades/`         | Create an activity  |
| GET    | `/api/actividades/{id}/`    | Retrieve an activity |
| PUT    | `/api/actividades/{id}/`    | Update an activity  |
| PATCH  | `/api/actividades/{id}/`    | Partial update      |
| DELETE | `/api/actividades/{id}/`    | Delete an activity  |

### Users (auth required)

| Method | Endpoint             | Description |
| ------ | -------------------- | ----------- |
| GET    | `/api/users/`        | List users  |
| POST   | `/api/users/`        | Create user |
| GET    | `/api/users/{id}/`   | Retrieve user |
| PUT    | `/api/users/{id}/`   | Update user |
| DELETE | `/api/users/{id}/`   | Delete user |

### Admin

| Method | Endpoint   | Description     |
| ------ | ---------- | --------------- |
| GET    | `/admin/`  | Django admin    |

## Getting Started

```bash
# Clone the repository
git clone <repo-url> && cd Gesthol-Railway-main

# Create and activate a virtual environment
python -m venv venv && source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

## Environment Variables

| Variable       | Description                                    | Default        |
| -------------- | ---------------------------------------------- | -------------- |
| `DATABASE_URL` | PostgreSQL connection string (production)      | SQLite (dev)   |
| `SECRET_KEY`   | Django secret key (should be set in production)| Hardcoded (dev)|
| `DEBUG`        | Debug mode                                     | `True`         |

## Deployment

The project includes a `build.sh` script that installs dependencies, collects static files, and runs migrations — ready for deployment on Railway or any platform supporting build/start commands.
