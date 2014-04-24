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
        self.image_arr = numpy.array([[[avg,avg,avg] for avg in col] for col in self.image_avgs])
        self.image_arrg = self.image_arr.astype(int)
        self.image_greyscale = pygame.surfarray.make_surface(self.image_arrg)
        self.mask = pygame.mask.from_threshold(self.image_greyscale,(50,50,50),(50,50,50))
#        self.reference_image_array = self.threshold_image(self.image_avgs)

#        self.image_array = numpy.array([[[avg,avg,avg] for avg in col] for col in self.image_avgs])
#        self.image_arrg = self.image_array.astype(int)
#        self.image_greyscale =  pygame.surfarray.make_surface(self.image_arrg)
#        self.image_greyscale =  pygame.surfarray.make_surface(self.reference_image_array)
 #       for pixel in self.image_arrg:
 #           print pixel

        
        print self.mask
        self.center_image = (self.image_greyscale.get_rect().width/4,self.image_greyscale.get_rect().height/4)
        self.image_loc = (center[0]-center_image[0],center[1]-center_image[1])

#     def threshold_image (self, imavgs):
#         image_array = []
#         for col in imavgs:
#             column_array = []
#             for avg in col:
#                 if avg > 125:
#                     avg = 255
#                 else:
#                     avg = 0
#                 column_array.append([avg,avg,avg])
#             image_array.append(column_array)
#         return image_array


    def write_greyscale (self,value):
#k        return self.mask.fill((value,value,value))
        return self.mask.fill()
#         if (value > 254):
#            value = 254
#         if (value < 0):
#            value = 0
# 
#         white_counter = 0
#         black_counter = 0
#         image_array = []
#         column_array = []
#         for col in self.image_avgs:
#             for avg in col:
#                 print avg
#                column_array.append([value
# 
#             print col 
#             print "newline\n"
#             for avg in col:
#                 if avg > 125: 
#                     print "White = %f"%(avg)
#                     white_counter = white_counter + 1
#                 else:
#                    print "Black = %f"%(avg)
#                     black_counter = black_counter + 1
#                 print "Here is the avg", avg
#         print black_counter, white_counter, black_counter + white_counter, 150*150 
    


if __name__ == '__main__':
    pygame.init()
    window=pygame.display.set_mode((0, 0),pygame.RESIZABLE)
    pygame.display.set_caption("Contrast Tool")
    center=(window.get_rect().width/2,window.get_rect().height/2)
    background=pygame.Surface((window.get_rect().width, window.get_rect().height))
    background.fill((255, 255, 255))

    gi = GreyImage(imagefile="large-E.jpg", gammafile="gamma") 
    
    window.fill((255, 255, 255))
    window.blit(background, background.get_rect())
    window.blit(gi.write_greyscale(75), gi.image_loc)
    

#     gi.write_greyscale(30)


