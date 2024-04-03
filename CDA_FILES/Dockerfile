FROM python

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app/

# Install dependencies
RUN pip install --verbose -r requirements.txt
RUN pip install --no-cache-dir gpiozero

# Set PYTHONPATH to include the src directory
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app/src"

# Display PYTHONPATH for debugging (optional)
RUN echo $PYTHONPATH

# Install RTIMU
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/RPi-Distro/RTIMULib.git
RUN cd RTIMULib/Linux/python && python setup.py install

# Set PYTHONPATH to include the stubs directory
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app/src/stubs"

# Run the Python application
CMD ["python", "src/app.py"]