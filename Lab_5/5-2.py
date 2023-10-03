import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    k = 0
    for i in range(7, 0, -1):
        k+=2**i
        GPIO.output(dac, decimal2binary(k))
        time.sleep(0.005)
        if GPIO.input(comp) == 0:
            k-=2**i
    return k

try:
    while True:
        k = adc()
        print(k, '{:.2f}v'.format(3.3*k/256))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()