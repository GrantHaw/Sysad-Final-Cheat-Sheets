# RAID 5 Quick Steps (mdadm)

## Identify 3+ unused drives
lsblk

Choose three unused disks, e.g.:
/dev/nvme0n5
/dev/nvme0n6
/dev/nvme0n7

## Create RAID 5 array
sudo mdadm --create /dev/md1 --level=5 --raid-devices=3 /dev/nvme0n5 /dev/nvme0n6 /dev/nvme0n7

## Watch sync status
cat /proc/mdstat

## Create filesystem (XFS or ext4)
sudo mkfs.xfs /dev/md1

## Create mount point
sudo mkdir -p /media/raid5

## Mount it
sudo mount /dev/md1 /media/raid5

## Verify
df -h | grep md1

## (Optional) Permanent entry in /etc/fstab
/dev/md1   /media/raid5   xfs   defaults   0 0

## Save RAID config (recommended)
sudo mdadm --detail --scan | sudo tee -a /etc/mdadm.conf
