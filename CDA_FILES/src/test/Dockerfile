# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python source code into the container at /app
COPY src/main/python /app

# Install any needed dependencies specified in requirements.txt
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Run your Python application
CMD ["python", "your_main_script.py"]
