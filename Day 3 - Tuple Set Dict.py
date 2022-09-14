#!/usr/bin/env python
# coding: utf-8

# # Day 3 - Tuple Set Dict

# In[4]:


t = (1,2,3,4,5)


# In[5]:


type(t)


# In[6]:


t1 = ("ilaya", 3.14, 248, 5+4j, True)


# In[7]:


l = ["ilaya", 3.14, 248, 5+4j, True]


# In[8]:


type(t1)


# In[9]:


type(l)


# In[10]:


t1[0:2]


# In[11]:


l[0:2]


# In[13]:


t1[::-1]


# In[14]:


l[::-1]


# In[15]:


l


# In[16]:


l[0]


# In[17]:


l[0]="perumal"


# In[18]:


l


# In[19]:


t1


# In[20]:


t1[0] = "Perumal"


# In[21]:


t2 = (23,34,45,67,78)


# In[22]:


t1+t2


# In[25]:


l1 = [4,5,6,7]


# In[26]:


l+l1


# In[27]:


t1*2


# In[28]:


t1


# In[29]:


t1.count("ilaya")


# In[30]:


t1.index("ilaya")


# In[33]:


t = (23,45,67, (4,5,6),("ilaya"))


# In[34]:


t


# In[35]:


t1 = ([3,4,5,6], ("ilaya", 3.14), "Perumal")


# In[36]:


t1


# In[37]:


t1[0][2]= "sahaana"


# In[38]:


t1


# In[39]:


t1[0]="dfh"


# In[42]:


t1 = (23,34,565,777,8,78)


# In[43]:


l=list(t1)


# In[44]:


l


# In[45]:


tuple(l)


# # SET

# In[46]:


l=[2,4,5,6,4,5,6,4,3,7,8,9,4,57,6,8,9,3,4,6,7,8,3,2,4,5]


# In[48]:


set(l)


# In[49]:


s={}


# In[50]:


type(s)


# In[52]:


s1 = {2,3,4}


# In[53]:


type(s1)


# In[55]:


s2 = {6,4,3,7,8,9,4,6,8,9,3,4,6,7,8}


# In[56]:


s2


# In[59]:


s2[0]


# In[60]:


list(s2)


# In[66]:


l[1]


# In[67]:


s2


# In[68]:


s2.add(9988)


# In[69]:


s2


# In[70]:


s2.add("ilaya")


# In[71]:


s2


# In[72]:


s2.add([3,4,5,6])


# In[73]:


{(3,4,5,6),3,4,5,4,3,3}


# In[74]:


{[3,4,5,6],3,4,5,4,3,3}


# In[75]:


s


# In[76]:


s={(3,4,5,6),3,4,5,4,3,3}


# In[77]:


s


# In[78]:


s.remove(4)


# In[79]:


s


# In[80]:


s.discard(5)


# In[81]:


s


# In[82]:


s.remove(27)


# In[83]:


s.discard(27)


# In[84]:


s


# In[86]:


l = [3,4,5,6]


# In[87]:


set(l)


# In[95]:


d = {3,4}


# In[96]:


type(d)


# In[97]:


d = {}


# In[98]:


type(d)


# In[99]:


d = {4:"ilay"}


# In[102]:


d1 = {"key1" : 3445, "key2" : "ilaya", 54 :[3,4,5]}


# In[103]:


d1


# In[104]:


l[0]


# In[105]:


d1["key1"]


# In[106]:


d1[54]


# In[109]:


d = {5 : ["sdff", "ffwq", 3,4,5,6]}


# In[ ]:




