''' Autor: Daniel Hernández Hernández
Codigo básico para el uso del sensor DHT11'''
#Biblioteca
from machine import Pin
from time import sleep
from dht import DHT11

#Pin a utilizar en la placa
sensor = DHT11(Pin(15))

# ciclo de lectura
while True:
    sensor.measure()
    print (f" Temp = {sensor.temperature()} , Hum = {sensor.humidity()} ")
    sleep(1)