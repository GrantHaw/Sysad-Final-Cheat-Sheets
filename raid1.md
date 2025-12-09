# RAID 1 Quick Steps (mdadm)

## Identify Available Drives
lsblk

Choose unused disks, e.g.:
  /dev/nvme0n3
  /dev/nvme0n4

## Create RAID 1
sudo mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/nvme0n3 /dev/nvme0n4

Check status:
cat /proc/mdstat

## Partition RAID Device
sudo fdisk /dev/md0

Inside fdisk:
  - Create MBR partition table (DOS)
  - Primary partition: 1GB
  - Extended partition: remainder
  - Logical partition inside extended
  - Write and quit

Verify:
ls /dev | grep md0

## Format Partitions
sudo mkfs.xfs /dev/md0p1
sudo mkfs.xfs /dev/md0p5

## Mount Partitions
sudo mkdir /media/nfs1
sudo mkdir /media/nfs2

sudo mount /dev/md0p1 /media/nfs1
sudo mount /dev/md0p5 /media/nfs2

Check:
mount | grep md0
