# Use a base image with Python installed
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Set up a virtual environment
RUN python -m venv venv

# Activate the virtual environment
RUN /bin/bash -c "source venv/bin/activate"

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of your application code
COPY . .

# Command to run the application
CMD ["python", "your_script.py"]
