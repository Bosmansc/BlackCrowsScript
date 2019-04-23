# BlackCrowsScript
Automated Python script to track the sales price of a set of skis.

## Windows Task Scheduler Settings

Use windows scheduler to daily run the python script.

1) go to administrative tools
2) choose task scheduler
3) create a basic task (on the right of the screen)
4) set the name etc. and browse to the SkiScraping.py file

-> an email will be sent if the sales price has fallen


Use the following settings to "Start a program" in the task scheduler:

-  Program/script: Full path to Python.exe, C:\Python27\ArcGIS10.2\python.exe

-  Arguments: Name of script, script.py

-  Start in: Location of script.py, something like C:\path\to\script

