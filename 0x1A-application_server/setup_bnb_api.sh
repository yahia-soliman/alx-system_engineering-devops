#!/usr/bin/env bash
sudo apt-get -y install python3-dev default-libmysqlclient-dev build-essential pkg-config net-tools python3-pip tmux
pip install --user flask flask-cors mysqlclient sqlalchemy gunicorn
git clone https://github.com/Mrelshimy/AirBnB_clone_v3 && cd AirBnB_clone_v3
tmux new-session -d 'gunicorn --bind 0.0.0.0:5002 api.v1.app:app'
sudo sed -i '0,/location \/ {/s//location \/api\/ {\n\t\tinclude proxy_params;\n\t\tproxy_pass http:\/\/0.0.0.0:5002;\n\t}\n\n\tlocation \/ {/' /etc/nginx/sites-available/default
sudo nginx -t && sudo service nginx restart
