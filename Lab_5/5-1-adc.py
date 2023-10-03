import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
bits = len(dac)
levels = 2**bits
comp = 14
troyka = 13

GPIO.setwarnings(False)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
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
        value = adc()
        voltage = value / levels * 3.3
        print("Sig = ",value," Volts = ", voltage)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()