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

# try:
#    gf = open(gammafile)
# except IOError:
#    print 'Error: gammafile not found:', gammafile
#    sys.exit()
# 
# try:
#    with open(imagefile): pass
# except IOError:
#    print 'Error: imagefile not found:', imagefile
#    sys.exit()

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

# image=pygame.image.load(imagefile)
# image=image.convert()

# image_arr = pygame.surfarray.array3d(image)
# image_avgs = [[(r*0.298 + g*0.587 + b*0.114) for (r,g,b) in col] for col in image_arr]    
# image_arr = numpy.array([[[avg,avg,avg] for avg in col] for col in image_avgs])
# image_arrg = image_arr.astype(int)
# image_greyscale =  pygame.surfarray.make_surface(image_arrg)

#black_counter = 0
# white_counter = 0

# for col in image_avgs:
#     print col 
#     print "newline\n"
#     for avg in col:
#         if avg > 125: 
#             print "White = %f"%(avg)
#             white_counter = white_counter + 1
#         else:
#             print "Black = %f"%(avg)
#             black_counter = black_counter + 1
        # print "Here is the avg", avg
# print black_counter, white_counter, black_counter + white_counter, 150*150 

center_image = (gi.image_greyscale.get_rect().width/4,gi.image_greyscale.get_rect().height/4)
image_loc = (center[0]-gi.center_image[0],center[1]-gi.center_image[1])
contrast_value=0
mm=contrast_value/255;
#y=1.6973*(mm**3) - 1.7375*(mm**2) +1.0494*mm - 0.0286;
y=1.6973*(mm**3) - 1.7375*(mm**2) +1.0494*mm;
contrast_value= contrast_value+ float(255*y);

# image_arrg = image_arr.astype(int)
# image_grey_adjusted = pygame.surfarray.make_surface(image_arrg)    
# imagegrey_array_float = numpy.array([[[avg,avg,avg] for avg in col] for col in avgs])
# imagegrey_array_int = arr.astype(int)
# imagegrey = pygame.surfarray.make_surface(imagegrey_array_int)
# print image.get_rect().width,image.get_rect().height
# print "Pixel Center", imagegrey.get_at((75,75))
# print "TL", imagegrey.get_at((0,0))
# print "TR", imagegrey.get_at((149,0))
# print "BL", imagegrey.get_at((0,149))
# print "BR", imagegrey.get_at((149,149))
# print "Pixel Center", imagegrey.get_at((75,75))
# print "Pixel Center", imagegrey.get_at((75,75))
# print "Pixel Top Left", imagegrey.get_at((0,0)
# print "Pixel Top Right", imagegrey.get_at((image.get_rect().width/2,0))
# print "Pixel Bottom Right", imagegrey.get_at((image.get_rect().width/2,image.get_rect().height/2))
# print "Pixel Bottom Left", imagegrey.get_at((0,image.get_rect().height/2))
image_loc = (center[0]-gi.center_image[0],center[1]-gi.center_image[1])
while True:
    # Manage quit and window resize events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print "Quit Event"
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print "key event", event.key
            out = "%d            %d\n"%(pygame.time.get_ticks(),event.key)
            df.write(out)
            if event.key == pygame.K_q:
                 sys.exit()
        if event.type == pygame.VIDEORESIZE:
            size = event.size
            center = (size[0]/2,size[1]/2)
            image_loc = (center[0]-gi.center_image[0],center[1]-gi.center_image[1])
#             print center,center_image,image_loc

    # Grab the change in the y position of the mouse, apply this to the current contrast value.
    mdelta = pygame.mouse.get_rel()
    #print (mdelta[0])
    #contrast_value  =math.log10(contrast_value);
    #print (contrast_value);
    m=float(-mdelta[0]);
    #print (m);
    #mm=(contrast_value+m)/255;
    contrast_value -= m/2;
    #print (contrast_value);
    #contrast_value  =math.pow(10, contrast_value);
    #print (contrast_value);

    # Clamp the value to put it on the alpha channel scale
    if contrast_value < 0:
        contrast_value = 0;
    elif contrast_value > 255:
        contrast_value = 255;

    if mdelta > 0: 
        outstr = "%d %d\n"%(pygame.time.get_ticks(),contrast_value)
        df.write(outstr)

    # write to the alpha channel
#     image.set_alpha(contrast_value)
    gi.write_greyscale(contrast_value)
    # sent the new surface to the screen
    window.fill((255, 255, 255))
    window.blit(background, background.get_rect())
    window.blit(gi.image_greyscale, image_loc)
    pygame.time.delay(20)
    pygame.display.update()
    print (contrast_value);

