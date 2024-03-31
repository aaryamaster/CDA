import random
import sense_hat
import RPi.GPIO as GPIO
import time

# Function to simulate reading temperature sensor
def read_temperature_sensor():
    temperature = random.uniform(20.0, 30.0)  # Simulate temperature between 20.0°C and 30.0°C
    return temperature

# Function to simulate reading humidity sensor
def read_humidity_sensor():
    humidity = random.uniform(40.0, 60.0)  # Simulate humidity between 40% and 60%
    return humidity

# Function to simulate reading pressure sensor
def read_pressure_sensor():
    pressure = random.uniform(1000.0, 1020.0)  # Simulate pressure between 1000.0 hPa and 1020.0 hPa
    return pressure

# Function to simulate controlling HVAC actuator
def control_hvac_actuator():
    print("HVAC actuator controlled")  # Placeholder for actual action

# Function to read temperature sensor using Sense HAT
def read_temperature_sensor_sensehat():
    sense = sense_hat.SenseHat()  # Initialize Sense HAT object
    temperature = sense.get_temperature()  # Read temperature from Sense HAT
    return temperature

# Function to read humidity sensor using Sense HAT
def read_humidity_sensor_sensehat():
    sense = sense_hat.SenseHat()  # Initialize Sense HAT object
    humidity = sense.get_humidity()  # Read humidity from Sense HAT
    return humidity

# Function to read pressure sensor using Sense HAT
def read_pressure_sensor_sensehat():
    sense = sense_hat.SenseHat()  # Initialize Sense HAT object
    pressure = sense.get_pressure()  # Read pressure from Sense HAT
    return pressure

# Define GPIO pin for the HVAC actuator
HVAC_PIN = 18

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(HVAC_PIN, GPIO.OUT)

# Function to control HVAC actuator using GPIO
def control_hvac_actuator_gpio():
    GPIO.output(HVAC_PIN, GPIO.HIGH)  # Turn on the HVAC actuator
    print("HVAC actuator turned on")
    time.sleep(2)  # Wait for some time
    GPIO.output(HVAC_PIN, GPIO.LOW)  # Turn off the HVAC actuator
    print("HVAC actuator turned off")

# Cleanup GPIO
GPIO.cleanup()
