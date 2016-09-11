__author__ = 'francesco'

import os
import scipy.misc as sm
import numpy as np

def thumbn()
l = {}
for filename in os.listdir( os.getcwd() ):
    ##DOES THIS WORK FOR ALL TYPES OF IMGS???
    a = sm.imread( filename )    #import image as array
    a = a[:,:,1]    #consider on one colour layer
    a = sm.imresize(a, (c,c))   #resize image
    name, extension = os.path.splitext( filename )
    sm.imsave( name+"_TMB"+extension, a) #SAVE THUMBNAILS IMAGE SHOULD NOT OVERWRITE IMAGES
    np.save(filename, a) #THUMBNAILS SHOULD NOT OVERWRITE IMAGES
    l[ filename ] = 'n' 
#WHEN SEARCHING FOR DUPLICATES IT IS CONVENIENT TO DELETE SPOTTED ELEMENTS, this can be tricky while looping

for filename in os.listdir( os.getcwd() ): #RUN on DICTIONARY LIST not all files!
    if 'TMB' not in filename:
        if l[filename]==n


        #COMPARE TMBs
        #if EQUAL



def likeliness( a, b):

#IMPORT and RESIZE IMG A
a = sm.imread(a)    #import image as array
a = a[:,:,1]    #consider on one colour layer
a = sm.imresize(a, (c,c))   #resize image

#IMPORT and RESIZE IMG B
b = sm.imread(b)    #import image as array
b = b[:,:,1]    #consider on one colour layer
b = sm.imresize(b, (c,c))   #resize image

c = abs(a - b)

t=10

r=0

for i in range(0,z):
    for j in range(0,z):
        if (c[i,j]<128):
            r=r+c[i,j]
        else if (c[i,j]>128):
           r=r+255-c[i,j]

if (r/z<t): M=True
else: M=False
