import psnr
import ssim
import rgb_bayer_ssim

if __name__ == "__main__":
    #produce different kinds of bayers
    rgb_bayer_ssim.rgb_bayer()
    #calculate psnr
    img1=Image.open('output 620X720rggb_2.gif')
    img2=Image.open('output 620X720rggb.gif')
    img1=np.array(img1)
    img2=np.array(img2)
    psnr=psnr.psnr2(img1,img2)
    #calculate ssim
    print(compute_ssim(img1,img2))


    