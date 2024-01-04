import cv2
import numpy as np
from numpy import random
import os
import time
r=720
c=1280
t=3
'''enc_start=0
enc_end=0
dec_start=0
dec_end=0'''
pathIn1="G:/impl/linux_backup/enc_rgb_swap/"
files1 = [f for f in os.listdir(pathIn1) if os.path.isfile(os.path.join(pathIn1, f))]
files1.sort(key=lambda x: int(x[5:-4]))

key=np.load('rgbchvideokey.npy')
for i in range(len(files1)):
    filename1=pathIn1+files1[i]
    img= cv2.imread(filename1,cv2.IMREAD_UNCHANGED)
    #r,c,t=img.shape
    enc_blue_ch=img[:,:,0]
    enc_green_ch=img[:,:,1]
    enc_red_ch=img[:,:,2]
    
    for row in range(r):
        for column in range(c):
            #enc_start=enc_start+time.clock()
            decrypted_image_blue[row, column] = encrypted_image_blue1[row, column] ^ key[row, column]
            decrypted_image_green[row,column]= encrypted_image_green1[row, column] ^ key[row, column]
            decrypted_image_red[row,column]=encrypted_image_red1[row, column] ^ key[row, column]
            #enc_end=enc_end+time.clock()
            #cv2.imshow("Encrypted image", encrypted_image)

    #cv2.imwrite("G:/murari/phd/impl/linux_backup/green_frames/frame%d.jpg" %i, encrypted_image)
    #print("Encrypted image:",encrypted_image)
    #print("encrypted_image:",encrypted_image[0][0])
    for row in range(r):
        for col in range(c):
            img[row][col][0]=decrypted_image_blue[row][col]
            img[row][col][1]=decrypted_image_green[row][col]
            img[row][col][2]=decrypted_image_red[row][col]
    cv2.imwrite("G:/impl/linux_backup/dec_rgb_dec/frame%d.png" %i,img)
    #print("After encryption",img)

