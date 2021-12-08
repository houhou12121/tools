import cv2
import numpy as np
import math
from PIL import Image
 
def psnr1(img1, img2):
   mse = np.mean((img1/1.0 - img2/1.0) ** 2 )
   if mse < 1.0e-10:
      return 100
   return 10 * math.log10(255.0**2/mse)
 
def psnr2(img1, img2):
   mse = np.mean( (img1/255. - img2/255.) ** 2 )
   if mse < 1.0e-10:
      return 100
   PIXEL_MAX = 1
   return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

if __name__=='__main__':
   img1=Image.open('output 620X720rggb_2.gif')
   img2=Image.open('output 620X720rggb.gif')
   img1=np.array(img1)
   img2=np.array(img2)
   psnr=psnr2(img1,img2)
   print(psnr)