# Send email alert using ifttt
#
import  datetime, subprocess, requests, socket

trigger = "{put event trigger name here"
secret = "{put secrey key here}"

def uptime():
        pipe = subprocess.Popen(['uptime',"| sed \'s/.*up \([^,]*\), .*/\1/\'"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        name = pipe.communicate()[0]
        #pipe.wait(timeout=120)
        return name.strip()

def diskspace():
        pipe = subprocess.Popen(["df -H | grep -vE '^Filesystem|tmpfs|cdrom'"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        #pipe.wait(timeout=120)
	name = pipe.communicate()[0]
        return name.replace('\n', '<br />')


def email_alert():
        report = {}
        report["value1"] = socket.gethostname()
        report["value2"] = uptime()
        report["value3"] = diskspace()
        requests.post("https://maker.ifttt.com/trigger/" + trigger + "/with/key/" + secret, data=report)

# send trigger to ifttt with uptime and disk space
email_alert()
        
