#!/usr/bin/python3
from fabric import Connection


def install_bnb_deps(c: Connection):
    """install required dependencies for the deployment"""
    c.run(
        "sudo apt install python3-dev default-libmysqlclient-dev"
        "build-essential pkg-config net-tools python3-pip tmux"
    )
    c.run("pip install --user flask flask-cors mysqlclient sqlalchemy gunicorn")


def update_nginx_config(c: Connection, config_file: str):
    """change the nginx config file with the one needed in the task"""
    c.put(config_file, "/etc/nginx/sites-available/default")
    c.run("sudo nginx -t")
    c.run("sudo service nginx restart")


def run_production(c: Connection):
    """run the server for production using gunicorn"""
    if c.run("test -d AirBnB_clone_v4", warn=True).failed:
        c.run("git clone https://github.com/yahia-soliman/AirBnB_clone_v4.git")
    c.cd("AirBnB_clone_v4")
    c.run("gunicorn --bind 0.0.0.0:5003 web_dynamic.100-hbnb:app")


if __name__ == "__main__":
    c = Connection(host="web-01.yahia.tech", user="ubuntu")
    install_bnb_deps(c)
    update_nginx_config(c, "5-app_server-nginx_config")
    run_production(c)
