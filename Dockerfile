# Base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requ.txt /app/

RUN pip install -r requ.txt

# Copy the rest of the application
COPY . /app/

# Collect static files (not required if you're using a CDN)
RUN python manage.py collectstatic --noinput


# Expose port 8000 (default port for Django)
EXPOSE 8000

# Start the Django server
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]