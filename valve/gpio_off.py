import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
gpio_pin = 26
GPIO.setup(gpio_pin, GPIO.OUT) # GPIO Assign mode
GPIO.output(gpio_pin, GPIO.LOW) # out
#GPIO.output(gpio_pin, GPIO.HIGH) # on
