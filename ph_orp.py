import time, statistics
import board, busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import json

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
ads.gain = 1

chan_ph = AnalogIn(ads, ADS.P0)
chan_orp = AnalogIn(ads, ADS.P1)

with open("config.json") as f:
    config = json.load(f)

ph_slope = config.get("ph_slope", 1.0)
ph_offset = config.get("ph_offset", 0.0)

PH_BUFFER = []
ORP_BUFFER = []
BUFFER_SIZE = 10

def _moving_average(buffer, new_value):
    buffer.append(new_value)
    if len(buffer) > BUFFER_SIZE:
        buffer.pop(0)
    return statistics.mean(buffer)

def read_ph(raw=False):
    voltage = chan_ph.voltage
    if raw:
        return voltage
    ph_value = ph_slope * voltage + ph_offset
    return round(_moving_average(PH_BUFFER, ph_value), 2)

def read_orp():
    mv = chan_orp.voltage * 1000
    return round(_moving_average(ORP_BUFFER, mv), 1)
