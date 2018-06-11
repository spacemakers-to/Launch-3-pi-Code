# Launch-3-pi-Code

Four different sets of code.

balloonVidsOnly-up.py
Intended for the payload's upward-facing camera
takes a continous video for 5 hours, breaks it up into 10 min videos
saves files in /home/pi/Launch3VidsOnlyup/Folder###
when called the "first time" (i.e. Launch3VidsOnlyup does not exist), it sleeps for 1 hour before continuing

balloonPicsOnly-down.py
intended for the payload's downward-facing camera
takes a jpeg picture with RAW Bayer metadata roughly every 20 seconds for 5 hours
saves files in /home/pi/Launch3PicsOnlydown/Folder###

balloonVidandPic-sponsor.py
intended for payload's side-facing camera (sponsor)
takes 10 min videos + 1 jpeg picture (with RAW Bayer metadata) for 5 hours
saves files in /home/pi/Launch3VidandPicsponsor/Folder###

balloonPicsandVid-side.py
intended for payload's side facing camera (not sponsor side)
takes a jpeg picture with RAW Bayer metadata roughly every 20 seconds for 20 min, then takes a 5 min video. Runs for 5 hours total
saves files in /home/pi/Launch3PicsandVidside/Folder###
