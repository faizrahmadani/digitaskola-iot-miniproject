import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883


def on_message(client, userdata, msg):
    print(f"Topic: {msg.topic} | Data: {msg.payload.decode()}")


client = mqtt.Client(client_id="subscriber-faiz-iot")
client.on_message = on_message

client.connect(BROKER, PORT, 60)

client.subscribe("faizrahmadani-digitalskola/iot/#")
client.loop_forever()
