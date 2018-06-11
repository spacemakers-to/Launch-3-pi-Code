#!/usr/bin/env python

import picamera
import time
import os
import datetime

# AstroHackers Pi Camera (Videos Only)
# takes a continous video for 5 hours, breaks it up into 10 min videos
# saves files in /home/pi/Launch3VidsOnlyup/Folder###
# prints statements that can be redirected to form a log
# intended for payload's upward-facing camera

# when called the first time (i.e. Launch3VidsOnlyup does not exist), it sleeps for 1 hour before continuing
# IMPORTANT: in order to have the 1 hour delay, make sure there is no Launch3VidsOnlyup directory in the /home/pi directory

print ('BOOTED UP')

path_to_dir = '/home/pi/Launch3VidsOnlyup'

if not os.path.isdir(path_to_dir):
    os.mkdir(path_to_dir)
    time.sleep(3600) #pauses for 1 hour before continuing

folder_count = len(next(os.walk(path_to_dir))[1])

path_to_subdir = path_to_dir + '/Folder' + str(folder_count).rjust(3, '0') + '_' + str(datetime.datetime.now())[:-7].replace(" ", "_").replace(":", "-")

if not os.path.isdir(path_to_subdir):
    os.mkdir(path_to_subdir)

os.chdir(path_to_subdir)


print ('Starting to use camera')
print ('Files saved on %s' % str(datetime.datetime.now())[:-7])
print ('Files saved in Folder%s' % str(folder_count).rjust(3, '0'))


# sleep time is in sec so need to record 6 files per hour
# 30 files of 10 min (600sec) each. 5 hrs total. Approx 1.5GB used per video file (bright video with movement)

# Full HD video
with picamera.PiCamera() as camera:
   camera.resolution = (1640, 1232)
   camera.framerate = 30
   camera.awb_mode = 'auto'
   time.sleep(2) #camera warm-up time
   for filename in camera.record_sequence(
       ('Video-%03d.h264' % i for i in range(1, 31)), format='h264', quality=23):
       camera.wait_recording(600)
       print ('Captured ' + filename)
