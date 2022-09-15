#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Converting km to mile
# Getting kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))


# In[3]:


# Converting mile to km
# Getting mile input from the user
mile = float(input("Enter value in miles: "))

# conversion factor
conv_fac = 1/0.621371

# calculate kilometers
kilometers = miles * conv_fac
print('%0.2f miles is equal to %0.2f kilometers' %(miles,kilometers))


# In[ ]:




