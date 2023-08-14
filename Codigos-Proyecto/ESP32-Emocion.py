from umqtt.simple import MQTTClient
import ujson
from time import sleep
import network
from machine import Pin, ADC, PWM
from dht import DHT11

servo=PWM(Pin(32))
servo.freq(50)
sensor = DHT11(Pin(15))
ldr = ADC(Pin(34))
led_rojo = Pin(5,Pin.OUT)
led_verde = Pin(18,Pin.OUT)
led_blanco = Pin (19,Pin.OUT)
# Conexión Wifi
wf = network.WLAN(network.STA_IF)
wf.active(True)
wf.connect('INFINITUM4554_2.4', "7jFWfAkRFn")
while not wf.isconnected():
    led_rojo.value(1)
    sleep(1)
    led_rojo.value(0)
    sleep(1)
print(f"Conectado: {wf.ifconfig()[0]}")
led_verde.value(1)
sleep(1)

#Conexion a MQTT
name = "ignis"
addr = "192.168.1.174"
topic = b'Emociones/mqtt'
mqtt = MQTTClient(name, addr , keepalive=60)
mqtt.connect()

def temp():
    #sensor.measure()
    Temp= sensor.temperature()
    msg_temp= ujson.dumps({"temp": Temp})
    if Temp >=31:
        servo.duty_u16(1311)
        sleep(2)
    elif Temp <=29:
         servo.duty_u16(7864)
         sleep(2)
    else:
        print("normal")
    return msg_temp

#Luminosidad
def Lum():
    valor = ldr.read_u16()
    eq = (valor/65535)*100
    lum = ujson.dumps({"lum": eq})
    if eq <=80:
        led_blanco.value(1)
        sleep(1)
    elif eq >=85:
        led_blanco.value(0)
        sleep(1)
    else:
        print("normal")
    return lum

while True:
    sensor.measure()
    mqtt.publish(topic, temp())
    sleep(3)
    mqtt.publish(topic, Lum())
    sleep(3)