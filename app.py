import json
import random
import time

from flask import Flask
import paho.mqtt.client as mqtt

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    for i in range(50):
        salle = {"numero": random.randrange(5), "temperature": random.randrange(50), "presence": random.randrange(5)}
        client.publish("salles", json.dumps(salle))


client = mqtt.Client()
client.on_connect = on_connect

client.connect("192.168.1.42", 1883, 60)
client.loop_start()
