# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

EXPOSE 8080

# Start the app on port 8080
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]
