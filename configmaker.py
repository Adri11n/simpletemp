#!/usr/bin/python3
import json
import time
import getpass
from clear import clear
def makeconfig():
    max_temp = int(input("max temperatur >"))
    send_email = input("sender email >")
    reciever_email = input("Recipient E-mail >")
    smtp_server = input("Smtpserver >")
    smtp_port = int(input("Smtpserverport >"))
    while True:
        email_passwortcheck = getpass.getpass(prompt="email password >")
        email_passwortcheck2 = getpass.getpass(prompt="retype email password >")
        if email_passwortcheck == email_passwortcheck2:
            email_passwort = email_passwortcheck
            if len(email_passwort) == 0:
                print("password could not be 0 character\nplease retry")
                continue
            else:
                break
        elif email_passwortcheck != email_passwortcheck2:
            print("PASSWORD ERROR\nboth passwords doesnt match try again")
            continue
        else:
            print("password error")
            continue
    time1 = int(input("time interval >"))
    global confwrite
    confwrite = {
        "question": True,
        "max-temp": max_temp,
        "send-email": send_email,
        "reciever-email": reciever_email,
        "smtp-server": smtp_server,
        "smtp-port": smtp_port,
        "email-password": email_passwort,
        "time": time1
    }


def checkasw():
    time.sleep(3)
    clear()
    print("your entered values\n")
    print("max temperatur = " + str(confwrite["max-temp"]))
    print("sender email = " + str(confwrite["send-email"]))
    print("Recipient E-mail = " + str(confwrite["reciever-email"]))
    print("Smtpserver = " + str(confwrite["smtp-server"]))
    print("Smtpserverport = " + str(confwrite["smtp-server"]))
    print("email password = " + str(confwrite["email-password"]))
    print("time interval = " + str(confwrite["time"]))
    asw1 = input("\nare these values correct ? (yes/no) >")
    if asw1 == "yes":
        json_object = json.dumps(confwrite, indent=4)
        with open("config.json", "w") as outfile:
            outfile.write(json_object),
        print("goodbye")
        time.sleep(2)
        exit()
    elif asw1 == "no":
        clear()
        makeconfig()
        checkasw()
    else:
        print("error")
        time.sleep(2)
        checkasw()


makeconfi
checkasw()