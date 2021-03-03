#!/usr/bin/python3
import json
import os
from clear import clear
import time
import smtplib
import ssl
import platform
from datetime import date
from datetime import datetime

with open('config.json') as config_file:
    data = json.load(config_file)
question = data['question']
max_temp = data['max-temp']
send_email = data['send-email']
reciever_email = data['reciever-email']
password = data['email-password']
smtp_server = data['smtp-server']
smtp_port = data['smtp-port']
howoften = data['time']
cmdwin = "wmic /namespace:\\\\root\\wmi PATH MSAcpi_ThermalZoneTemperature GET CurrentTemperature | findstr /v \"C\""
cmd = "cat /sys/class/thermal/thermal_zone0/temp"
a = " °C"
amount = 0
lol = platform.system()
clear()
print("""simpletemp  Copyright (C) 2021  Adriaan van Vliet
This program comes with ABSOLUTELY NO WARRANTY; for details go to https://www.gnu.org/licenses/gpl-3.0.txt.
This is free software, and you are welcome to redistribute it
under certain conditions; go to https://www.gnu.org/licenses/gpl-3.0.txt for details.
""")
time.sleep(3)
print("Temp  | Time")
while True:
    if lol == "Windows":
        temp = os.popen(cmdwin).read()
        temp = temp[0:2]
    else:
        temp = os.popen(cmd).read()
        temp = temp[0:2]
    today = date.today()
    today = today.strftime("%d/%m/%Y")
    today = " " + today
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_time = " | " + current_time
    time.sleep(howoften)
    print(temp + a + current_time + today)
    if not question :
        continue
    elif int(temp) > max_temp:
        if amount == 0:
            amount = 1
            today = date.today()
            today = today.strftime("%d/%m/%Y")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            message = """\
Subject: The temperature of your computer has exceeded {} degrees celsius
The temperature of your computer has exceeded {} degrees celsius
                
Your computer is {} degrees celsius warm

The Time is {} and the Date is {}
    
This email is only sent once""".format(max_temp, max_temp, temp, current_time, today)
            try:
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
                    server.login(send_email, password)
                    server.sendmail(send_email, reciever_email, message)
            except:
                print("email error")
    elif int(temp) < max_temp:
        amount = 0
        continue
    else:
        continue