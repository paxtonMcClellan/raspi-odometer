#!/bin/bash

SERVICE_FILE=/etc/systemd/system/odometer.service

sudo bash -c "cat > $SERVICE_FILE" <<EOF
[Unit]
Description=Raspberry Pi Odometer
After=multi-user.target

[Service]
ExecStart=/home/pi/raspi-odometer/venv/bin/python /home/pi/raspi-odometer/src/main.py
WorkingDirectory=/home/pi/raspi-odometer/src
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable odometer.service
sudo systemctl start odometer.service

echo "Service installed and started"