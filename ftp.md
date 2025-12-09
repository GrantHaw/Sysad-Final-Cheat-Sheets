# FTP / vsftpd Quick Steps

## On Storage Server
1. Update
   sudo dnf update -y

2. Install vsftpd
   sudo dnf install vsftpd -y

3. Enable + start service
   sudo systemctl enable --now vsftpd

4. Verify service
   ss -l | grep ftp

5. Firewall
   sudo firewall-cmd --add-service=ftp --permanent
   sudo firewall-cmd --reload

6. Add FTP user
   sudo adduser ftpuser
   sudo passwd ftpuser

## On Linux Client
1. Install FTP client
   sudo dnf install lftp -y

2. Connect
   lftp ftpuser@tatooine.starwars.com
