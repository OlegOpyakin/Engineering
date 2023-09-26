import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

try:
    x = int(input('Введите коэффициент заполнения от 0 до 100: '))
    p = GPIO.PWM(24, 1000)
    p.start(x) 
    input('press any key to stop ')
    p.stop()
finally:
    GPIO.output(24, 0)
    GPIO.cleanup()