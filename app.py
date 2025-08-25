from flask import Flask, render_template, request, jsonify, redirect, url_for
import json, datetime
import ph_orp
import pump_control
import mqtt_client

app = Flask(__name__)

CONFIG_FILE = "config.json"

def load_config():
    with open(CONFIG_FILE) as f:
        return json.load(f)

def save_config(cfg):
    with open(CONFIG_FILE, "w") as f:
        json.dump(cfg, f, indent=4)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/data")
def api_data():
    ph = ph_orp.read_ph()
    orp = ph_orp.read_orp()
    pump_status = pump_control.get_pump_status()
    return jsonify({"ph": ph, "orp": orp, "pump": pump_status})

@app.route("/settings", methods=["GET", "POST"])
def settings():
    cfg = load_config()
    if request.method == "POST":
        cfg["pump_schedule"] = request.json.get("pump_schedule", [])
        save_config(cfg)
        return jsonify({"status": "ok"})
    return render_template("settings.html", config=cfg)

@app.route("/maintenance", methods=["POST"])
def maintenance():
    cfg = load_config()
    cfg["maintenance_mode"] = not cfg.get("maintenance_mode", False)
    save_config(cfg)
    if cfg["maintenance_mode"]:
        pump_control.set_pump(False)
    return jsonify({"maintenance": cfg["maintenance_mode"]})

@app.route("/calibrate/start", methods=["POST"])
def calibrate_start():
    pump_control.set_pump(False)
    return render_template("calibration.html", step="start")

@app.route("/calibrate/save", methods=["POST"])
def calibrate_save():
    ph10_voltage = float(request.form.get("ph10_voltage"))
    ph_value = 10.0
    slope = (ph_value - 7.0) / (ph10_voltage - 2.5)  # Simplified
    cfg = load_config()
    cfg["ph_slope"] = slope
    cfg["ph_offset"] = ph_value - slope * ph10_voltage
    save_config(cfg)
    pump_control.set_pump(True)
    return redirect(url_for("dashboard"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
