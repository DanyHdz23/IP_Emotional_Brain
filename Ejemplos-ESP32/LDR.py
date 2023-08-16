''' Autor: Daniel Hernández Hernández
Codigo básico para la lectura de una fotoresistencia (LDR)'''
# Bibliotecas
from machine import Pin, ADC
from time import sleep

# Pin a utilizar
ldr = ADC(Pin(34))

# Lectura de LDR
while True:
    valor = ldr.read_u16()
    luz = round((valor/65535)*100,2)
    print (f" Valor : {luz}")
    sleep(1)
    