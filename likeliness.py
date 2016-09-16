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
    np.save(name, a) #THUMBNAILS SHOULD NOT OVERWRITE IMAGES
    l[ name ] = 'n' 
    
    
#WHEN SEARCHING FOR DUPLICATES IT IS CONVENIENT TO DELETE SPOTTED ELEMENTS, this can be tricky while looping
d=[0] #list of duplicates IT WILL BE A LIST OF LISTS [[],[],[]] WHERE EACH SUBLIST CONTAINS DUPLICATES GROUPS
b=0 #counter for how many i have duplicates
for i in l.keys():
    if l[ i ] == 'n': #a picture can compare only in one duplicates group
        c=0 #counter for how many duplicates for i
        for j in l.keys():
            if i!=j & l[j]=='n':
                #compare i and j DEVELOP METHOD
                if #compare = match:
                    l[ j ] = 'y'
                    if c=0
                        l[ i ] = 'y'
                        d[b]=[i,j]
                    else
                        d[b].append[j]
                    c=c+1
                    b=b+1


#ADD TKINTER DISPLAY of ELEMENT of d LIST of LISTS

for filename in os.listdir( os.getcwd() ): #RUN on DICTIONARY LIST not all files!
    if filename.endswith(".npy") & l[filename]==n:
    for    


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
