import random
import time
from sense_hat import SenseHat
from gpiozero import Device, OutputDevice
from gpiozero.pins.mock import MockFactory 

# Use MockFactory to replace RPi.GPIO with mock pins
Device.pin_factory = MockFactory()

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

# Function to simulate controlling HVAC actuator using GPIO
def control_hvac_actuator_gpio():
    hvac_pin = OutputDevice(18)  # Initialize GPIO pin for the HVAC actuator
    hvac_pin.on()  # Turn on the HVAC actuator
    print("HVAC actuator turned on")
    time.sleep(2)  # Wait for some time
    hvac_pin.off()  # Turn off the HVAC actuator
    print("HVAC actuator turned off")

# Function to read temperature sensor using Sense HAT
def read_temperature_sensor_sensehat():
    sense = SenseHat()  # Initialize Sense HAT object
    temperature = sense.get_temperature()  # Read temperature from Sense HAT
    return temperature

# Function to read humidity sensor using Sense HAT
def read_humidity_sensor_sensehat():
    sense = SenseHat()  # Initialize Sense HAT object
    humidity = sense.get_humidity()  # Read humidity from Sense HAT
    return humidity

# Function to read pressure sensor using Sense HAT
def read_pressure_sensor_sensehat():
    sense = SenseHat()  # Initialize Sense HAT object
    pressure = sense.get_pressure()  # Read pressure from Sense HAT
    return pressure

# Test the GPIO control function
control_hvac_actuator_gpio()
