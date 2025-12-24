import numpy as np
import cv2
from google.colab.patches import cv2_imshow
img=cv2.imread("/content/sacca.jpg",0)
if img is not None:
  alpha=2.5
  beta=50
  new_image=cv2.convertScaleAbs(img,alpha=alpha,beta=beta)
  print("original one....")
  cv2_imshow(img)
  print("new one....")
  cv2_imshow(new_image)
else:
  print("error")
