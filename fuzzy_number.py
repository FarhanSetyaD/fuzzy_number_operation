
# coding: utf-8

# In[12]:


get_ipython().run_line_magic('matplotlib', 'inline')
from numpy import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

A = [0,1,2,3,4,5,6,7,8,9,10]
B = []
acut = 0.5
for i in range(len(A)):
    x = A[i]/(A[i]+2)
    B.append(x)
    c = np.round(B,2)
    
for x in B:
    if (x > acut):
        print(x)

print("\nPEMBULATAN 2 ANGKA BELAKANG KOMA")
for x in c:
    if (x > acut):
        print(x)

plt.plot(A, B, 'ro')
plt.plot([-3, 15], [acut, acut], 'k-', lw=2)
plt.axis([-3, 15, 0, 1])
plt.show()


# In[27]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

a = [1,2,3]
b = [2,3,4]

def addition(a,b):
    if(len (a) == len (b)):
        c = []
        for i in range (len(a)):
            for j in range (len(b)):
                c.append(a[i]+b[j])
        return c
    else:
        print("Not triangle set")
        
hasil = addition(a,b)
print(hasil)

def remove_duplicates(hasil):
    output = []
    seen = set()
    for hasil in hasil:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if hasil not in seen:
            output.append(hasil)
            seen.add(hasil)
    return output
kombinasi = sorted(remove_duplicates(hasil))
print("kombinasi = ",kombinasi)

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

def miub(b):
    miub = []
    for i in range(len(b)):
        if(b[i] < 1):
            x = 0
            miub.append(x)
        elif(b[i] >= 2 and b[i] <= 3):
            x = b[i] - 2
            miub.append(x)
        elif(b[i] > 3 and b[i] <= 4):
            x = 4 - b[i]
            miub.append(x)
        elif(b[i] > 4):
            x = 0
            miub.append(x)
    return miub
miub = miub(b)
print("miu b = ",miub)

def miu_tiga(miua, miub):
    miu_tiga = []
    x = max(min(miua[0],miub[0]),0)
    miu_tiga.append(x)
    return miu_tiga
miu_tiga = miu_tiga(miua, miub) 
print("miu 3 = ",miu_tiga)

def miu_empat(miua, miub):
    miu_empat = []
    x = max(min(miua[1],miub[0]),min(miua[0],miub[1]))
    miu_empat.append(x)
    return miu_empat
miu_empat = miu_empat(miua, miub) 
print("miu 4 = ",miu_empat)

def miu_lima(miua, miub):
    miu_lima = []
    x = max(min(miua[0],miub[2]),min(miua[1],miub[1]),min(miua[2],miub[0]))
    miu_lima.append(x)
    return miu_lima
miu_lima = miu_lima(miua, miub) 
print("miu 5 = ",miu_lima)

def miu_enam(miua, miub):
    miu_enam = []
    x = max(min(miua[1],miub[2]),min(miua[2],miub[1]))
    miu_enam.append(x)
    return miu_enam
miu_enam = miu_enam(miua, miub) 
print("miu 6 = ",miu_enam)

def miu_tujuh(miua, miub):
    miu_tujuh = []
    x = max(min(miua[2],miub[2]),0)
    miu_tujuh.append(x)
    return miu_tujuh
miu_tujuh = miu_tujuh(miua, miub) 
print("miu 7 = ",miu_tujuh)

x = kombinasi
y = [miu_tiga,miu_empat,miu_lima,miu_enam,miu_tujuh]
plt.plot(a,[0,1,0])
plt.plot(b,[0,1,0])
plt.plot(x,y)
plt.xlabel('GRAFIK miu A(+)B')
plt.show()


# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

a = [1,2,3]
b = [2,3,4]

def substraction(a,b):
    if(len (a) == len (b)):
        c = []
        for i in range (len(a)):
            for j in range (len(b)):
                c.append(a[i]-b[j])
        return c
    else:
        print("Not triangle set")
hasil = substraction(a,b)
print(hasil)

def remove_duplicates(hasil):
    output = []
    seen = set()
    for hasil in hasil:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if hasil not in seen:
            output.append(hasil)
            seen.add(hasil)
    return output
kombinasi = sorted(remove_duplicates(hasil))
print("kombinasi = ",kombinasi)

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

def miub(b):
    miub = []
    for i in range(len(b)):
        if(b[i] < 1):
            x = 0
            miub.append(x)
        elif(b[i] >= 2 and b[i] <= 3):
            x = b[i] - 2
            miub.append(x)
        elif(b[i] > 3 and b[i] <= 4):
            x = 4 - b[i]
            miub.append(x)
        elif(b[i] > 4):
            x = 0
            miub.append(x)
    return miub
miub = miub(b)
print("miu b = ",miub)

def miu_mintiga(miua, miub):
    miu_mintiga = []
    x = max(min(miua[0],miub[2]),0)
    miu_mintiga.append(x)
    return miu_mintiga
miu_mintiga = miu_mintiga(miua, miub) 
print("miu -3 = ",miu_mintiga)

def miu_mindua(miua, miub):
    miu_mindua = []
    x = max(min(miua[0],miub[1]),min(miua[1],miub[2]))
    miu_mindua.append(x)
    return miu_mindua
miu_mindua = miu_mindua(miua, miub) 
print("miu -2 = ",miu_mindua)

def miu_minsatu(miua, miub):
    miu_minsatu = []
    x = max(min(miua[0],miub[0]),min(miua[1],miub[1]),min(miua[2],miub[2]))
    miu_minsatu.append(x)
    return miu_minsatu
miu_minsatu = miu_minsatu(miua, miub) 
print("miu -1 = ",miu_minsatu)

def miu_nol(miua, miub):
    miu_nol = []
    x = max(min(miua[1],miub[0]),min(miua[2],miub[1]))
    miu_nol.append(x)
    return miu_nol
miu_nol = miu_nol(miua, miub) 
print("miu 0 = ",miu_nol)

def miu_satu(miua, miub):
    miu_satu = []
    x = max(min(miua[0],miub[2]),0)
    miu_satu.append(x)
    return miu_satu
miu_satu = miu_satu(miua, miub) 
print("miu 1 = ",miu_satu)

x = kombinasi
y = [miu_mintiga,miu_mindua,miu_minsatu,miu_nol,miu_satu]
plt.plot(a,[0,1,0])
plt.plot(b,[0,1,0])
plt.plot(x,y)
plt.xlabel('GRAFIK miu A(-)B')
plt.show()


# In[25]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

a = [1,2,3]
b = [2,3,4]

def multiplication(a,b):
    if(len (a) == len (b)):
        c = []
        for i in range (len(a)):
            for j in range (len(b)):
                c.append(a[i]*b[j])
        return c
    else:
        print("Not triangle set")
        
hasil = multiplication(a,b)
print(hasil)

def remove_duplicates(hasil):
    output = []
    seen = set()
    for hasil in hasil:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if hasil not in seen:
            output.append(hasil)
            seen.add(hasil)
    return output
kombinasi = sorted(remove_duplicates(hasil))
print("kombinasi = ",kombinasi)

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

def miub(b):
    miub = []
    for i in range(len(b)):
        if(b[i] < 1):
            x = 0
            miub.append(x)
        elif(b[i] >= 2 and b[i] <= 3):
            x = b[i] - 2
            miub.append(x)
        elif(b[i] > 3 and b[i] <= 4):
            x = 4 - b[i]
            miub.append(x)
        elif(b[i] > 4):
            x = 0
            miub.append(x)
    return miub
miub = miub(b)
print("miu b = ",miub)

def miu_dua(miua, miub):
    miu_dua = []
    x = max(min(miua[0],miub[0]),0)
    miu_dua.append(x)
    return miu_dua
miu_dua = miu_dua(miua, miub) 
print("miu 3 = ",miu_dua)

def miu_tiga(miua, miub):
    miu_tiga = []
    x = max(min(miua[0],miub[1]),0)
    miu_tiga.append(x)
    return miu_tiga
miu_tiga = miu_tiga(miua, miub) 
print("miu 3 = ",miu_tiga)

def miu_empat(miua, miub):
    miu_empat = []
    x = max(min(miua[0],miub[2]),min(miua[1],miub[0]))
    miu_empat.append(x)
    return miu_empat
miu_empat = miu_empat(miua, miub) 
print("miu 4 = ",miu_empat)

def miu_enam(miua, miub):
    miu_enam = []
    x = max(min(miua[1],miub[1]),min(miua[2],miub[0]))
    miu_enam.append(x)
    return miu_enam
miu_enam = miu_enam(miua, miub) 
print("miu 6 = ",miu_enam)

def miu_lapan(miua, miub):
    miu_lapan = []
    x = max(min(miua[1],miub[2]),0)
    miu_lapan.append(x)
    return miu_lapan
miu_lapan = miu_lapan(miua, miub) 
print("miu 8 = ",miu_lapan)

def miu_bilan(miua, miub):
    miu_bilan = []
    x = max(min(miua[2],miub[1]),0)
    miu_bilan.append(x)
    return miu_bilan
miu_bilan = miu_bilan(miua, miub) 
print("miu 9 = ",miu_bilan)

def miu_dulas(miua, miub):
    miu_dulas = []
    x = max(min(miua[2],miub[2]),0)
    miu_dulas.append(x)
    return miu_dulas
miu_dulas = miu_dulas(miua, miub) 
print("miu 12 = ",miu_dulas)

x = kombinasi
y = [miu_dua,miu_tiga,miu_empat,miu_enam,miu_lapan,miu_bilan,miu_dulas]
plt.plot(a,[0,1,0])
plt.plot(b,[0,1,0])
plt.plot(x,y)
plt.xlabel('GRAFIK miu A(⋅)B')
plt.show()


# In[26]:


get_ipython().run_line_magic('matplotlib', 'inline')
from numpy import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

a = [1,2,3]
b = [2,3,4]

def division(a,b):
    if(len (a) == len (b)):
        c = []
        for i in range (len(a)):
            for j in range (len(b)):
                c.append(a[i]/b[j])
        return c
    else:
        print("Not triangle set")
        
hasil = division(a,b)
print(hasil)

def remove_duplicates(hasil):
    output = []
    seen = set()
    for hasil in hasil:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if hasil not in seen:
            output.append(hasil)
            seen.add(hasil)
    return output
kombinasi = sorted(remove_duplicates(hasil))
div = np.round(kombinasi,2)
print("kombinasi = ",div)

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

def miub(b):
    miub = []
    for i in range(len(b)):
        if(b[i] < 1):
            x = 0
            miub.append(x)
        elif(b[i] >= 2 and b[i] <= 3):
            x = b[i] - 2
            miub.append(x)
        elif(b[i] > 3 and b[i] <= 4):
            x = 4 - b[i]
            miub.append(x)
        elif(b[i] > 4):
            x = 0
            miub.append(x)
    return miub
miub = miub(b)
print("miu b = ",miub)

def miu_025(miua, miub):
    miu_025 = []
    x = max(min(miua[0],miub[2]),0)
    miu_025.append(x)
    return miu_025
miu_025 = miu_025(miua, miub) 
print("miu 0.25 = ",miu_025)

def miu_033(miua, miub):
    miu_033 = []
    x = max(min(miua[0],miub[1]),0)
    miu_033.append(x)
    return miu_033
miu_033 = miu_033(miua, miub) 
print("miu 0.33 = ",miu_033)

def miu_05(miua, miub):
    miu_05 = []
    x = max(min(miua[0],miub[0]),min(miua[1],miub[2]))
    miu_05.append(x)
    return miu_05
miu_05 = miu_05(miua, miub) 
print("miu 0.5 = ",miu_05)

def miu_067(miua, miub):
    miu_067 = []
    x = max(min(miua[1],miub[1]),0)
    miu_067.append(x)
    return miu_067
miu_067 = miu_067(miua, miub) 
print("miu 0.67 = ",miu_067)

def miu_075(miua, miub):
    miu_075 = []
    x = max(min(miua[2],miub[2]),0)
    miu_075.append(x)
    return miu_075
miu_075 = miu_075(miua, miub) 
print("miu 0.75 = ",miu_075)

def miu_1(miua, miub):
    miu_1 = []
    x = max(min(miua[2],miub[1]),0)
    miu_1.append(x)
    return miu_1
miu_1 = miu_1(miua, miub) 
print("miu 1 = ",miu_1)

def miu_15(miua, miub):
    miu_15 = []
    x = max(min(miua[2],miub[0]),0)
    miu_15.append(x)
    return miu_15
miu_15 = miu_15(miua, miub) 
print("miu 1.5 = ",miu_15)

x = kombinasi
y = [miu_025,miu_033,miu_05,miu_067,miu_075,miu_1,miu_15]
plt.plot(a,[0,1,0])
plt.plot(b,[0,1,0])
plt.plot(x,y)
plt.xlabel('GRAFIK miu A(/)B')
plt.show()


# In[42]:


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
plt.plot(b,[0,1,0])
plt.plot(add,[0,1,0])
plt.plot(sub,[0,1,0])
plt.plot(([min(mul),max(mul)]),[0,1])
plt.plot(([min(div),max(div)]),[0,1])
plt.plot(([min(ain),max(ain)]),[0,1])
plt.plot(([min(binv),max(binv)]),[0,1])
plt.axis()
plt.show()

