import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

leds = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(leds, GPIO.OUT)

try:
    while True:
        a = input('Пожалуйста, введите число от 0 до 255: ')
        if a == 'q':
            break
        if a.isdigit() is False:
            print('Вы ввели букву, а не число')
        elif int(a)>255:
            print('Слишком большое число!')
        elif int(a)<0:
            print('Нельзя вводить отрицательное число!')
        else:
            b = float(a)
            a = decimal2binary(int(a))
            print('Выходное напряжение примерно равно ',3.3/256*b)
            GPIO.output(leds, a)
            
finally:
    GPIO.cleanup()