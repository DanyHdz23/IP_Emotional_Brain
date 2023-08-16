'''Autor: Daniel Hernández Hernández
Este código muestra el uso básico de un servo motor con PWM, para el cambio de posicion de 0°  a 180°'''
#Bibliotecas
from machine import Pin, PWM
from time import sleep

#Pin y frecuencia de pulso
servo=PWM(Pin(19))
servo.freq(50)

#Ciclo de trabajo 0° a 180° y 180° a 0° 
while True:
    servo.duty_u16(1311)
    sleep(2)
    servo.duty_u16(7864)
    sleep(2)
    