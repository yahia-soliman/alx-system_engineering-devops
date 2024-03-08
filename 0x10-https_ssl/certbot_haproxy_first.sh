#!/usr/bin/env bash
# secure HAProxy with Let's Encrypt
apt-get install certbot
service haproxy stop
certbot certonly
#follow the instructions just fill your email and domain name
cat /etc/letsencrypt/live/www.yahia.tech/{fullchain.pem,privkey.pem} > /etc/ssl/certs/www.yahia.tech.pem

sed -i 's/bind :80/bind :80\n\tbind :443 ssl crt \/etc\/ssl\/certs\/www.yahia.tech.pem/' /etc/haproxy/haproxy.cfg
haproxy -f /etc/haproxy/haproxy.cfg -c # validate config

# there was warnings
openssl dhparam -out /etc/haproxy/dhparams.pem 2048
sed -i '0,/global/{s/global/global\n\tssl-dh-param-file \/etc\/haproxy\/dhparams.pem/}' /etc/haproxy/haproxy.cfg

service haproxy start
