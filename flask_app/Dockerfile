# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app files
COPY . .

# Set the environment variables
ENV FLASK_APP=app.py

# Expose the Flask port
EXPOSE 5000

# Run the app
CMD ["flask", "run", "--host=0.0.0.0"]
