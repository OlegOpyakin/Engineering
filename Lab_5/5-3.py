import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
led = [2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setup(led, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    value_res = 0 
    temp_value = 0
    for i in range(8):
        pow2 = 2 ** (8 - i - 1)
        temp_value = value_res + pow2
        signal = decimal2binary(temp_value)
        GPIO.output(dac, signal)
        time.sleep(0.005)
        compVal = GPIO.input(comp)
        if compVal == 0:
            value_res = value_res + pow2
    return value_res

try:
    while True:
        k = adc()
        print(k, '{:.2f}v'.format(3.3*k/256))
        if k >= 32:
            GPIO.output(led[0], 1)
        else: GPIO.output(led[0], 0)
        if k >= 64:
            GPIO.output(led[1], 1)
        else: GPIO.output(led[1], 0)
        if k >= 96:
            GPIO.output(led[2], 1)
        else: GPIO.output(led[2], 0)
        if k >= 128:
            GPIO.output(led[3], 1)
        else: GPIO.output(led[3], 0)
        if k >= 160:
            GPIO.output(led[4], 1)
        else: GPIO.output(led[4], 0)
        if k >= 192:
            GPIO.output(led[5], 1)
        else: GPIO.output(led[5], 0)
        if k >= 224:
            GPIO.output(led[6], 1)
        else: GPIO.output(led[6], 0)
        if k >= 240:
            GPIO.output(led[7], 1)
        else: GPIO.output(led[7], 0)



finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()