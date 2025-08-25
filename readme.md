🏊‍♂️ Smart Pool Controller
Ein smarter Pool-Controller basierend auf Raspberry Pi 5, der pH-Wert, Redox (ORP), Temperatur überwacht und die Poolpumpe über einen Shelly Plus Plug S zeit- und sensorabhängig steuert.
Zusätzlich gibt es ein modernes Web-Dashboard mit animierten Grafiken und eine MQTT-Anbindung.

🚀 Features:
📊 Live-Dashboard (pH, ORP, Temperatur, Pumpenstatus, Verbrauch)
🕒 Zeitgesteuerte Pumpensteuerung (mehrere Zeitfenster über Web-UI konfigurierbar)
⚡ Integration von Shelly Plus Plug S (MQTT)
🛠️ Wartungsmodus (schaltet Pumpe sicher aus)
🛠️ Dosierpumpen werden ausgeschaltet und gesperrt, bis die Poolpumpe wieder eingeschaltet wird
🔧 Automatischer Kalibrierungs-Workflow für pH-Sonde
🔐 Optional: Passwortschutz für Weboberfläche
💾 Backup & Restore Funktion

🧩 Hardware (Raspberry Pi 5 Variante)
- Raspberry Pi 5 (empfohlen: 4–8 GB RAM Version)
- Original Raspberry Pi 5 Netzteil (5V / 5A USB-C)
- Raspberry Pi Chipsatzkühler Raspberry Pi Aktiv Kühler
- N07 M.2 PCIe to NVMe Bottom SSD Pip PCIe Peripheral Board for Raspberry Pi 5
- M.2 PCIe min. 128 GB SSD
- 2 x ADS1115 ADC (I²C)
- pH-Sensor BNC Modul + Elektrode
- ORP-Sensor BNC Modul + Elektrode
- DS18B20 Temperaturfühler (wasserdicht)
- 4.7 kΩ Widerstand für DS18B20 Pullup
- Shelly Plus Plug S (für Poolpumpe)


📦 Installation
Projekt herunterladen und entpacken:
git clone https://github.com/<dein-user>/pool-controller.git
cd pool-controller


Installation starten:
./install.sh


Systemdienst einrichten:
sudo cp service/pool_controller.service /etc/systemd/system/
sudo systemctl enable pool_controller.service
sudo systemctl start pool_controller.service


Weboberfläche öffnen:
http://<raspi-ip>:5000

⚙️ Beispiel-Konfiguration (config/config.json)
{
  "mqtt": {
    "broker": "192.168.1.245",
    "port": 1883,
    "topic_pump": "pool/pump",
    "topic_sensors": "pool/sensors"
  },
  "pump": {
    "schedule": [
      { "start": "08:00", "end": "12:00" },
      { "start": "16:00", "end": "20:00" }
    ]
  },
  "ph": {
    "min": 7.0,
    "max": 7.4
  },
  "orp": {
    "min": 650,
    "max": 750
  }
}

📊 Dashboard Screenshots
Übersicht
Kalibrierung
Pumpensteuerung

🛠️ Wartungs- / Entwicklerinfos
Python 3.11+
Flask für Webserver
MQTT via paho-mqtt
Charts via Chart.js
TailwindCSS für modernes UI
Systemd für Autostart

📜 Lizenz
MIT License – frei nutzbar für private & kommerzielle Projekte.
