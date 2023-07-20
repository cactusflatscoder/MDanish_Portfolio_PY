#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np

image = cv2.imread("CSC515/Module 3/WIN_20230627_14_34_42_Pro.jpg")
height, width = image.shape[:2]
shrink = cv2.resize(image, (int(0.5*width), int(0.5*height)), interpolation = cv2.INTER_AREA)
# cv2.imshow("Image", shrink)
image_wmu = cv2.rectangle(shrink,(500,260),(650,215),(0,0,255), 3)
image_wmu = cv2.circle(image_wmu,(570,255), 145, (0,255,0), 3)
image_wmu = cv2.putText(image_wmu, 'This is me',(300,700), cv2.FONT_HERSHEY_SIMPLEX, 4,(255,255,255),2,cv2.LINE_AA)
cv2.imshow("Image with Markup", image_wmu)

cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:




