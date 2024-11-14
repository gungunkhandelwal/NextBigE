# User Authentication API with Docker and Django
<hr>

This project is a Django REST API for user management, including user registration, login, and profile retrieval. The API is designed with JWT token authentication and includes a custom user model with additional fields like `phone_number`, `date_of_birth`, and `last_login_ip`. 

Docker is used to containerize the application, and PostgreSQL is used as the database backend.

## Features
<hr>
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
<hr>

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
In .env file add your environment variable

### 5. Docker Setup
Make sure you have Dockerfile and docker-compose.yml

```bash
docker-compose up --build
```

### 6. Testing

```bash
pytest
```



