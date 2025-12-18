import paho.mqtt.client as mqtt
import time
import random

BROKER = "broker.hivemq.com"
PORT = 1883

client = mqtt.Client(client_id="publisher-faiz-iot")
client.connect(BROKER, PORT, 60)

while True:
    payload = {
        "energy": round(random.uniform(100, 500), 2),
        "room_temp": round(random.uniform(24, 30), 2),
        "motor_rpm": random.randint(800, 1500)
    }

    client.publish("faizrahmadani-digitalskola/iot/energy", payload["energy"])
    client.publish("faizrahmadani-digitalskola/iot/room", payload["room_temp"])
    client.publish("faizrahmadani-digitalskola/iot/motor", payload["motor_rpm"])

    print("Publish:", payload)
    time.sleep(5)
