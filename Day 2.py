#!/usr/bin/env python
# coding: utf-8

# In[1]:


s = ilayaperumal


# In[2]:


S = "ilayaperumal"


# In[6]:


S[1]


# In[7]:


S[0]


# In[8]:


S[4]


# In[9]:


S[3]


# In[10]:


S[-3]


# In[11]:


S[-4]


# In[12]:


a = "my name is sahaana"


# In[13]:


type(a)


# In[14]:


a[1]


# In[15]:


a[2]


# In[17]:


a[0:10]


# In[18]:


b = "sahaana"


# In[19]:


b[0:3]


# In[20]:


b[0:300]


# In[22]:


b[300]


# In[23]:


b[0:300]


# In[24]:


b[0:300:1]


# In[25]:


b[0:300:2]


# In[26]:


a[0:300:2]


# In[27]:


b[-1:-4]


# In[28]:


b[0:200:-1]


# In[29]:


b[-4:-1]


# In[30]:


b[-1:-4:-1]


# In[31]:


b[:::]


# In[32]:


b[::]


# In[33]:


b[:7]


# In[34]:


b[-2:]


# In[35]:


b[::-1]


# In[36]:


b[-1::-1]


# In[37]:


b[-2::-1]


# In[38]:


k ="my name is ilaya"


# In[39]:


k[::-1]


# In[43]:


k[-3:2:-1]


# In[44]:


k[-2:-10]


# In[45]:


k[-2:-10:-1]


# In[46]:


"ilay"*3


# In[47]:


"ilaya" + "perumal"


# In[48]:


"ilaya" - "ya"


# In[50]:


len(a)


# In[51]:


len(k)


# In[52]:


len(b)


# In[54]:


k.find("a")


# In[55]:


k.find("y")


# In[56]:


k


# In[57]:


k.find("m")


# In[58]:


k.find("il")


# In[59]:


k.find("ms")


# In[60]:


k.count("m")


# In[61]:


k


# In[62]:


k.count("a")


# In[63]:


k


# In[64]:


k.split()


# In[65]:


type(k.split())


# In[1]:


l[0]


# In[2]:


k


# In[3]:


k = "my name is ilaya"


# In[4]:


k


# In[10]:


k.split()


# In[11]:


type(k.split())


# In[12]:


l = k.split()


# In[13]:


l


# In[14]:


l[0]


# In[15]:


l[3]


# In[16]:


l[1:3]


# In[18]:


l[1:100:2]


# In[20]:


k.split('m')


# In[21]:


k.upper()


# In[22]:


k.swapcase()


# In[24]:


m = "saHaaNa"


# In[25]:


m.swapcase()


# In[26]:


k.title()


# In[27]:


a = "Namaa"
b = "chennai"


# In[28]:


a.join(b)


# In[29]:


" ".join("SAHAANA")


# In[38]:


reversed("sahaana")


# In[39]:


for i in reversed("sahaana"):
    print(i)


# In[41]:


s = " ilaya "


# In[42]:


s.strip()


# In[43]:


s.lstrip()


# In[44]:


s.rstrip()


# In[46]:


s.replace("l","m")


# In[52]:


s.center(20, "x")


# In[53]:


s.islower()


# In[54]:


s.isupper()


# In[57]:


s.startswith(" ")


# In[58]:


s.startswith("i")


# In[60]:


l = ["ilaya", "perumal", 423.54, 35+3j, True, 3445]


# In[61]:


type(l)


# In[62]:


l[0]


# In[63]:


l[-2]


# In[64]:


l


# In[65]:


l[0:4]


# In[66]:


l[::-1]


# In[72]:


l[-1:6]


# In[73]:


l[0]


# In[75]:


type(l[0])


# In[79]:


type(l[4])


# In[81]:


l[0][3]


# In[82]:


l[3]


# In[83]:


l[3].real


# In[84]:


l[3].imag


# In[86]:


l1 = [3445, True, (35+3j)]
l2 = ["Amazon", '3.14', 'ilaya']


# In[87]:


l1+l2


# In[88]:


l2+l1


# In[107]:


l1+l2


# In[93]:


p


# In[97]:


l1*3


# In[101]:


l1[0]


# In[102]:


l1[0]= "Flipkart"


# In[104]:


l1


# In[105]:


p


# In[108]:


l2


# In[110]:


l1[0]


# In[113]:


l1[0][0] = "S"


# In[119]:


l1.replace("F", "S")


# In[116]:


l1[0]


# In[120]:


s = "flipkart"


# In[121]:


s.replace("f", "s")


# In[122]:


l1


# In[124]:


"ilaya" in l1


# In[127]:


'3.14' in l1


# In[128]:


3.14 in l1


# In[129]:


'14' in l1


# In[132]:


l1 = [3445, True, (35+3j)]
l2 = ["Amazon", '3.14', 'ilaya']


# In[133]:


l1


# In[134]:


l2


# In[135]:


l2.append("Insta")


# In[136]:


l2


# In[137]:


l2.pop()


# In[138]:


l2.pop(2)


# In[139]:


l2


# In[140]:


l2.insert(1,"ilaya")


# In[141]:


l2


# In[142]:


l2.insert(2,[22,34,456])


# In[143]:


l2


# In[144]:


l2[::-1]


# In[145]:


l2.reverse()


# In[146]:


l2


# In[148]:


l2[::-1]


# In[149]:


l2


# In[150]:


l2.reverse()


# In[151]:


l2


# In[152]:


l2[2][1]


# In[153]:


l1


# In[156]:


l1.extend([34, True, "Airtel"])


# In[155]:


l1


# In[ ]:




