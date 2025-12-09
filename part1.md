# Part I Practical Checklist (Infrastructure Build)

## 1. Build Linked Clones (All on Thawspace T:)
- pfSense
- Windows Server 2025
- Windows 11
- Rocky Linux

Create linked clones only. Name folders meaningfully.

## 2. Configure Networking (LAN Segment)
In VMware:
- Create a LAN Segment (Net01 or similar)
- pfSense:
  - Adapter 1: NAT (WAN)
  - Adapter 2: LAN Segment
- All other VMs: LAN Segment only

## 3. Configure pfSense
On console:
1) Assign Interfaces → WAN = NAT MAC, LAN = segment MAC
2) Set LAN IP:
   192.168.1.254/24
3) Disable DHCP on pfSense
4) Confirm LAN/WAN addresses

## 4. Configure Windows Server 2025 Networking
Set static IPv4:
- IP: 192.168.1.1
- Gateway: 192.168.1.254
- DNS: 192.168.1.1 (self)
Verify:
- ping pfSense
- ping external (optional if allowed)

## 5. Install AD DS, DNS, DHCP
Server Manager → Add Roles and Features:
- Active Directory Domain Services
- DNS Server
- DHCP Server

Promote to domain controller:
- Domain: <your RIT username>.com
- NetBIOS auto-fill
- Set DSRM password

## 6. Configure DHCP
DHCP console:
- Create IPv4 scope:
  Range: 192.168.1.50–192.168.1.200
  Mask: /24
  Router: 192.168.1.254
  DNS: 192.168.1.1
- Activate scope

## 7. Add a User to AD
ADUC:
- Create OU (e.g., Workstations or Users)
- Create user (testuser)
- Set password options

## 8. Join Windows 11 to the Domain
On Windows 11:
System → Rename this PC → Join domain
Domain: <your RIT username>.com
Login using testuser + domain password
Reboot

## 9. Validate
- Windows 11 receives DHCP IP from Server 2025
- Windows 11 can ping domain controller
- Windows 11 authenticates domain user

If all above works, you get the full 60 pts.
