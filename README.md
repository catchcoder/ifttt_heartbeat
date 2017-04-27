# Build progress
![Alt text]("https://travis-ci.org/catchcoder/ifttt_heartbeat.svg?branch=mas")
# ifttt_heartbeat
python script that will send a trigger to https://ifttt.com/ with uptime and disk space emailed to user


# Run script every hour
Exmaple of cron job
0 * * * * python /home/pi/heartbeat/heartbeat.py >/dev/null 2>&1

