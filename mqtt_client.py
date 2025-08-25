import paho.mqtt.client as mqtt
import json

with open("config.json") as f:
    config = json.load(f)

BROKER = config["mqtt_broker"]
TOPIC_STATUS = config["mqtt_topic_status"]
TOPIC_POWER = config["mqtt_topic_power"]

pump_status = False
pump_power = 0.0

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    client.subscribe(TOPIC_STATUS)
    client.subscribe(TOPIC_POWER)

def on_message(client, userdata, msg):
    global pump_status, pump_power
    if msg.topic == TOPIC_STATUS:
        pump_status = msg.payload.decode() == "on"
    elif msg.topic == TOPIC_POWER:
        pump_power = float(msg.payload.decode())

def set_pump(state: bool):
    client.publish(TOPIC_STATUS, "on" if state else "off")

client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, 1883, 60)
client.loop_start()
