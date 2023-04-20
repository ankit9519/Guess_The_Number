#!/usr/bin/env python
# coding: utf-8

# In[4]:


from random import randint
start = 1
end = 10000
value = randint(start,end)
guess = None
while guess != value:
    text = input("Guess the number: ")
    guess = int(text)
    if guess < value:
        print("The number is on the higher side. ")
    elif guess > value:
        print("The number is on the smaller side. ")
print("Excellent! You have guessed the number.")


# In[ ]:




