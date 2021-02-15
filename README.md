# What is simpletemp

simpletemp is an tool written in python and it displays the currunt cpu temperature with current time and date, you could also enable email notification.

# **Requirements**

All things listed below are python libs.

The most are standart lib libs.

if you do not have all libs just an executable for your Plattform.

 1. Windows or LInux (for executable files)
 2. If you want to use the source file you need an python interpreter
 3. json
 4. os
 5. platform
 6. time
 7. smtplib
 8. ssl
 9. datetime
10. for the deamon bash

# **Installation**

[Go to](https://github.com/Adri11n/simpletemp/releases/tag/1.0) and search for an .zip that you want to use, download it, unzip it and run.

simpletemp.linux.executable.zip is for linux and it contains an linux executable, config.json and the simpletempd.sh file.

run following to make sure you can run the programm .

```
chmod +x simpletemp
```

run following to run the programm

```
./simpletemp
```

simpletemp.windows.zip is for windows and it contains the windows exe and the config.json file.

You need admin rights to run it.

You might get an security warning dont worry its because i compiled the source code without and cert.

simpletemp.python.zip could be run every where where an python interpreter is running (only windows and linux are supportet) and it contains simpletemp.py, config.json and simpletempd.sh.
