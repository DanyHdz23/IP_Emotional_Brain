'''Autor: Daniel Hernández Hernández
Este código muestra como conectar el microcontrolador ESP32 a nuestra red wifi.
También funciona para Raspberry Pi Pico W.
'''
# Biblioteca
import network
from time import sleep

# Conexión Wifi
wf = network.WLAN(network.STA_IF)
wf.active(True)
wf.connect('nom_red', "contraseña")
while not wf.isconnected():
    print('.')
    sleep(1)
print(f"Conectado: {wf.ifconfig()[0]}")