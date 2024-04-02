# Use a Python base image
FROM python:latest

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy only necessary files
COPY . .

# Install dependencies
RUN apt-get update \
    && apt-get install -y git build-essential \
    && pip install --verbose -r requirements.txt \
    && pip install --no-cache-dir gpiozero \
    && git clone https://github.com/RPi-Distro/RTIMULib.git \
    && cd RTIMULib/Linux/python \
    && python setup.py install \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set PYTHONPATH to include the src directory
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app/src"

# Set PYTHONPATH to include the stubs directory
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app/src/stubs"

# Run the Python application
CMD ["python", "src/app.py"]
