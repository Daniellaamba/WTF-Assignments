#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1. Write a Python program to create a tuple with different data types
tuple=("ama",True, 2.5,-7)
print(tuple)


# In[3]:


#2. Write a Python program to create a tuple with numbers and print one item
age=(25,80,57,8,10)
print(age[1])


# In[4]:


#3. Write a Python program to create a tuple
thistuple=("Kumasi","Accra","Tarkwa")
print(thistuple)
           


# In[12]:


#4. Write a Python program to convert a tuple to a string
cities=("Kumasi","Accra","Tarkwa")
cities_str=""
for item in cities:
    cities_str=cities_str+item
print(cities_str)

#or
cities_str="".join(cities)
print(cities_str)


# In[14]:


#5. Write a Python script to add a key to a dictionary
mydict={"Nigera":"Abuja","Ghana":"Accra","Rwanda":"Kigali","Kenya":"Nairobi"}
mydict["zimbabwe"]="Harare"
print(mydict)


# In[15]:


#6. Write a Python script to merge two Python dictionaries
mydict={"Nigera":"Abuja","Ghana":"Accra","Rwanda":"Kigali","Kenya":"Nairobi"}
mydict2={"Mali":"Bamako"}
mydict.update(mydict2)
print(mydict)


# In[21]:


#7.Write a Python program to sum all the items in a dictionary
mydict={"Nigera":120,"Ghana":30,"Rwanda":15,"Kenya":50}
print(sum(mydict.values()))


# In[ ]:




