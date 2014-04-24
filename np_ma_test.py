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
import numpy as np 

if __name__ == '__main__':
#     x = np.ma.array([1,2,3,4,5], mask=[0,0,1,0,1], fill_value=-999)
#     print x.filled()
     
#    init_data = np.arange(10)
#    my_array = np.array([[[200,200,200],[32,200,180],[34,200,200]],[[200,200,200],[32,200,180],[34,200,200]],[[200,200,200],[32,200,180],[34,200,200]]])
#    data = np.ma.masked_array(my_array, mask=(init_data>100), fill_value=255)
  #  data = np.ma.masked_array(init_data, mask=(init_data >= 6), fill_value=1000)
#    print data.filled() 

    ydim = 150
    xdim = 150 
    (ydim,xdim,dummy) = img.shape
# make an open grid of x,y
    y,x = np.ogrid[0:ydim, 0:xdim, ]
    y -= ydim/2                 # centered at the origin
    x -= xdim/2
# now make a mask
    mask = x**2+y**2 <= radius**2 # start with 2d
    img[mask,:] = (255,255,255)
