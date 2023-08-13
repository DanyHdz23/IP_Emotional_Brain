''' Autor: Daniel Hernández Hernández
Este codigo es una parte del proyecto I:P Emotional Brain
Analisis de imagenes capturadas por ESP32 CAM, publicadas en MQTT y visualizacion en Node-Red.
Las imagenes deben encontrarse en el ordenador y en la misma carpeta.'''

# Librerias
from deepface import DeepFace
import paho.mqtt.client as mqtt

# Conexión a mqtt
client = mqtt.Client()
client.connect("IP",port,60)

# Analisis de la captura
emotion = DeepFace.analyze(img_path='direccion de la imagen: home/captura, etc', actions=['emotion','age','gender'])
parametro = emotion[0]['dominant_emotion']
client.publish("Topic a publicar", parametro)
print(f"El resultado es: {parametro}")
