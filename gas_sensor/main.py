from machine import Pin, ADC
import time

# Initialize the smoke sensor pin
smoke_sensor = ADC(Pin(34))

# Threshold value for smoke detection
SMOKE_THRESHOLD = 400

while True:
    print("adfafaf")
    sensor_value = smoke_sensor.read()
    print(sensor_value)
    if sensor_value > SMOKE_THRESHOLD:
        print("Smoke Detected!")
        # Add your action here (e.g., sound a buzzer, send a notification)
    else:
        print("No Smoke")
    time.sleep(1)