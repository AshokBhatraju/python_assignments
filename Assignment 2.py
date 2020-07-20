#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input('enter a positive integer:'))
x = n**2
if n<0:
    print('The input you gave is not valid. It must be positive.')
elif n>0:
    print (x)


# In[2]:


n = int(input('enter a positive integer:'))
for row in range(1,n+1):
    for column in range(1,row+1):
        print(column,end="")
    print("")


# In[3]:


pi = 0
accuracy = 10000
for n in range(0,accuracy):
    pi += ((-1)**n)*4/(2*n+1)
    
    print (pi)


# In[5]:


n = int(input('how many marbles to start with?'))
while n>0:
    a = int(input('player #1, there are {} marbles left. how many marbles will you take? '. format(n)))
    n=n-a
    if n>0:
        b = int(input('player #2, there are {} marbles left. how many marbles will you take? '. format(n)))
        n=n-b
        if n>0:
            continue
        else:
            print('player #2, you took the last marble and have won!')
    else:
        print('player #1, you took the last marble and have won!')


# In[6]:


x = int(input("enter a positive integer:"))
i = 1
while i<(x+1):
    print ('*'*(2*i-1)+' '*(4*x-2-4*i+2)+'*'*(2*i-1))
    i=i+1


# In[ ]:




