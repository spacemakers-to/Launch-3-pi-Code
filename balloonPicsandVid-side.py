#!/usr/bin/env python

import picamera
import time
import os
import datetime

# AstroHackers Pi Camera (Pictures and Videos)
# takes a jpeg picture with RAW Bayer metadata roughly every 20 seconds for 20 min, then takes a 5 min video. Runs for 5 hours total
# saves files in /home/pi/Launch3PicsandVidside/Folder###
# prints statements that can be redirected to form a log
# intended for payload's side facing camera (not sponsor side)

print ('BOOTED UP')

path_to_dir = '/home/pi/Launch3PicsandVidside'

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


# loop for taking pictures + videos, takes 60 pictures then 1 video
# quality for pictures captured is default (85)
# pictures numbered from 1 to 720, videos numbered in multiples of 60
# video 60 captured right after pic 60, video 120 captured right after pic 120, etc
for pic_numb in range(1, 721):

   i = str(pic_numb).rjust(4, '0')

   with picamera.PiCamera() as camera:
      camera.resolution = (3280, 2462)
      camera.awb_mode = 'auto'
      time.sleep(2) #camera warm-up time
      camera.capture ('PIC-%s.jpg' % i, format='jpeg', bayer=True)
      print ('Captured PIC-%s.jpg' % i)
   time.sleep(18)

   if (pic_numb % 60) == 0:
      with picamera.PiCamera() as camera:
         camera.resolution = (1640, 1232)
         camera.framerate = 30
         camera.awb_mode = 'auto'
         time.sleep(2) #camera warm-up time
         camera.start_recording('Video-%s.h264' % i, format='h264', quality=23)
         camera.wait_recording(300)
         camera.stop_recording()
         print ('Captured Video-%s.h264' % i)
