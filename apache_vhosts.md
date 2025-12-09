# Apache Virtual Hosts Quick Steps

## Install Apache
sudo dnf install httpd -y
sudo systemctl enable --now httpd

## Default Site
Place index.html in:
/var/www/html/index.html

## Create Virtual Host Directories
sudo mkdir -p /www/virtualhosts/site1.example.com
sudo mkdir -p /www/virtualhosts/site2.example.com

Add an index.html inside each.

## Add Directory Permissions
Edit /etc/httpd/conf/httpd.conf:

<Directory "/www/virtualhosts">
    AllowOverride None
    Require all granted
</Directory>

## Create vhost configs in /etc/httpd/conf.d/

### site1.example.com.conf
<VirtualHost *:80>
    DocumentRoot /www/virtualhosts/site1.example.com
    ServerName site1.example.com
    ErrorLog logs/site1-error.log
</VirtualHost>

### site2.example.com.conf
<VirtualHost *:80>
    DocumentRoot /www/virtualhosts/site2.example.com
    ServerName site2.example.com
    ErrorLog logs/site2-error.log
</VirtualHost>

### _default_.conf
<VirtualHost *:80>
    DocumentRoot /var/www/html
    ServerName www.example.com
</VirtualHost>

## Firewall
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --reload

## Restart Apache
sudo systemctl restart httpd

## DNS Notes
Create:
- A record for the web server hostname
- CNAMEs for each vhost → pointing to the A record
