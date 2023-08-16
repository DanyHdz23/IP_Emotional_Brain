# Autor: Daniel Hernández Hernández
# Circuito_leds2
# Bibliotecas 
from machine import Pin
from time import sleep
import network

# Declaración de pines
led_rojo = Pin(5,Pin.OUT)
led_verde = Pin(18,Pin.OUT)

# Conexión Wifi
wf = network.WLAN(network.STA_IF)
wf.active(True)
wf.connect('nom_red', "contraseña_red")
while not wf.isconnected():
    led_rojo.value(1)
    sleep(1)
    led_rojo.value(0)
    sleep(1)
print(f"Conectado: {wf.ifconfig()[0]}")
led_verde.value(1)
sleep(1)