import RPi.GPIO as GPIO
from datetime import datetime
import time
import setup
import config
from components.led import Single_Led
from components.led import Multi_Led
from components.weather_api import WeatherApi

# API
apiKey = config.apiKey
location = setup.lindholmen
option = 1
api = WeatherApi(location, apiKey)

# LEDS
multiLed = Multi_Led(
    "multi led", setup.multi_led["red"], setup.multi_led["blue"], setup.multi_led["green"])
greenLed = Single_Led("green", setup.single_greenPin)
redLed = Single_Led("red", setup.single_redPin)

switch_On = True
switch_Off = False

# Setting Up
# surpress warnings
GPIO.setwarnings(False)
# setup the pins accrding to B+ board rather than BCM
GPIO.setmode(GPIO.BOARD)

# set up multi-color LED #
GPIO.setup(multiLed.red, GPIO.OUT)
GPIO.setup(multiLed.green, GPIO.OUT)
GPIO.setup(multiLed.blue, GPIO.OUT)

# set up LED #
GPIO.setup(greenLed.pin, GPIO.OUT)
GPIO.setup(redLed.pin, GPIO.OUT)

# set up buttons #
# Set button pin to be an input pin and set initial value to be pulled low (off)
GPIO.setup(setup.leftButton["pin"], GPIO.IN)
GPIO.setup(setup.rightButton["pin"], GPIO.IN)

print(setup.multi_led)
print(setup.rightButton)
print(setup.leftButton)

multiLed.rainbow()
redLed.lightsOn()
greenLed.lightsOn()
time.sleep(3)
multiLed.lightsOut()
redLed.lightsOut()
greenLed.lightsOut()
print("{} led switch is {}".format(redLed.name, redLed.switch))
print("{} led switch is {}".format(greenLed.name, greenLed.switch))
print("{} led switch is {}".format(multiLed.name, multiLed.switch))

try:
    while True:
        if GPIO.input(setup.rightButton["pin"]) == 0:
            print("right")
            redLed.toggle()
            time.sleep(.5)
        elif GPIO.input(setup.leftButton["pin"]) == 0:
            print("left")
            greenLed.toggle()
            time.sleep(.5)
        else:
            multiLed.setColor(multiLed.blue)
finally:
    multiLed.lightsOut()
    greenLed.lightsOut()
    redLed.lightsOut()
