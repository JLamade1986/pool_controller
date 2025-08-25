from ph_orp import read_ph
import time, json

with open("config.json") as f:
    config = json.load(f)

print("Starte manuelle pH-Kalibrierung (7.0 -> 4.0 -> 10.0) ...")
points = {}
for ph in [7.0, 4.0, 10.0]:
    input(f"Elektrode in pH {ph} Lösung tauchen und ENTER drücken ...")
    time.sleep(10)
    points[ph] = read_ph(raw=True)
    print(f"-> Rohspannung bei pH {ph}: {points[ph]:.4f} V")

slope = (10.0 - 4.0) / (points[10.0] - points[4.0])
offset = 4.0 - slope * points[4.0]

config["ph_slope"]  = slope
config["ph_offset"] = offset
with open("config.json","w") as f:
    json.dump(config,f,indent=2)

print(f"Fertig. Neue Kalibrierung gespeichert: pH = {slope:.4f} * V + {offset:.4f}")
