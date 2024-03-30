# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install gcc and other build dependencies if needed
RUN apt-get update && apt-get install -y gcc python3-dev

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file from the host into the Docker image
COPY requirements.txt /app/

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container at /app
COPY . /app

# Define environment variables (if any)
ENV ENV_VARIABLE=value

# Run your main script or application
CMD ["python", "/app/src/main/ConstrainedDeviceApp.py"]










