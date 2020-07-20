#!/usr/bin/env python
# coding: utf-8

# In[1]:


print ('*')
print ('**')
print ('*****')


# In[2]:


import math
a=1
b=-40
c=391
d=(b**2)-(4*a*c)
sol1=(-b-math.sqrt(d))/(2*a)
sol2=(-b+math.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))


# In[3]:


X=15
Y=10
print ((X+Y)/(X-Y))
print ((X-Y)**3)
lastonedigit = (X+Y) %10
print(lastonedigit)


# In[4]:


player1 = input ("?")
player2 = input ("?")

if (player1 == 'rock' and player2 == 'scissors'):
    print ("Player 1 wins.")

elif (player1 == 'rock' and player2 == 'rock'):
    print ("Tie")

elif (player1 == 'scissors' and player2 == 'paper'):
    print ("Player 1 wins.")

elif (player2 == 'scissors' and player2 == 'scissors'):
    print ("Tie")

elif (player1 == 'paper' and player2 == 'paper'):
    print ("Tie")

elif (player1 == 'paper' and player2 == 'scissors'):
    print ("Player 2 wins.")

elif (player1 == 'rock'and player2 == 'paper'):
    print ("Player 2 wins.")

elif (player1 == 'paper' and player2 == 'rock'):
    print ("Player 2 wins.")

elif (player1 == 'scissors' and player2 == 'rock'):
    print ("Player 2 wins.")
else:
    print ("This is not a valid object selection.")


# In[5]:


x = input("temperature:")
y = input("c or f?")

x=int(x)
y=str(y)

c= (x-32)*(5/9)
f= (x+32)*(9/5)

if y=="f":
    print(x,"f", "is", c, "in celsius.")
elif y=="c":
    print(x,"c", "is", f, "in celsius.")


# In[ ]:




