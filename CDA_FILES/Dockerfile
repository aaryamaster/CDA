# Use the Python official image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY CDA_FILES/requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --verbose -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Command to run the application
CMD ["python", "app.py"]
