#!/usr/bin/env bash
#preparing the web servers for the deployment of web static.

#this will updates the machine and then install the nginx web servers
sudo apt-get update
sudo apt-get install nginx -y

#create the folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
#fake html page
echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
   Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# a symbolic link creation and if it already exists, delete it and create a new one
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default
sudo service nginx restart
