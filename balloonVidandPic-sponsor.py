#!/usr/bin/env python

import picamera
import time
import os
import datetime

# AstroHackers Pi Camera (Video and Picture)
# takes 10 min videos + 1 jpeg picture (with RAW Bayer metadata) for 5 hours
# saves files in /home/pi/Launch3VidandPicsponsor/Folder###
# prints statements that can be redirected to form a log
# intended for payload's side-facing camera (sponsor)

print ('BOOTED UP')

path_to_dir = '/home/pi/Launch3VidandPicsponsor'

if not os.path.isdir(path_to_dir):
    os.mkdir(path_to_dir)

folder_count = len(next(os.walk(path_to_dir))[1])

path_to_subdir = path_to_dir + '/Folder' + str(folder_count).rjust(3, '0') + '_' + str(datetime.datetime.now())[:-7].replace(" ", "_").replace(":", "-")

if not os.path.isdir(path_to_subdir):
    os.mkdir(path_to_subdir)

os.chdir(path_to_subdir)


print ('Starting to use camera')
print ('Files saved on %s' % str(datetime.datetime.now())[:-7])
print ('Files saved in Folder%s' % str(folder_count).rjust(3, '0'))


# sleep time is in sec so need to record 6 files per hour
# 30 files of 10 min (600sec) each. 5 hrs total. Approx 1.5GB used per video file. Approx 11MB per picture file
# some video will be lost due to transition time
# quality parameter for pics not set, thus is default (85)

# Full HD video
for j in range(1, 31):

   i = str(j).rjust(3, '0')

   with picamera.PiCamera() as camera:
      camera.awb_mode = 'auto'
      camera.resolution = (1640, 1232)
      camera.framerate = 30
      time.sleep(2) #camera warm-up time
      camera.start_recording('Video-%s.h264' % i, format='h264', quality=23)
      camera.wait_recording(600)
      camera.stop_recording()
      print ('Captured Video-%s.h264' % i)

      camera.resolution = (3280, 2462)
      time.sleep(2) #camera warm-up time
      camera.capture('PIC-%s.jpg' % i, format='jpeg', bayer=True)
      print ('Captured PIC-%s.jpg' % i)
