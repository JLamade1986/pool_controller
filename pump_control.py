import json
import mqtt_client

CONFIG_FILE = "config.json"

def load_config():
    with open(CONFIG_FILE) as f:
        return json.load(f)

def get_pump_status():
    return mqtt_client.pump_status

def set_pump(state: bool):
    mqtt_client.set_pump(state)
