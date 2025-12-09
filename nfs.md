# NFS Quick Steps

## Storage Server
1. Install NFS packages
   sudo dnf install nfs-utils -y

2. Create directory
   sudo mkdir -p /media/nfs1
   sudo chmod -R 755 /media/nfs1

3. Edit /etc/exports
   /media/nfs1 *(rw,sync,no_root_squash)

4. Enable + start service
   sudo systemctl enable --now nfs-server

5. Apply exports
   sudo exportfs -rav

6. Open firewall
   sudo firewall-cmd --add-service=nfs --permanent
   sudo firewall-cmd --reload

## Client Machine
1. Install utilities
   sudo dnf install nfs-utils -y

2. Create mount point
   sudo mkdir -p /mnt/nfs1

3. Mount NFS
   sudo mount storage-server:/media/nfs1 /mnt/nfs1

4. /etc/fstab example
   storage-server:/media/nfs1 /mnt/nfs1 nfs defaults 0 0
