cp /services/python-count.service /etc/system/systemd/
sudo systemctl daemon-reload
sudo systemctl enable python-count.service
sudo systemctl start python-count.service

