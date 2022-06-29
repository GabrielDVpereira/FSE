import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)

leds = [4, 17,27,5,6,13, 19, 26]

GPIO.setup(leds, GPIO.OUT)

p = GPIO.PWM(4, 100)
p.start(0)


def liga_lampadas(estado):
    for l in leds:
        print(l, ": ", estado)
        if(estado > 0):
            GPIO.output(l, GPIO.HIGH)
        else:
            GPIO.output(l, GPIO.LOW)
        sleep(2)


def main():
    print("Iniciando Testes!")

    liga = 0
    while True:
        if(liga == 0):
            liga = 1
            p.ChangeDutyCycle(30)
        else:
            liga = 0
            p.ChangeDutyCycle(0)
        sleep(1)

if __name__ == "__main__":
    main()