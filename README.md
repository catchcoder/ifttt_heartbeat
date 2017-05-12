# Build progress
![Travis CI](https://travis-ci.org/catchcoder/ifttt_heartbeat.svg?branch=master "Progress")

# Using **If this then that** to send a email heartbeat

>This python script that will send a trigger to [ifttt.com](https://ifttt.com/) with uptime and disk space then *ifttt* wil send a email.



 ## Run script every hour
 Add cron job to run every hour or set the schedule to what you require
* Run crontab -e
* Add example below

`0 * * * * python /home/pi/heartbeat/heartbeat.py >/dev/null 2>&1`
