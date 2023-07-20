#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


# Load the image
image = cv2.imread('shutterstock93075775--250.jpg')


# In[3]:


try:
    cv2.imshow('Image', image)
    cv2.waitKey(0)
except:
    print('There was an error, and the image did not load correctly.')


# In[4]:


try:
    output_path = 'C:/Users/mgdan/Downloads/M1PM_image_copy.jpg'
    cv2.imwrite(output_path, image)
    print('Image saved successfully.')
except:
    print('There was an error, and the image did not save correctly.')


# In[ ]:




