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

class GreyImage():
    
    def __init__(self, imagefile = "imagefile", gammafile = "gamma"):
        self.gammafile = gammafile
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

        self.raw_image_surface = pygame.image.load(imagefile)
        self.raw_image_surface = self.raw_image_surface.convert()
        self.raw_image_array = pygame.surfarray.array3d(self.raw_image_surface)
        self.image_avgs = [[(r*0.298 + g*0.587 + b*0.114) for (r,g,b) in col] for col in self.raw_image_array]    
        self.image_array = numpy.array([[[avg,avg,avg] for avg in col] for col in self.image_avgs])
        self.image_arrg = self.image_array.astype(int)
        self.image_greyscale =  pygame.surfarray.make_surface(self.image_arrg)

    def change_greyscale (self,value):
        

        


if __name__ == '__main__':
    sm = SyncroMesh(height=8, xdim=10, ydim=10, zdim=1) 
    sm.change_group_resistance("G-7-3-0-G-7-4-0", '45k')
    sm.report_devices()

