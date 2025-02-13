# Please fill in Dockerfile content# Use an official Python image as the base
FROM python:3.13-slim

# Set environment variables
ENV POETRY_VERSION=2.0.1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYTHONPATH=/app

# Set working directory
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

# Copy pyproject.toml and poetry.lock to install dependencies first (for caching efficiency)
COPY pyproject.toml poetry.lock /app/

# Install dependencies
RUN poetry install --no-root 

# Copy the rest of the application files
COPY . /app

# Expose FastAPI default port
EXPOSE 8000

# Set entrypoint for the container
ENTRYPOINT ["poetry", "run"]

# Default CMD arguments (can be overridden)
CMD ["sh", "-c", "cd my_service && uvicorn main:app --reload --host 0.0.0.0"]
