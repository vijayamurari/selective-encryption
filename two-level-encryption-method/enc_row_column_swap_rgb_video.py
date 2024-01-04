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
pathIn1="G:/impl/linux_backup/png_frames/"
files1 = [f for f in os.listdir(pathIn1) if os.path.isfile(os.path.join(pathIn1, f))]
files1.sort(key=lambda x: int(x[5:-4]))
key=random.randint(256,size=(r,c))
np.save('rgbchvideokey_swap',key)
for i in range(len(files1)):
    filename1=pathIn1+files1[i]
    img= cv2.imread(filename1,cv2.IMREAD_UNCHANGED)
    #r,c,t=img.shape
    blue_ch=img[:,:,0]
    green_ch=img[:,:,1]
    red_ch=img[:,:,2]
    #print("Green channel:",green_ch)
    
    #print("image array:",img[0])
    encrypted_image_blue=np.zeros((r, c), np.uint8)
    encrypted_image_green=np.zeros((r, c), np.uint8)
    encrypted_image_red=np.zeros((r, c), np.uint8)
    for row in range(r):
        for column in range(c):
            #enc_start=enc_start+time.clock()
            encrypted_image_blue[row, column] = blue_ch[row, column] ^ key[row, column]
            encrypted_image_green[row,column]= green_ch[row, column] ^ key[row, column]
            encrypted_image_red[row,column]=red_ch[row, column] ^ key[row, column]
            #enc_end=enc_end+time.clock()
            #cv2.imshow("Encrypted image", encrypted_image)

    encrypted_image_blue1=np.zeros((r,c),np.uint8)
    encrypted_image_blue1[:,0:640]=encrypted_image_blue[:,640:1280]
    encrypted_image_blue1[:,640:1280]=encrypted_image_blue[:,0:640]

    encrypted_image_green1=np.zeros((r,c),np.uint8)
    encrypted_image_green1[:,0:640]=encrypted_image_green[:,640:1280]
    encrypted_image_green1[:,640:1280]=encrypted_image_green[:,0:640]

    encrypted_image_red1=np.zeros((r,c),np.uint8)
    encrypted_image_red1[:,0:640]=encrypted_image_red[:,640:1280]
    encrypted_image_red1[:,640:1280]=encrypted_image_red[:,0:640]
    
    for row in range(r):
        for col in range(c):
            img[row][col][0]=encrypted_image_blue1[row][col]
            img[row][col][1]=encrypted_image_green1[row][col]
            img[row][col][2]=encrypted_image_red1[row][col]
    cv2.imwrite("G:/impl/linux_backup/enc_rgb_swap/frame%d.png" %i,img)
    #print("After encryption",img)

