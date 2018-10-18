
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from numpy import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

a = [1,2,3]
b = [2,3,4]

def miua(a):
    miua = [] 
    for i in range(len(a)):
        if(a[i] < 1):
            x = 0
            miua.append(x)
        elif(a[i] >= 1 and a[i] <= 2):
            x = a[i] - 1
            miua.append(x)
        elif(a[i] > 2 and a[i] <= 3):
            x = 3 - a[i]
            miua.append(x)
        elif(a[i] > 3):
            x = 0
            miua.append(x)
    return miua
miua = miua(a)
print("miu a = ",miua)

acut = 0.5
for x in miua:
    if (x > acut):
        print(x)
        
plt.plot(a,[0,1,0])
plt.plot([0, 5], [acut, acut], 'k-', lw=2)
plt.show()


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

a = [1,2,3]
b = [2,3,4]
print("A = ",a)
print("B = ",b,"\n")

def addition(a,b):
    if(len (a) == len (b)):
        c = []
        for i in range (len(a)):
            c.append(a[i]+b[i])
        return c
    else:
        print("Not triangle set")
        
add = addition(a,b)
print("A(+)B = ",add)

def substraction(a,b):
    if(len(a)==len(b)):
        c=[]
        for i in range(len(a)):
            c.append(a[i]-b[((len(b)-i)-1)])
        return c
    else:
        print("not triangle fuzzy set")

sub = substraction(a,b)
print("A(-)B = ",sub)
    
def multiplication(a,b):
    if(len (a) == len (b)):
        c = []
        for i in range (len(a)):
            for j in range (len(b)):
                x = a[i]*b[j]
                c.append(x)
        return c
    else:
        print("Not triangle set")

mul = multiplication(a,b)
print ("A(.)B = [",min(mul),",",max(mul),"]")

def division(a,b):
    if(len (a) == len (b)):
        c = []
        for i in range (len(a)):
            for j in range (len(b)):
                x = a[i]/b[j]
                c.append(x)
        return c
    else:
        print("Not triangle set")

div = division(a,b)
print ("A(/)B = [",min(div),",",max(div),"]")
    
def ain(a):
    if(len(a)):
        c = []
        for i in range(len(a)):
            x = 1/a[i]
            c.append(x)
        return c
    else:
        print("Not triangle set")
        
ain = ain(a)
print("A^-1 = [",np.round(min(ain),2),",",max(ain),"]")

def binv(b):
    if(len(b)):
        c = []
        for i in range(len(b)):
            x = 1/b[i]
            c.append(x)
        return c
    else:
        print("Not triangle set")
        
binv = binv(b)
print("B^-1 = [",np.round(min(binv),2),",",max(binv),"]")

plt.plot(a,[0,1,0])
plt.show()
plt.plot(b,[0,1,0])
plt.show()
plt.plot(add,[0,1,0])
plt.show()
plt.plot(sub,[0,1,0])
plt.show()
plt.plot(([min(mul),max(mul)]),[0,1])
plt.show()
plt.plot(([min(div),max(div)]),[0,1])
plt.show()
plt.plot(([min(ain),max(ain)]),[0,1])
plt.show()
plt.plot(([min(binv),max(binv)]),[0,1])
plt.show()

