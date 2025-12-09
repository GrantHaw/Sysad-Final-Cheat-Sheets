# Group Policy Quick Steps

## Create OUs + Users
1. Open AD Users and Computers
2. Right-click domain → New → Organizational Unit
3. Create an OU
4. Inside OU → New → User

## Create a GPO
1. Open Group Policy Management
2. Right-click OU → Create a GPO in this domain, and Link it here
3. Name appropriately (PasswordPolicy, LoginScript, MappedDrive, etc.)

## Edit GPO

### Password Policy
Computer Config → Policies → Windows Settings → Security Settings → Account Policies → Password Policy

### Login Script
User Config → Policies → Windows Settings → Scripts (Logon)

### Drive Mapping
User Config → Preferences → Windows Settings → Drive Maps

## Force Update on Client
gpupdate /force
