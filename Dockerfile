# Use an official Python runtime as the base image
FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install system dependencies
RUN apt-get update \
    && apt-get install -y \
        default-libmysqlclient-dev \
        && rm -rf /var/lib/apt/lists/*

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project code
COPY . .

# Expose the port the Django app runs on
EXPOSE 8000

# Define the command to run when the container starts
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Set the entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the entrypoint command
ENTRYPOINT ["/entrypoint.sh"]