# ifttt_heartbeat
python script that will send a trigger to https://ifttt.com/ with uptime and disk space emailed to user


Add a Cron job to run the script every hour

Example:
# Send email every hour 
0 * * * * python /home/pi/heartbeat/heartbeat.py >/dev/null 2>&1

