# Cron Cheatsheet

## Open Your User Crontab
crontab -e

This opens your personal cron table. Each line = one scheduled job.

## Basic Format
* * * * * command
| | | | |
| | | | ----- Day of week (0-7 Sunday)
| | | ------- Month (1-12)
| | --------- Day of month (1-31)
| ----------- Hour (0-23)
------------- Minute (0-59)

## Always Use Full Paths
Example:
  /home/student/script.sh
  /usr/bin/rsync
  /usr/bin/bash

## View Your Crontab
crontab -l

## Remove Your Crontab
crontab -r


# -------------------------------
# Common Scheduling Examples
# -------------------------------

## Run Every 1 Minute
* * * * * /home/student/script.sh

## Run Every 5 Minutes
*/5 * * * * /home/student/script.sh

## Run Every 15 Minutes
*/15 * * * * /home/student/script.sh

## Run Every Hour at :00
0 * * * * /home/student/script.sh

## Run Every Hour at :30
30 * * * * /home/student/script.sh

## Run Daily at Midnight
0 0 * * * /home/student/script.sh

## Run Daily at 3 AM
0 3 * * * /home/student/script.sh

## Run Every Monday at 8 AM
0 8 * * 1 /home/student/script.sh

## Run on the 1st of Every Month at Midnight
0 0 1 * * /home/student/script.sh

## Run Every Weekend at 2 AM (Sat & Sun)
0 2 * * 6,0 /home/student/script.sh

## Run Only on Weekdays at 7 PM
0 19 * * 1-5 /home/student/script.sh


# -------------------------------
# Testing Cron-Manually + Debugging
# -------------------------------

## 1. Run the script manually to confirm it works
/home/student/script.sh

## 2. Redirect cron output to a log file (recommended)
*/5 * * * * /home/student/script.sh >> /home/student/cron_output.log 2>&1

## 3. View system cron logs (depending on distro)
sudo journalctl -u crond
sudo grep CRON /var/log/cron
sudo tail -f /var/log/cron

## 4. Check permissions
chmod +x /home/student/script.sh

## 5. Check absolute paths inside your script
Use full paths for everything:
  /usr/bin/rsync
  /usr/bin/date
  /usr/bin/hostname


# -------------------------------
# Environment Notes
# -------------------------------

Cron does NOT load your normal shell environment.
If your script depends on PATH, set it manually at the top of the job:

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

Example:
0 * * * * PATH=/usr/bin:/bin /home/student/script.sh


# -------------------------------
# Example Full Working Cron Entry
# -------------------------------

# Run backup script every 10 minutes and log output
*/10 * * * * PATH=/usr/bin:/bin /home/student/script.sh >> /home/student*
