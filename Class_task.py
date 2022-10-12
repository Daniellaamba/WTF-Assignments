#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Write a Python program to create a tuple with different data types.
tupe = ("tech4dev", True, 3.223, 1)
print(tupe)


# In[2]:


# 2.  Write a Python program to create a tuple with numbers and print one item
tupe1 = (23,45,67,123,90,12,2,0,1,7,)
print(tupe1[2])


# In[3]:


# 3. Write a Python program to create a tuple
colors = ('red', 'blue', 'yellow', 'green', 'black', 'white', 'pink')
print(colors)


# In[1]:


# 4. Write a Python program to convert a tuple to a string
#tupe2 = ('c', 'l', 'a', 's', 's', 't', 'a', 's', 'k')
#tupe2_str =  ''.join(tupe2)
#print(tupe2_str)

# or
tupe2 = ('c', 'l', 'a', 's', 's', 't', 'a', 's', 'k')
tupe2_str = " "
for item in tupe2:
    tupe2_str = tupe2_str + item
print(tupe2_str)


# In[ ]:


# 5. Write a Python script to add a key to a dictionary.


# In[2]:


#5. Write a Python script to add a key to a dictionary
mydict={"Nigera":"Abuja","Ghana":"Accra","Rwanda":"Kigali","Kenya":"Nairobi"}
mydict["zimbabwe"]="Harare"
print(mydict)


# In[3]:


#6. Write a Python script to merge two Python dictionaries
mydict={"Nigera":"Abuja","Ghana":"Accra","Rwanda":"Kigali","Kenya":"Nairobi"}
mydict2={"Mali":"Bamako"}
mydict.update(mydict2)
print(mydict)


# In[4]:


#7.Write a Python program to sum all the items in a dictionary
mydict={"Nigera":120,"Ghana":30,"Rwanda":15,"Kenya":50}
print(sum(mydict.values()))


# In[ ]:




