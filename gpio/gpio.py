'''   
    Programa simples que conecta leds em GPIO 
    https://sourceforge.net/p/raspberry-gpio-python/wiki/Outputs/
'''
import RPi.GPIO as GPIO
from time import sleep

# Define o padrao de numeracao das portas como BCM
# A outra opcap e GPIO.BOARD para usar o numero dos pinos fisicos da placa
GPIO.setmode(GPIO.BCM)

# portas da GPIO onde os leds estão conectados
GREEN_1 = 2
YELLOW_1 = 3
RED_1 = 11

GREEN_2 = 0
YELLOW_2 = 5
RED_2 = 6

semaforo_1 = [GREEN_1, YELLOW_1, RED_1]
semaforo_2 = [GREEN_2, YELLOW_2, RED_2]


states_1 = [[True, False, False], [False, True, False], [False, False, True]]

botoes =[10,9]
sensores_carros = [4, 17]

def configura_gpio():
    leds = semaforo_1 + semaforo_2
    for l in leds:
        GPIO.setup(l, GPIO.OUT)

    for b in botoes:
        GPIO.setup(b, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    for s in sensores_carros:
        GPIO.setup(s, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def liga_lampadas():
    active = []
    count = 0
    while True:
        if count >= 3:
            count = 0

        current_state = states_1[count]
        print(current_state)
        for i in range(0,3):
            if current_state[i]:
                GPIO.output(semaforo_1[i],  GPIO.HIGH)
            else:
                GPIO.output(semaforo_1[i], GPIO.LOW)

        sleep(2)
        count+=1

def trataEntradas(entradas):
    while True:
        ativos = []
        for e in entradas:
            if GPIO.input(e):
                ativos.append(e)
        print('Botoes ativos')
        print(ativos)
        sleep(0.5)

def tratarBotoesDebouncing():
    count = 0
    while True:
        for b in botoes:
            if GPIO.input(b):
                if count < 4:
                    count+=1
                if count == 4:
                    print('ativo {}'.format(b))
            else:
                if count > 0:
                    count -= 1
                if count == 0:
                    print('Inativo {}'.format(b))
        sleep(1)


def main():
    print("Iniciando Testes!")
    configura_gpio()

    option = int(input())

    if option == 1:
        liga_lampadas()
    elif option == 2:
        trataEntradas(botoes)
    elif option == 3:
        tratarBotoesDebouncing()
    elif option == 4:
        trataEntradas(sensores_carros)

if __name__ == "__main__":
    main()