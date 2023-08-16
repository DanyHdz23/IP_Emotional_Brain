# Autor: Daniel Hernández Hernández
# Bibliotecas 
from machine import Pin
from time import sleep

# Declaración de pines
led_rojo = Pin(5,Pin.OUT)
led_verde = Pin(18,Pin.OUT)

# Ciclo infnito para parpadeo de leds
while True:
    led_rojo.value(1) 
    sleep(1)
    led_rojo.value(0)
    sleep(1)
    led_verde.value(1)
    sleep(1)
    led_verde.value(0)
    sleep(1)
    