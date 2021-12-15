from PIL import Image  
import numpy as np  

def rgb_bayer():
    bayer_list=[0,1,2,3]#rggb、grbg、gbrg、bggr
    bayer_type=['rggb','grbg','gbrg','bggr']
    bayer_style=bayer_list[0]
    image = Image.open('input.jpg')
    Image_array = np.array(image)
    Image_array=Image_array**2.2 #gamma反变换（恢复到线性空间）
    #print(Image_array[700][100][1])
    shape=Image_array.shape
    Image_bayer=np.zeros((shape[0],shape[1]),dtype=int)
    for i in range(shape[0]):
        for j in range(shape[1]):
            if bayer_style==0:
                if (i+1)%2==1:
                    if (j+1)%2==1: #rggb
                        Image_bayer[i][j]=Image_array[i][j][0]  #奇行奇列 r
                    else:
                        Image_bayer[i][j]=Image_array[i][j][1]  #奇行偶列 g
                elif (i+1)%2==0:
                    if (j+1)%2==1:
                        Image_bayer[i][j]=Image_array[i][j][1]  #偶行奇列 g
                    else:
                        Image_bayer[i][j]=Image_array[i][j][2]  #偶行偶列 b
            elif bayer_style==1:  #grbg
                if (i+1)%2==1:
                    if (j+1)%2==1:
                        Image_bayer[i][j]=Image_array[i][j][1]  #g
                    else:
                        Image_bayer[i][j]=Image_array[i][j][0]  #r
                elif (i+1)%2==0:
                    if (j+1)%2==1:
                        Image_bayer[i][j]=Image_array[i][j][2]  #b
                    else:
                        Image_bayer[i][j]=Image_array[i][j][1]  #g
            elif bayer_style==2: #gbrg
                if (i+1)%2==1:
                    if (j+1)%2==1:
                        Image_bayer[i][j]=Image_array[i][j][1]  #g
                    else:
                        Image_bayer[i][j]=Image_array[i][j][2]  #b
                elif (i+1)%2==0:
                    if (j+1)%2==1:
                        Image_bayer[i][j]=Image_array[i][j][0]  #r
                    else:
                        Image_bayer[i][j]=Image_array[i][j][1]  #g
            elif bayer_style==3: #bggr
                if (i+1)%2==1:
                    if (j+1)%2==1:
                        Image_bayer[i][j]=Image_array[i][j][2]  #b
                    else:
                        Image_bayer[i][j]=Image_array[i][j][1]  #g
                elif (i+1)%2==0:
                    if (j+1)%2==1:
                        Image_bayer[i][j]=Image_array[i][j][1]  #g
                    else:
                        Image_bayer[i][j]=Image_array[i][j][0]  #r
    Image_bayer.tofile('output %dX%d%s.txt'% (shape[0],shape[1],bayer_type[bayer_style]))
    
    Image_bayer=Image_bayer**(1/2.2)#gamma矫正，用作显示
    Image_pic=Image.fromarray(np.uint8(Image_bayer))
    Image_pic.show()    
    
    Image_pic.save('output %dX%d%s.gif'% (shape[0],shape[1],bayer_type[bayer_style]))  


if __name__=='__main__':
    rgb_bayer()




