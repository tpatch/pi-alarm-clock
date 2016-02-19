import RPi.GPIO as GPIO
import datetime

print(datetime.datetime.now().time())
#datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')

GPIO.setmode(GPIO.BCM)
# Pins to set up
# 1. Power (on/off)
# 2. Data


# Get alarm time from server (different script)

# Store time in case wifi connection is lost (different script)

# Check if current time matches alarm time

# If yes, trigger light sequence

# Detect button during light sequence to disable light