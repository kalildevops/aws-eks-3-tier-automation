# Use the official Python image as the base image
FROM python:3.12.3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    nginx \
    python3-dev \
    build-essential \
    telnet \
    dnsutils

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY pyproject.toml poetry.lock /app/

# Install Poetry
RUN pip install poetry

# Install project dependencies using Poetry
RUN poetry install

# Copy the rest of the application code to the working directory
COPY . /app/

# Expose port 5000 to the outside world
EXPOSE 8080

# Command to run the Flask application
CMD ["poetry", "run", "python", "app.py"]
