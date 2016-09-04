__author__ = 'francesco'



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