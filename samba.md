# Samba Quick Steps

## On Storage Server
1. Install Samba
   sudo dnf install samba samba-common samba-client -y

2. Create share directory
   sudo mkdir -p /media/samba1
   sudo chmod -R 777 /media/samba1

3. Edit /etc/samba/smb.conf
   [samba1]
       path = /media/samba1
       writable = yes
       browsable = yes
       guest ok = no

4. Create Samba user
   sudo adduser myuser
   sudo passwd myuser
   sudo smbpasswd -a myuser

5. Enable/start services
   sudo systemctl enable --now smb nmb

6. Firewall
   sudo firewall-cmd --add-service=samba --permanent
   sudo firewall-cmd --reload

## Windows Client
1. Open File Explorer
2. Connect using UNC:
   \\tatooine.starwars.com\samba1
3. Authenticate with Samba credentials
