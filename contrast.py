#!/usr/bin/env python

__author__ = "Bryce Himebaugh"
__copyright__ = "Copyright 2013 Bryce Himebaugh"
__credits__ = ["Bryce Himebaugh, Jun Zhang"]
__license__ = "GPL V3"
__version__ = "0.001"
__maintainer__ = "Bryce Himebaugh"
__email__ = "bhimebau@gmail.com"
__status__ = "prototype"

import pygame, sys, getopt, time

imagefile = ''
prefix = 'cdata'
try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["image=","prefix="])
except getopt.GetoptError:
    print 'contrast.py <target image file> -p <output_datafile_prefix>'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print 'contrast.py -i <target image file> -p <output_datafile_prefix>'
        sys.exit()
    elif opt in ("-i", "--image"):
        imagefile = arg
    elif opt in ("-p", "--prefix"):
        datafile = arg
try:
   with open(imagefile): pass
except IOError:
   print 'Error: imagefile not found:', imagefile
   sys.exit()
timestr = time.strftime("%m%d%Y-%H%M%S")
datafile = prefix + "-" + timestr

df=open(datafile, 'w')
pygame.init()
window=pygame.display.set_mode((0, 0),pygame.RESIZABLE)
pygame.display.set_caption("Contrast Tool")
center=(window.get_rect().width/2,window.get_rect().height/2)
background=pygame.Surface((window.get_rect().width, window.get_rect().height))
background.fill((0, 0, 0))
image=pygame.image.load(imagefile)
image=image.convert()
center_image = (image.get_rect().width/2,image.get_rect().height/2)
image_loc = (center[0]-center_image[1],center[1]-center_image[1])
contrast_value=0

while True:
    # Manage quit and window resize events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print "Quit Event"
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print "key event", event.key
            if event.key == pygame.K_q:
                sys.exit()
        if event.type == pygame.VIDEORESIZE:
            size = event.size
            center = (size[0]/2,size[1]/2)
            image_loc = (center[0]-center_image[1],center[1]-center_image[1])
            print center,center_image,image_loc

    # Grab the change in the y position of the mouse, apply this to the current contrast value.
    mdelta = pygame.mouse.get_rel()
    contrast_value -= mdelta[1]/2;

    # Clamp the value to put it on the alpha channel scale
    if contrast_value < 0:
        contrast_value = 0;
    elif contrast_value > 255:
        contrast_value = 255;

    if mdelta > 0:
        outstr = "%d %d\n"%(pygame.time.get_ticks(),contrast_value)
        df.write(outstr)

    # write to the alpha channel
    image.set_alpha(contrast_value)

    # sent the new surface to the screen
    window.fill((255, 255, 255))
    window.blit(background, background.get_rect())
    window.blit(image, image_loc)
    pygame.time.delay(20)
    pygame.display.update()


