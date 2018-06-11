#!/usr/bin/env python

import picamera
import time
import os
import datetime

# AstroHackers Pi Camera (Pictures Only)
# takes a jpeg picture with RAW Bayer metadata roughly every 20 seconds for 5 hours
# saves files in /home/pi/Launch3PicsOnlydown/Folder###
# prints statements that can be redirected to form a log
# intended for the payload's downward-facing camera
# each picture is roughly 13.4MB (5 hours = roughly 12GB)

print ('BOOTED UP')

path_to_dir = '/home/pi/Launch3PicsOnlydown'

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


# loop for taking pictures 
# 3 pics/min = 180 pics/hour = 900 pics/5 hours
# quality parameter not set and is thus the default (85)
for j in range(1, 901):

   i = str(j).rjust(4, '0')

   with picamera.PiCamera() as camera:
	camera.resolution = (3280, 2462)
	camera.awb_mode = 'auto'
   	time.sleep(2) #camera warm-up time
   	camera.capture('PIC-%s.jpg' % i, format='jpeg', bayer=True)
   	print ('Captured PIC-%s.jpg' % i)
   time.sleep(18)
