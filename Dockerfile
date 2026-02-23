# Use an official Python base image
FROM python:3.10-slim

# Set a working directory
WORKDIR /app

# Copy requirements.txt first to leverage Docker layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the source code
COPY . .

# Expose port 8000
EXPOSE 8000

# Run the app using CMD
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]