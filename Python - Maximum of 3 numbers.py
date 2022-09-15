#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Maximum of 3 number
x = int(input('Enter value of X : '))
y = int(input('Enter value of y : '))
z = int(input('Enter value of Z : '))
if x>y:
    if y>z:
        print ('x is biggest')
    else:
        if z>x:
            print ('z is biggest')
        else:
            print ('x is biggest')
else:
    if x>z:
        print ('y is biggest' )
    else:
        if y>z:
            print ('y is biggest')
        else:
            print ('z is biggest')

