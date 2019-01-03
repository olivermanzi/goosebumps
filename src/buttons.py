import RPi.GPIO as GPIO
import time

redPin = 11  # GPIO 17
greenPin = 13  # GPIO 22
bluePin = 15  # GPIO 27

leftB = 18  # GPIO 24 [left]
rightB = 16  # GPIO 23 [right]

switch_On = True
switch_Off = False

# all the color codes
red = [redPin]
green = [greenPin]
blue = [bluePin]
yellow = [redPin, greenPin]
puprle = [redPin, bluePin]
cyan = [green, blue]
white = [red, blue, green]
_rgb = [red, green, blue]
allColors = [red, green, blue, yellow, puprle, cyan, white]


def toggle(pin, switch):
    GPIO.output(pin, switch)


def lightsOut():
    for pin in _rgb:
        toggle(pin, switch_Off)


def setColor(colors):
    # switch off leds
    lightsOut()
    # log color
    print(colors)
    for color in colors:
        toggle(color, switch_On)


def rainbow():
    for color in allColors:
        setColor(color)
        time.sleep(.5)


# surpress warnings
GPIO.setwarnings(False)
# setup the pins accrding to B+ board rather than BCM
GPIO.setmode(GPIO.BOARD)
# set up RGB led pins
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
# set up buttons
GPIO.setup(leftB, GPIO.IN)
GPIO.setup(rightB, GPIO.IN)

start = 0
end = len(allColors)
print("end"+str(end))

current = start
setColor(allColors[current])
while True:
    print("current is {}".format(current))
    if GPIO.input(rightB) == 0:
        print("inside right")
        nextNum = current + 1
        if(nextNum == end):
            current = start
            setColor(allColors[current])
        else:
            current += 1
            setColor(allColors[current])
    elif GPIO.input(leftB) == 0:
        print("inside left")
        prev = current-1
        if(prev < start):
            current = end-1
            setColor(allColors[current])
        else:
            current -= 1
            setColor(allColors[current])

    time.sleep(0.25)