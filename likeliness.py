__author__ = 'francesco'

import os
import scipy.misc as sm
import numpy as np
import tkinter

def thumbn(c)    #CREATES SQUARE THUMBNAIL COPIES (size c-by-c) of the IMAGES
l = {}
for filename in os.listdir( os.getcwd() ):              #for all files into folder
    a = sm.imread( filename )                           ###import image as array <<DOES IT WORK THE SAME FOR DIFFERENT FORMATS?
    a = a[:,:,1]                                        ###consider ony one colour layer <<DOES IT WORK THE SAME FOR DIFFERENT FORMATS?
    a = sm.imresize(a, (c,c))                           #resize image
    name, extension = os.path.splitext( filename )      #extract name and file extension
    np.save(name, a)                                    #save thumbnail as np array as a temporary file
    l[ name ] = 'n'                                     #add the name to the blacklist but as non-duplicate
    

d=[0]                                                   #list of duplicated groups
#IT WILL BE A LIST OF LISTS [[.,.],[.,.,.],[.,.]] WHERE EACH SUBLIST CONTAINS GROUPS OF DUPLICATES
b=0                                                     #counter for how many i have duplicates i.e. how many groups in the list
for i in l.keys():                                      #loop on every file in the folder
    if l[ i ] == 'n':                                   #a picture can compare only in one duplicates group
        c=0                                             #counter for how many duplicates for i i.e. how many pics in one group
        for j in l.keys():                              #loop on every file in the folder
            if i!=j & l[j]=='n':                        #if i and j are different
                #compare i and j DEVELOP METHOD
                if #compare = match:                    
                    l[ j ] = 'y'                        #
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
    

    
if __name__ == '__main__':
    main()
