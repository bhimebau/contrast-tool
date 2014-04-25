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
        print "array shape =", self.image_arr.shape
        self.image_arrg = self.image_arr.astype(int)
        self.image_greyscale = pygame.surfarray.make_surface(self.image_arrg)
        self.mask = pygame.mask.from_threshold(self.image_greyscale,(50,50,50),(50,50,50))
        self.msize = self.mask.get_size()
#        self.gmask = []
        for i in range(msize[0]):
#            gcol = []
            for j in range(msize[1]):
               if self.mask.get_at((i,j)):
                   self.image_greyscale.set_at((i,j),(175,175,175))
               else:
                   self.image_greyscale.set_at((i,j),(255,255,255))
#                if self.mask.get_at((i,j)):
#                     gcol.append([True,True,True])
#                 else:
#                     gcol.append([False,False,False])
#            self.gmask.append(gcol)
 #       print self.gmask.shape
 #       print "True at %d %d\n"%(i,j)
            
#        self.greyscale_masked = numpy.ma.array([[[avg,avg,avg] for avg in col] for col in self.image_avgs],mask=self.gmask,fill_value=125)
#        self.image_greyscale_masked_int = self.greyscale_masked.astype(int)
#        self.image_greyscale = pygame.surfarray.make_surface(self.image_greyscale_masked_int)
            
#        self.reference_image_array = self.threshold_image(self.image_avgs)

#        self.image_array = numpy.array([[[avg,avg,avg] for avg in col] for col in self.image_avgs])
#        self.image_arrg = self.image_array.astype(int)
#        self.image_greyscale =  pygame.surfarray.make_surface(self.image_arrg)
#        self.image_greyscale =  pygame.surfarray.make_surface(self.reference_image_array)
 #       for pixel in self.image_arrg:
 #           print pixel
        
        self.center_image = (self.image_greyscale.get_rect().width/4,self.image_greyscale.get_rect().height/4)
        
#         self.gsi = pygame.surfarray.array3d(self.image_greyscale)
  #       self.gsa = numpy.array(self.gsi)

#     def threshold_image (self):
#         column_list = []
#        for col in self.image_avgs:
            
#             for avg in col:
#                if avg > 122:
#                     avg = 255
#                else:
#                     avg = 0 
#                 pixel = numpy.array([avg,avg,avg])
#            column_array = []
#            for avg in col:
#                if avg > 125:
#                    avg = 255
#                else:
#                    avg = 0
#                    column_array.append([avg,avg,avg])
#                    image_array.append(column_array)
#                return image_array


    def write_greyscale (self,value):
        for i in range(self.msize[0]):
            for j in range(self.msize[1]):
               if self.mask.get_at((i,j)):
                   self.image_greyscale.set_at((i,j),(value,value,value))
               else:
                   self.image_greyscale.set_at((i,j),(255,255,255))


 #        for 
        pass
        #       self.gsa[:,:,:] = value
 #       return pygame.surfarray.make_surface(self.gsa)

#k        return self.mask.fill((value,value,value))
        #return self.mask.fill()
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
    background=pygame.Surface((window.get_rect().width, window.get_rect().height))
    background.fill((255, 255, 255))

    gi = GreyImage(imagefile="large-E.jpg", gammafile="gamma") 
  
    # Set the location
    center=(window.get_rect().width/2,window.get_rect().height/2)
    image_loc = (center[0]-gi.center_image[0],center[1]-gi.center_image[1])
    print "Initial location",center,gi.center_image,image_loc    

    # Write the image
#    window.blit(gi.write_greyscale(75), image_target)
    
#    gi.threshold_image()
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
            window.blit(gi.image_greyscale, image_loc)
            
#           gisize = gi.mask.get_size()
#           print gisize
#           girect = pygame.Rect((0,0),gisize)
#           print girect
#           tmp = gi.image_greyscale.copy()
#           tmp.blit(gi.mask,girect.topleft,girect,special_flags=pygame.BLEND_RGBA_MULT)
#            window.blit(gi.write_greyscale(75), image_loc)
#           window.blit(tmp,image_loc,window.get_rect().clip(girect))
#            pygame.time.delay(20)
            pygame.display.update()
   
#     gi.write_greyscale(30)


