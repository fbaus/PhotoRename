__author__ = 'francesco'

import os

def thumbn()
for filename in os.listdir( os.getcwd() ):
    ##DOES THIS WORK FOR ALL TYPES OF IMGS???
    a = sm.imread( filename )    #import image as array
    a = a[:,:,1]    #consider on one colour layer
    a = sm.imresize(a, (c,c))   #resize image
#return

#WHEN SEARCHING FOR DUPLICATES IT IS CONVENIENT TO DELETE SPOTTED ELEMENTS, this can be tricky while looping

def likeliness( a, b, c):

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
