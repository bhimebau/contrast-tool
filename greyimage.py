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
import math
import numpy 
import csv
import bisect

class GreyImage():
    
    def __init__(self, imagefile, gammafile):
        self.gammafile = gammafile
        print self.gammafile
        try:
            self.gf = open(gammafile)
        except IOError:
            print 'Error: gammafile not found:', gammafile
            sys.exit()
        self.imagefile = imagefile
        try:
            with open(imagefile): pass
        except IOError:
            print 'Error: imagefile not found:', imagefile
            sys.exit()

        print "about to process csv"
        with open(self.gammafile, 'rU') as f:
            gcf = csv.reader(f)
            self.gammalist = []
            for row in gcf:
                self.gammalist.append((row[0],row[1]))

        self.raw_image_surface = pygame.image.load(imagefile)
        self.raw_image_surface = self.raw_image_surface.convert()
        self.raw_image_array = pygame.surfarray.array3d(self.raw_image_surface)
        self.image_avgs = [[(r*0.298 + g*0.587 + b*0.114) for (r,g,b) in col] for col in self.raw_image_array]    
        self.image_arr = numpy.array([[[avg,avg,avg] for avg in col] for col in self.image_avgs])
        self.image_arrg = self.image_arr.astype(int)
        self.image_greyscale = pygame.surfarray.make_surface(self.image_arrg)
        self.mask = pygame.mask.from_threshold(self.image_greyscale,(50,50,50),(50,50,50))
        self.msize = self.mask.get_size()
        for i in range(self.msize[0]):
            for j in range(self.msize[1]):
               if self.mask.get_at((i,j)):
                   self.image_greyscale.set_at((i,j),(0,0,0))
               else:
                   self.image_greyscale.set_at((i,j),(255,255,255))
        self.center_image = (self.image_greyscale.get_rect().width/4,self.image_greyscale.get_rect().height/4)

    def write_greyscale (self,value):
        cvalue = self.correction_lookup(value);
        for i in range(self.msize[0]):
            for j in range(self.msize[1]):
               if self.mask.get_at((i,j)):
                   self.image_greyscale.set_at((i,j),(cvalue,cvalue,cvalue))
               else:
                   self.image_greyscale.set_at((i,j),(255,255,255))

    def correction_lookup(self,value):
        for i in range(len(self.gammalist)):
            x0 = float(self.gammalist[i][0])
            y0 = float(self.gammalist[i][1])
            if (x0 == value):
                return (int(y0))
            elif (x0 > value):
                if (i == 0):
                    return (int(y0))
                else:
                    x1 = float(self.gammalist[i-1][0])
                    y1 = float(self.gammalist[i-1][1])
                    interp_val = y0 + (((y1-y0)/(x1-x0)) * (value-x0))
                    return int(interp_val)

             
if __name__ == '__main__':
    pygame.init()
    window=pygame.display.set_mode((0, 0),pygame.RESIZABLE)
    pygame.display.set_caption("Contrast Tool")
    background=pygame.Surface((window.get_rect().width, window.get_rect().height))
    background.fill((255, 255, 255))

    gi = GreyImage(imagefile="large-E.jpg", gammafile="gamma") 
  
    center=(window.get_rect().width/2,window.get_rect().height/2)
    image_loc = (center[0]-gi.center_image[0],center[1]-gi.center_image[1])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print "Quit Event"
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print "key event", event.key
                out = "%d            %d\n"%(pygame.time.get_ticks(),event.key)
                if event.key == pygame.K_q:
                    sys.exit()
            if event.type == pygame.VIDEORESIZE:
                size = event.size
                center = (size[0]/2,size[1]/2)
                image_loc = (center[0]-gi.center_image[0],center[1]-gi.center_image[1])
                print center,gi.center_image,image_loc
            window.fill((255, 255, 255))
            window.blit(background, background.get_rect())
            gi.write_greyscale(200)
            window.blit(gi.image_greyscale, image_loc)
            pygame.display.update()
            
   


