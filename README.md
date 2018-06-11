# Launch-3-pi-Code

Four different sets of code. For the crontab, keep in mind that Linux is case-sensitive. Crontabs need to be updated with current location of the code.

balloonVidsOnly-up.py - 
Intended for the payload's upward-facing camera. 
Takes a continous video for 5 hours, breaks it up into 10 min videos. 
Saves files in /home/pi/Launch3VidsOnlyup/Folder### .
When called the "first time" (i.e. Launch3VidsOnlyup does not exist), it sleeps for 1 hour before continuing. 
Crontab: @reboot python -u /home/pi/FINALCODE/balloonVidsOnly-up.py >>/home/pi/balloonviduplog.txt 2>>/home/pi/balloonviduplog.txt

balloonPicsOnly-down.py - 
Intended for the payload's downward-facing camera. 
Takes a jpeg picture with RAW Bayer metadata roughly every 20 seconds for 5 hours.
Saves files in /home/pi/Launch3PicsOnlydown/Folder### . 
Crontab: @reboot python -u /home/pi/FINALCODE/balloonPicsOnly-down.py >>/home/pi/balloonpicdownlog.txt 2>>/home/pi/balloonpicdownlog.txt 

balloonVidandPic-sponsor.py - 
Intended for payload's side-facing camera (sponsor). 
Takes 10 min videos + 1 jpeg picture (with RAW Bayer metadata) for 5 hours. 
Saves files in /home/pi/Launch3VidandPicsponsor/Folder### . 
Crontab: @reboot python -u /home/pi/FINALCODE/balloonVidandPic-sponsor.py >>/home/pi/balloonvidpicsponsorlog.txt 2>>/home/pi/balloonvidpicsponsorlog.txt

balloonPicsandVid-side.py - 
Intended for payload's side facing camera (not sponsor side). 
Takes a jpeg picture with RAW Bayer metadata roughly every 20 seconds for 20 min, then takes a 5 min video. Runs for 5 hours total. 
Saves files in /home/pi/Launch3PicsandVidside/Folder### . 
Crontab: @reboot python -u /home/pi/FINALCODE/balloonPicsandVid-side.py >>/home/pi/balloonpicsvidsidelog.txt 2>>/home/pi/balloonpicsvidsidelog.txt
