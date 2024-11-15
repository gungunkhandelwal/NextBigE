# User Authentication API with Docker and Django

This project is a Django REST API for user management, including user registration, login, and profile retrieval. The API is designed with JWT token authentication and includes a custom user model with additional fields like `phone_number`, `date_of_birth`, and `last_login_ip`. 

Docker is used to containerize the application, and PostgreSQL is used as the database backend.

## Features

- **Custom User Model**: Extends `AbstractUser` with additional fields:
  - `phone_number` (validated for Indian phone number format)
  - `date_of_birth`
  - `last_login_ip`

- **REST API Endpoints**:
  - `POST /api/register/` - User registration
  - `POST /api/login/` - User login (returns JWT token)
  - `GET /api/profile/` - Get authenticated user profile (includes `phone_number`, `date_of_birth`, and `last_login_ip`)

- **JWT Token Authentication**: Authentication is handled via JWT tokens.

- **Custom Middleware**: Captures and stores the user's IP address upon login.

- **PostgreSQL Database**: The application is containerized using Docker and uses PostgreSQL as the database.

## Installation

### Prerequisites
- Docker
- Docker Compose
- Python 3.10

### 1. Clone the repository

```bash
git clone https://github.com/gungunkhandelwal/NextBigE.git
cd NextBigE/
```

### 2. Set up virtual environment

```bash
python -m venv myenv
source myenv/bin/activate
```

### 3. Install requirements.txt

```bash
pip install -r requirements.txt
```

### 4. Set up environment variable

Create a .env file in the root directory of the project. Make sure to add any environment variables such as database credentials.
```bash
DATABASE_NAME=db_name
DATABASE_USER=db_user
DATABASE_PASSWORD=db_password
DATABASE_HOST=db
DATABASE_PORT=5432
```

### 5. Docker Setup

If you're using Docker to containerize the application, follow these steps:
**Build and Start the Containers**
Make sure you have both Dockerfile and docker-compose.yml files in your project directory. You can then build and start the application containers by running:
```bash
docker-compose up --build
```
This will:
- Build the Docker images
- Start the web server and PostgreSQL database containers

**Verify the Setup**
Once the containers are running, you can verify that everything is working by visiting the following endpoints:

- `http://localhost:8000/api/register/` for registration
- `http://localhost:8000/api/login/` for login
- `http://localhost:8000/api/profile/` for profile details

### 6. Run Migrations (Docker or Local Setup)

Before testing the application, make sure to run the migrations to set up the database schema:
```bash
docker-compose exec web python manage.py migrate
```
If you're using a local setup, run:

```bash
python manage.py migrate
```

### 7. Testing

```bash
docker-compose exec web pytest
```



