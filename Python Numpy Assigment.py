#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[11]:


a = np.array([[1,2,3],
              [4,5,6]])


# In[12]:


b = np.array([[10,11,12],
              [13,14,15]])


# In[13]:


sum(a,b)


# In[ ]:





# Q2. Given a numpy array (matrix), how to get a numpy array output which is equal to
# the original matrix multiplied by a scalar

# In[15]:


b = 2*a


# In[16]:


print(b)


# In[ ]:





# Q3. Create an identity matrix of dimension 4-by-4.

# In[17]:


i = np.eye(3)
i


# Q4. Convert a 1-D array to a 3-D array

# In[23]:


x = np.array([x for x in range(27)])

y = x.reshape((3,3,3))

y


# Q5. Convert a binary numpy array (containing only 0s and 1s) to a boolean numpy
# array

# In[24]:


k = np.array([[1, 0, 0],
              [1, 1, 1],
              [0, 0, 0]])

m = k.astype('bool')

m


# Q6. Convert all the elements of a numpy array from float to integer datatype

# In[25]:


j = np.array([[2.5, 3.8, 1.5],
              [4.7, 2.9, 1.56]])

p = j.astype('int')

p


# Q7. Stack 2 numpy arrays horizontally i.e., 2 arrays having the same 1st dimension
# (number of rows in 2D arrays)

# In[26]:


a1 = np.array([[1,2,3],
               [4,5,6]])

a2 = np.array([[7,8,9],
               [10,11,12]])

l = np.hstack((a1, a2))

l


# Q8. Output a sequence of equally gapped 5 numbers in the range 0 to 100 (both
# inclusive)

# In[27]:


g = np.arange(0, 101, 2)

g


# Q9. Output a matrix (numpy array) of dimension 2-by-3 with each and every value
# equal to 5
# 

# In[33]:


e = np.full((2, 3), 5)
e


# Q10.Given 2 numpy arrays as matrices, output the result of multiplying the 2 matrices
# (as a numpy array)
# 

# In[34]:


r = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

t = np.array([[2,3,4],
              [5,6,7],
              [8,9,10]])

w = np.matmul(r, t)

w


# Q11. Output the array element indexes such that the array elements appear in the
# ascending order

# In[35]:


array = np.array([46,36,7,9,42])

indexes = np.argsort(array)

indexes


# Q12.Multiply a 5x3 matrix by a 3x2 matrix (real matrix product).

# In[38]:


q = np.random.rand(5,3)
t = np.random.rand(3,2)
d = np.matmul(q, t)
d


# In[ ]:




