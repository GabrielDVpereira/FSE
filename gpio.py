'''   
    Programa simples que conecta leds em GPIO 
    https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/

'''
import RPi.GPIO as GPIO
from time import sleep

# Define o padrao de numeracao das portas como BCM
# A outra opcap e GPIO.BOARD para usar o numero dos pinos fisicos da placa
GPIO.setmode(GPIO.BCM) 

# portas da GPIO onde os leds estão conectados
leds = [13, 19, 26] 


def configura_gpio():
    for l in leds:
        GPIO.setup(l, GPIO.OUT)


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
    configura_gpio()

    liga = 0
    while True:
        if(liga == 0):
            liga = 1
        else:
            liga = 0
        liga_lampadas(liga)
        sleep(100/1000)

if __name__ == "__main__":
    main()