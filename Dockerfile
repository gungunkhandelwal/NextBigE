# Use the official Python image from the Docker Hub
FROM python:3.10.12

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container at /app
COPY . /app/

# Expose port 8000 for the Django app
EXPOSE 8000

# Run the Django application using the command defined in docker-compose.yml
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
