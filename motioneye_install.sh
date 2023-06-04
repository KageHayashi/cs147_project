#!/bin/bash

apt-get install ffmpeg libmariadb3 libpq5 libmicrohttpd12 -y
wget https://github.com/Motion-Project/motion/releases/download/release-4.3.2/pi_buster_motion_4.3.2-1_armhf.deb 
dpkg -i pi_buster_motion_4.3.2-1_armhf.deb
systemctl stop motion
systemctl disable motion

apt-get install python2 python-dev-is-python2 -y

curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py

python2 get-pip.py

apt-get install libssl-dev libcurl4-openssl-dev libjpeg-dev zlib1g-dev -y

pip2 install motioneye

mkdir -p /etc/motioneye
cp /usr/local/share/motioneye/extra/motioneye.conf.sample /etc/motioneye/motioneye.conf

mkdir -p /var/lib/motioneye

cp /usr/local/share/motioneye/extra/motioneye.systemd-unit-local /etc/systemd/system/motioneye.service
systemctl daemon-reload
systemctl enable motioneye
systemctl start motioneye

pip install motioneye --upgrade
systemctl restart motioneye