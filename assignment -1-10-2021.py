#!/usr/bin/env python
# coding: utf-8

# In[73]:


#1
def lambda_function(a,b):
 x= a * (b-2)
 print(x)

lambda_function(5,4)
def string(w):
    for i in w.split(":"):
        print(i,end=" ")
string("hello:everyone")


# In[106]:


#2
def staircase(num):
    if num > 0:
        for i in range(num):
            for j in range (num):
                if i+j == num-1:
                    print("_"*j+"#"*(num-j))
    else:
        num=abs(num)
        for i in range(num):
            for j in range (num):
                if i+j == num-1:
                    print("_"*(num-j)+"#"*(j))

Underscore(-5)


# In[154]:


#3
def x(n):
    new = []
    for i in n.split(" "):
        new.append(i)

    a = new[-1]
    b = []
    for k,j in enumerate(a.split("-")):
        b.append(j)
    if int(b[-1]) < 25:
            old = b[-1]
            b[-1] = "20" + str(old)
    else:
        old = b[-1]
        b[-1] = "19" + str(old)
    
    print(b)
x("I was born in 23-06-98")


# In[122]:


#4 
def range_1(x,y):
    a = []
    for i in range(x,y+1):
        if i < 10:
            a.append(i)
        else:
            x = sum(int(digit) for digit in str(i))
            a.append(x)
    sum_1 = sum(a)
    print(sum_1)


# In[121]:


range_1(1,10)


# In[117]:


#7
import itertools

def ranges(i):
    for a, b in itertools.groupby(enumerate(i), lambda pair: pair[1] - pair[0]):
        b = list(b)
        yield b[0][1], b[-1][1]

print(list(ranges([0,1, 3, 4, 7, 8, 9,10,11])))


# In[115]:


#8
def length(n):
    x = []
    y = []
    for i in n:
        if int(i) == 0:
            x.append(i)
        elif int(i) == 1:
            y.append(i)
    if len(x) == len(y):
            print ("True")
    else:
            print ("False")

length("111")


# In[149]:


def year(n):
    new = []



    for i in n.split(" "):
        new.append(i)

    a = new[-1]
    b = []
    for k,j in enumerate(a.split("-")):
        b.append(j)


    if int(b[-1]) < 25:
        old = b[-1]
        b[-1] = "20" + str(old)



    else:
        old = b[-1]
        b[-1] = "19" + str(old)





    print(b)
year("I was born in 20-05-96")


# In[ ]:




