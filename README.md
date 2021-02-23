# What is simpletemp

simpletemp is a tool written in python, and it displays the current CPU temperature with current time and date, you could also enable email notification.

# **Requirements**

All things listed below are python libs.

The most are standard lib libs.

If you do not have all libs just choose an executable for your platform.

 1. Windows or Linux (for executable files)
 2. If you want to use the source file you need a python interpreter
 3. json
 4. os
 5. platform
 6. time
 7. smtplib
 8. ssl
 9. datetime
10. for the daemon bash

# **Installation**

[Go to](https://github.com/Adri11n/simpletemp/releases/tag/1.0) and search for an .zip that you want to use, download it, unzip it and run.

simpletemp.linux.executable.zip is for Linux, and it contains a Linux executable, config.json, configmaker and the simpletempd.sh file.

Run following to make sure you can run the program.

```
chmod +x simpletemp
```

Run following to run the program

```
./simpletemp
```

simpletemp.windows.zip is for windows, and it contains the Windows EXE and the config.json file.

You need admin rights to run it.

You might get a security warning don't worry it's because I compiled the source code without and cert.

Simpletemp.python.zip could be run everywhere where a python interpreter is running (only windows and Linux are supported) and it contains simpletemp.py, config.json, configmaker.py and simpletempd.sh.

To launch it a Linux with a python interpreter typ follow two lines.

```
chmod +x simpletemp.py
./simpletemp.py
```

# **Usage**

With this tool you will get your CPU temperature on Windows and Linux, with time and date.

![lol.png](/lol.png?fileId=104511#mimetype=image%2Fpng&hasPreview=true)You could also enable email notification when your CPU is getting to hot.

Also the python and the linux .zip file contains a bash script that acts like an daemon, so in case you want to run this software in the background.

# Config

only configure if you want to use email notification.

i have written an config script so you just simply run that script, enter some values and your ready to go.

this config script is not included by the windows zip because the email feature does not work there yet.

for the binary configmaker in simpletemp.linux.executable.zip make it executable and run it.

```
chmod +x configmaker
./configmaker
```

for the simpletemp.python.zipmake it executable and run.

```
chmod +x configmaker.py
./configmaker.py
```

now your ready

# How to use the Deamon ?

the daemon script is not included by the windows zip because it only works on linux.

make the daemon script executable with the following line.

```
chmod +x simpletempd.sh
```

it will detect if you're using a binary or the source python file and run it in the background.

now set up a crontab to start your simpletemp at reboot.

```
crontab -e
```

and paste follwing line in it (note replace the path to your simpletempd.sh)

```
@reboot /path/to/your/simpletempd.sh
```

now your ready.
