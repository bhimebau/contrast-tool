#!/usr/bin/env python

__author__ = "Bryce Himebaugh"
__copyright__ = "Copyright 2013 Bryce Himebaugh"
__credits__ = ["Bryce Himebaugh, Jun Zhang"]
__license__ = "GPL V3"
__version__ = "0.002"
__maintainer__ = "Bryce Himebaugh"
__email__ = "bhimebau@gmail.com"
__status__ = "prototype"

import pygame, sys, getopt, time
import math
import numpy 
import greyimage

imagefile = ''
prefix = 'cdata'
try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:o:p:i:g:",["image=","prefix="])
except getopt.GetoptError:
    print opts
    print args
    print 'contrast.py <target image file> -p <output_datafile_prefix>'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print 'contrast.py -i <target image file> -p <output datafile prefix> -g <gamma correction file>'
        sys.exit()
    elif opt in ("-i", "--image"):
        imagefile = arg
    elif opt in ("-p", "--prefix"):
        datafile = arg
    elif opt in ("-g", "--gamma"):
        gammafile = arg

timestr = time.strftime("%m%d%Y-%H%M%S")
datafile = prefix + "-" + timestr

df=open(datafile, 'w')
pygame.init()
window=pygame.display.set_mode((0, 0),pygame.RESIZABLE)
pygame.display.set_caption("Contrast Tool")
center=(window.get_rect().width/2,window.get_rect().height/2)
background=pygame.Surface((window.get_rect().width, window.get_rect().height))
background.fill((255, 255, 255))
gi = greyimage.GreyImage(imagefile="large-E.jpg", gammafile="gamma")
center_image = (gi.image_greyscale.get_rect().width/4,gi.image_greyscale.get_rect().height/4)
image_loc = (center[0]-gi.center_image[0],center[1]-gi.center_image[1])
contrast_val=0
mm=contrast_val/255;
y=1.6973*(mm**3) - 1.7375*(mm**2) +1.0494*mm;
contrast_val= contrast_val+ float(255*y);
baseline = contrast_val

image_loc = (center[0]-gi.center_image[0],center[1]-gi.center_image[1])
while True:
    # Manage quit and window resize events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print "Quit Event"
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
#             print "key event", event.key
            out = "%d            %d\n"%(pygame.time.get_ticks(),event.key)
            df.write(out)
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_b:
                baseline = contrast_val
                out = "%d            %d baseline %d\n"%(pygame.time.get_ticks(),event.key,baseline)
                df.write(out)
            if event.key == pygame.K_r:
                contrast_val = baseline
                out = "%d            %d revert %d\n"%(pygame.time.get_ticks(),event.key,baseline)
                df.write(out)
            
        if event.type == pygame.VIDEORESIZE:
            size = event.size
            center = (size[0]/2,size[1]/2)
            image_loc = (center[0]-gi.center_image[0],center[1]-gi.center_image[1])

    mdelta = pygame.mouse.get_rel()
    m=float(-mdelta[0]);
    contrast_val -= m/2;

    # Clamp the value to put it on the alpha channel scale
    if contrast_val < 0:
        contrast_val = 0;
    elif contrast_val > 255:
        contrast_val = 255;

    if mdelta > 0: 
        outstr = "%d %d\n"%(pygame.time.get_ticks(),contrast_val)
        df.write(outstr)

    gi.write_greyscale(contrast_val)
    # sent the new surface to the screen
    window.fill((255, 255, 255))
    window.blit(background, background.get_rect())
    window.blit(gi.image_greyscale, image_loc)
    pygame.time.delay(20)
    pygame.display.update()
#     print (contrast_val);

