import cv2
import numpy as np
from numpy import random
#import random
import os
import time

#Blue channel

def blue_xor1(x,y,blue_ch,blue_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               
               rc_image1[0:80,0:80]=blue_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               blue_tr[x:y,x+1200:y+1200]=xor_image1[0:80,0:80]
               #print("Green channel traspose:",blue_tr)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x+80:y+80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               blue_tr[x+80:y+80,1200:1280]=xor_image2[0:80,0:80]
               #print("Green channel:",blue_tr)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x+160:y+160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]

               #print("After encryption+row column transpose",xor_image)
               blue_tr[x+160:y+160,1200:1280]=xor_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x+240:y+240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               blue_tr[x+240:y+240,1200:1280]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x+320:y+320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               blue_tr[x+320:y+320,1200:1280]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x+400:y+400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               blue_tr[x+400:y+400,1200:1280]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x+480:y+480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               blue_tr[x+480:y+480,1200:1280]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x+560:y+560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               blue_tr[x+560:y+560,1200:1280]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x+640:y+640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               blue_tr[x+640:y+640,1200:1280]=xor_image9[0:80,0:80]
               
               return blue_tr
               
def blue_xor2(x,y,blue_ch,blue_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               blue_tr[x-80:y-80,1120:1200]=xor_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               blue_tr[x:y,1120:1200]=xor_image2[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x+80:y+80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               blue_tr[x+80:y+80,1120:1200]=xor_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x+160:y+160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               blue_tr[x+160:y+160,1120:1200]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x+240:y+240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               blue_tr[x+240:y+240,1120:1200]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x+320:y+320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               blue_tr[x+320:y+320,1120:1200]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x+400:y+400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               blue_tr[x+400:y+400,1120:1200]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x+480:y+480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               blue_tr[x+480:y+480,1120:1200]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x+560:y+560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               blue_tr[x+560:y+560,1120:1200]=xor_image9[0:80,0:80]
               return blue_tr

def blue_xor3(x,y,blue_ch,blue_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               blue_tr[x-160:y-160,1040:1120]=xor_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               blue_tr[x-80:y-80,1040:1120]=xor_image2[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               blue_tr[x:y,1040:1120]=xor_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x+80:y+80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               blue_tr[x+80:y+80,1040:1120]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x+160:y+160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               blue_tr[x+160:y+160,1040:1120]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x+240:y+240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               blue_tr[x+240:y+240,1040:1120]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x+320:y+320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               blue_tr[x+320:y+320,1040:1120]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x+400:y+400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               blue_tr[x+400:y+400,1040:1120]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x+480:y+480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               blue_tr[x+480:y+480,1040:1120]=xor_image9[0:80,0:80]
               return blue_tr              

def blue_xor4(x,y,blue_ch,blue_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               blue_tr[x-240:y-240,960:1040]=xor_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               blue_tr[x-160:y-160,960:1040]=xor_image2[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               blue_tr[x-80:y-80,960:1040]=xor_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               blue_tr[x:y,960:1040]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x+80:y+80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               blue_tr[x+80:y+80,960:1040]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x+160:y+160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               blue_tr[x+160:y+160,960:1040]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x+240:y+240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               blue_tr[x+240:y+240,960:1040]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x+320:y+320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               blue_tr[x+320:y+320,960:1040]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x+400:y+400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               blue_tr[x+400:y+400,960:1040]=xor_image9[0:80,0:80]
               return blue_tr              

def blue_xor5(x,y,blue_ch,blue_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               blue_tr[x-320:y-320,880:960]=xor_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               blue_tr[x-240:y-240,880:960]=xor_image2[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               blue_tr[x-160:y-160,880:960]=xor_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               blue_tr[x-80:y-80,880:960]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               blue_tr[x:y,880:960]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x+80:y+80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               blue_tr[x+80:y+80,880:960]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x+160:y+160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               blue_tr[x+160:y+160,880:960]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x+240:y+240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               blue_tr[x+240:y+240,880:960]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x+320:y+320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               blue_tr[x+320:y+320,880:960]=xor_image9[0:80,0:80]
               return blue_tr              

def blue_xor6(x,y,blue_ch,blue_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               blue_tr[x-400:y-400,800:880]=xor_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               blue_tr[x-320:y-320,800:880]=xor_image2[0:80,0:80]
               print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               blue_tr[x-240:y-240,800:880]=xor_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               blue_tr[x-160:y-160,800:880]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               blue_tr[x-80:y-80,800:880]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               blue_tr[x:y,800:880]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x+80:y+80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               blue_tr[x+80:y+80,800:880]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x+160:y+160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               blue_tr[x+160:y+160,800:880]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x+240:y+240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               blue_tr[x+240:y+240,800:880]=xor_image9[0:80,0:80]
               return blue_tr              

def blue_xor7(x,y,blue_ch,blue_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               blue_tr[x-480:y-480,720:800]=xor_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               blue_tr[x-400:y-400,720:800]=xor_image2[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               blue_tr[x-320:y-320,720:800]=xor_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               blue_tr[x-240:y-240,720:800]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               blue_tr[x-160:y-160,720:800]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               blue_tr[x-80:y-80,720:800]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               blue_tr[x:y,720:800]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x+80:y+80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               blue_tr[x+80:y+80,720:800]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x+160:y+160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               blue_tr[x+160:y+160,720:800]=xor_image9[0:80,0:80]
               return blue_tr              

def blue_xor8(x,y,blue_ch,blue_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               blue_tr[x-560:y-560,640:720]=xor_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               #print("After encryption+row column transpose",xor_image)
               blue_tr[x-480:y-480,640:720]=xor_image2[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               #print("After encryption+row column transpose",xor_image)
               blue_tr[x-400:y-400,640:720]=xor_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               #print("After encryption+row column transpose",xor_image)
               blue_tr[x-320:y-320,640:720]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               blue_tr[x-240:y-240,640:720]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               #print("After encryption+row column transpose",xor_image)
               blue_tr[x-160:y-160,640:720]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               #print("After encryption+row column transpose",xor_image)
               blue_tr[x-80:y-80,640:720]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               blue_tr[x:y,640:720]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x+80:y+80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               blue_tr[x+80:y+80,640:720]=xor_image9[0:80,0:80]
               return blue_tr
            
def blue_xor9(x,y,blue_ch,blue_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-640:y-640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               blue_tr[x-640:y-640,560:640]=xor_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               #print("After encryption+row column transpose",xor_image)
               blue_tr[x-560:y-560,560:640]=xor_image2[0:80,0:80]
               print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               #print("After encryption+row column transpose",xor_image)
               blue_tr[x-480:y-480,560:640]=xor_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               blue_tr[x-400:y-400,560:640]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               blue_tr[x-320:y-320,560:640]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               #print("After encryption+row column transpose",xor_image)
               blue_tr[x-240:y-240,560:640]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               blue_tr[x-160:y-160,560:640]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               blue_tr[x-80:y-80,560:640]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               blue_tr[x:y,560:640]=xor_image9[0:80,0:80]
               return blue_tr             

def blue_xor10(x,y,blue_ch,blue_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-720:y-720,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               blue_tr[x-720:y-720,480:560]=xor_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-640:y-640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               blue_tr[x-640:y-640,480:560]=xor_image2[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               blue_tr[x-560:y-560,480:560]=xor_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               blue_tr[x-480:y-480,480:560]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               blue_tr[x-400:y-400,480:560]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               blue_tr[x-320:y-320,480:560]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               blue_tr[x-240:y-240,480:560]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               blue_tr[x-160:y-160,480:560]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               blue_tr[x-80:y-80,480:560]=xor_image9[0:80,0:80]
               return blue_tr             

def blue_xor11(x,y,blue_ch,blue_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-800:y-800,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               blue_tr[x-800:y-800,400:480]=xor_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-720:y-720,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               blue_tr[x-720:y-720,400:480]=xor_image2[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-640:y-640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               blue_tr[x-640:y-640,400:480]=xor_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               blue_tr[x-560:y-560,400:480]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               blue_tr[x-480:y-480,400:480]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               blue_tr[x-400:y-400,400:480]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               blue_tr[x-320:y-320,400:480]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               blue_tr[x-240:y-240,400:480]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               blue_tr[x-160:y-160,400:480]=xor_image9[0:80,0:80]
               return blue_tr              

def blue_xor12(x,y,blue_ch,blue_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-880:y-880,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               blue_tr[x-880:y-880,320:400]=xor_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-800:y-800,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               blue_tr[x-800:y-800,320:400]=xor_image2[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-720:y-720,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               blue_tr[x-720:y-720,320:400]=xor_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x-640:y-640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               blue_tr[x-640:y-640,320:400]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               blue_tr[x-560:y-560,320:400]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               blue_tr[x-480:y-480,320:400]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               blue_tr[x-400:y-400,320:400]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               blue_tr[x-320:y-320,320:400]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               blue_tr[x-240:y-240,320:400]=xor_image9[0:80,0:80]
               return blue_tr              

def blue_xor13(x,y,blue_ch,blue_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-960:y-960,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               blue_tr[x-960:y-960,240:320]=xor_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-880:y-880,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               
               blue_tr[x-880:y-880,240:320]=xor_image2[0:80,0:80]
               print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-800:y-800,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               blue_tr[x-800:y-800,240:320]=xor_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x-720:y-720,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               blue_tr[x-720:y-720,240:320]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x-640:y-640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               blue_tr[x-640:y-640,240:320]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               blue_tr[x-560:y-560,240:320]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               blue_tr[x-480:y-480,240:320]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               blue_tr[x-400:y-400,240:320]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               blue_tr[x-320:y-320,240:320]=xor_image9[0:80,0:80]
               return blue_tr    

def blue_xor14(x,y,blue_ch,blue_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-1040:y-1040,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
                   
               blue_tr[x-1040:y-1040,160:240]=xor_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-960:y-960,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               blue_tr[x-960:y-960,160:240]=xor_image2[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-880:y-880,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               blue_tr[x-880:y-880,160:240]=xor_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x-800:y-800,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               blue_tr[x-800:y-800,160:240]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x-720:y-720,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               blue_tr[x-720:y-720,160:240]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x-640:y-640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               blue_tr[x-640:y-640,160:240]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               blue_tr[x-560:y-560,160:240]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               blue_tr[x-480:y-480,160:240]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               blue_tr[x-400:y-400,160:240]=xor_image9[0:80,0:80]
               return blue_tr    

def blue_xor15(x,y,blue_ch,blue_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-1120:y-1120,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               blue_tr[x-1120:y-1120,80:160]=xor_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-1040:y-1040,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               blue_tr[x-1040:y-1040,80:160]=xor_image2[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-960:y-960,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               blue_tr[x-960:y-960,80:160]=xor_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x-880:y-880,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               blue_tr[x-880:y-880,80:160]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x-800:y-800,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               blue_tr[x-800:y-800,80:160]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x-720:y-720,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               blue_tr[x-720:y-720,80:160]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x-640:y-640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               blue_tr[x-640:y-640,80:160]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               blue_tr[x-560:y-560,80:160]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               blue_tr[x-480:y-480,80:160]=xor_image9[0:80,0:80]
               return blue_tr    

def blue_xor16(x,y,blue_ch,blue_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-1200:y-1200,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               blue_tr[x-1200:y-1200,0:80]=xor_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-1120:y-1120,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               blue_tr[x-1120:y-1120,0:80]=xor_image2[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-1040:y-1040,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               blue_tr[x-1040:y-1040,0:80]=xor_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x-960:y-960,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               blue_tr[x-960:y-960,0:80]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x-880:y-880,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               blue_tr[x-880:y-880,0:80]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x-800:y-800,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               blue_tr[x-800:y-800,0:80]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x-720:y-720,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               blue_tr[x-720:y-720,0:80]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x-640:y-640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               blue_tr[x-640:y-640,0:80]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               blue_tr[x-560:y-560,0:80]=xor_image9[0:80,0:80]
               return blue_tr
#Green channel
def green_xor1(x,y,green_ch,green_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               
               rc_image1[0:80,0:80]=green_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               green_tr[x:y,x+1200:y+1200]=xor_image1[0:80,0:80]
               #print("Green channel traspose:",green_tr)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x+80:y+80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               green_tr[x+80:y+80,1200:1280]=xor_image2[0:80,0:80]
               #print("Green channel:",green_tr)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x+160:y+160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]

               #print("After encryption+row column transpose",xor_image)
               green_tr[x+160:y+160,1200:1280]=xor_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x+240:y+240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               green_tr[x+240:y+240,1200:1280]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x+320:y+320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               green_tr[x+320:y+320,1200:1280]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x+400:y+400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               green_tr[x+400:y+400,1200:1280]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x+480:y+480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               green_tr[x+480:y+480,1200:1280]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x+560:y+560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               green_tr[x+560:y+560,1200:1280]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x+640:y+640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               green_tr[x+640:y+640,1200:1280]=xor_image9[0:80,0:80]
               
               return green_tr
               
def green_xor2(x,y,green_ch,green_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               green_tr[x-80:y-80,1120:1200]=xor_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               green_tr[x:y,1120:1200]=xor_image2[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x+80:y+80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               green_tr[x+80:y+80,1120:1200]=xor_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x+160:y+160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               green_tr[x+160:y+160,1120:1200]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x+240:y+240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               green_tr[x+240:y+240,1120:1200]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x+320:y+320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               green_tr[x+320:y+320,1120:1200]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x+400:y+400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               green_tr[x+400:y+400,1120:1200]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x+480:y+480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               green_tr[x+480:y+480,1120:1200]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x+560:y+560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               green_tr[x+560:y+560,1120:1200]=xor_image9[0:80,0:80]
               return green_tr

def green_xor3(x,y,green_ch,green_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               green_tr[x-160:y-160,1040:1120]=xor_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               green_tr[x-80:y-80,1040:1120]=xor_image2[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               green_tr[x:y,1040:1120]=xor_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x+80:y+80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               green_tr[x+80:y+80,1040:1120]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x+160:y+160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               green_tr[x+160:y+160,1040:1120]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x+240:y+240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               green_tr[x+240:y+240,1040:1120]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x+320:y+320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               green_tr[x+320:y+320,1040:1120]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x+400:y+400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               green_tr[x+400:y+400,1040:1120]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x+480:y+480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               green_tr[x+480:y+480,1040:1120]=xor_image9[0:80,0:80]
               return green_tr              

def green_xor4(x,y,green_ch,green_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               green_tr[x-240:y-240,960:1040]=xor_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               green_tr[x-160:y-160,960:1040]=xor_image2[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               green_tr[x-80:y-80,960:1040]=xor_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               green_tr[x:y,960:1040]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x+80:y+80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               green_tr[x+80:y+80,960:1040]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x+160:y+160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               green_tr[x+160:y+160,960:1040]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x+240:y+240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               green_tr[x+240:y+240,960:1040]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x+320:y+320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               green_tr[x+320:y+320,960:1040]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x+400:y+400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               green_tr[x+400:y+400,960:1040]=xor_image9[0:80,0:80]
               return green_tr              

def green_xor5(x,y,green_ch,green_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               green_tr[x-320:y-320,880:960]=xor_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               green_tr[x-240:y-240,880:960]=xor_image2[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               green_tr[x-160:y-160,880:960]=xor_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               green_tr[x-80:y-80,880:960]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               green_tr[x:y,880:960]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x+80:y+80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               green_tr[x+80:y+80,880:960]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x+160:y+160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               green_tr[x+160:y+160,880:960]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x+240:y+240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               green_tr[x+240:y+240,880:960]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x+320:y+320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               green_tr[x+320:y+320,880:960]=xor_image9[0:80,0:80]
               return green_tr              

def green_xor6(x,y,green_ch,green_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               green_tr[x-400:y-400,800:880]=xor_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               green_tr[x-320:y-320,800:880]=xor_image2[0:80,0:80]
               print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               green_tr[x-240:y-240,800:880]=xor_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               green_tr[x-160:y-160,800:880]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               green_tr[x-80:y-80,800:880]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               green_tr[x:y,800:880]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x+80:y+80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               green_tr[x+80:y+80,800:880]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x+160:y+160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               green_tr[x+160:y+160,800:880]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x+240:y+240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               green_tr[x+240:y+240,800:880]=xor_image9[0:80,0:80]
               return green_tr              

def green_xor7(x,y,green_ch,green_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               green_tr[x-480:y-480,720:800]=xor_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               green_tr[x-400:y-400,720:800]=xor_image2[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               green_tr[x-320:y-320,720:800]=xor_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               green_tr[x-240:y-240,720:800]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               green_tr[x-160:y-160,720:800]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               green_tr[x-80:y-80,720:800]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               green_tr[x:y,720:800]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x+80:y+80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               green_tr[x+80:y+80,720:800]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x+160:y+160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               green_tr[x+160:y+160,720:800]=xor_image9[0:80,0:80]
               return green_tr              

def green_xor8(x,y,green_ch,green_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               green_tr[x-560:y-560,640:720]=xor_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               #print("After encryption+row column transpose",xor_image)
               green_tr[x-480:y-480,640:720]=xor_image2[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               #print("After encryption+row column transpose",xor_image)
               green_tr[x-400:y-400,640:720]=xor_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               #print("After encryption+row column transpose",xor_image)
               green_tr[x-320:y-320,640:720]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               green_tr[x-240:y-240,640:720]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               #print("After encryption+row column transpose",xor_image)
               green_tr[x-160:y-160,640:720]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               #print("After encryption+row column transpose",xor_image)
               green_tr[x-80:y-80,640:720]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               green_tr[x:y,640:720]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x+80:y+80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               green_tr[x+80:y+80,640:720]=xor_image9[0:80,0:80]
               return green_tr
            
def green_xor9(x,y,green_ch,green_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-640:y-640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               green_tr[x-640:y-640,560:640]=xor_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               #print("After encryption+row column transpose",xor_image)
               green_tr[x-560:y-560,560:640]=xor_image2[0:80,0:80]
               print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               #print("After encryption+row column transpose",xor_image)
               green_tr[x-480:y-480,560:640]=xor_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               green_tr[x-400:y-400,560:640]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               green_tr[x-320:y-320,560:640]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               #print("After encryption+row column transpose",xor_image)
               green_tr[x-240:y-240,560:640]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               green_tr[x-160:y-160,560:640]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               green_tr[x-80:y-80,560:640]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               green_tr[x:y,560:640]=xor_image9[0:80,0:80]
               return green_tr             

def green_xor10(x,y,green_ch,green_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-720:y-720,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               green_tr[x-720:y-720,480:560]=xor_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-640:y-640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               green_tr[x-640:y-640,480:560]=xor_image2[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               green_tr[x-560:y-560,480:560]=xor_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               green_tr[x-480:y-480,480:560]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               green_tr[x-400:y-400,480:560]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               green_tr[x-320:y-320,480:560]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               green_tr[x-240:y-240,480:560]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               green_tr[x-160:y-160,480:560]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               green_tr[x-80:y-80,480:560]=xor_image9[0:80,0:80]
               return green_tr             

def green_xor11(x,y,green_ch,green_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-800:y-800,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               green_tr[x-800:y-800,400:480]=xor_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-720:y-720,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               green_tr[x-720:y-720,400:480]=xor_image2[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-640:y-640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               green_tr[x-640:y-640,400:480]=xor_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               green_tr[x-560:y-560,400:480]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               green_tr[x-480:y-480,400:480]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               green_tr[x-400:y-400,400:480]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               green_tr[x-320:y-320,400:480]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               green_tr[x-240:y-240,400:480]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               green_tr[x-160:y-160,400:480]=xor_image9[0:80,0:80]
               return green_tr              

def green_xor12(x,y,green_ch,green_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-880:y-880,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               green_tr[x-880:y-880,320:400]=xor_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-800:y-800,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               green_tr[x-800:y-800,320:400]=xor_image2[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-720:y-720,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               green_tr[x-720:y-720,320:400]=xor_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x-640:y-640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               green_tr[x-640:y-640,320:400]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               green_tr[x-560:y-560,320:400]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               green_tr[x-480:y-480,320:400]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               green_tr[x-400:y-400,320:400]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               green_tr[x-320:y-320,320:400]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               green_tr[x-240:y-240,320:400]=xor_image9[0:80,0:80]
               return green_tr              

def green_xor13(x,y,green_ch,green_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-960:y-960,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               green_tr[x-960:y-960,240:320]=xor_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-880:y-880,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               
               green_tr[x-880:y-880,240:320]=xor_image2[0:80,0:80]
               print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-800:y-800,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               green_tr[x-800:y-800,240:320]=xor_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x-720:y-720,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               green_tr[x-720:y-720,240:320]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x-640:y-640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               green_tr[x-640:y-640,240:320]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               green_tr[x-560:y-560,240:320]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               green_tr[x-480:y-480,240:320]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               green_tr[x-400:y-400,240:320]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               green_tr[x-320:y-320,240:320]=xor_image9[0:80,0:80]
               return green_tr    

def green_xor14(x,y,green_ch,green_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-1040:y-1040,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
                   
               green_tr[x-1040:y-1040,160:240]=xor_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-960:y-960,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               green_tr[x-960:y-960,160:240]=xor_image2[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-880:y-880,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               green_tr[x-880:y-880,160:240]=xor_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x-800:y-800,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               green_tr[x-800:y-800,160:240]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x-720:y-720,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               green_tr[x-720:y-720,160:240]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x-640:y-640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               green_tr[x-640:y-640,160:240]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               green_tr[x-560:y-560,160:240]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               green_tr[x-480:y-480,160:240]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               green_tr[x-400:y-400,160:240]=xor_image9[0:80,0:80]
               return green_tr    

def green_xor15(x,y,green_ch,green_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-1120:y-1120,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               green_tr[x-1120:y-1120,80:160]=xor_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-1040:y-1040,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               green_tr[x-1040:y-1040,80:160]=xor_image2[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-960:y-960,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               green_tr[x-960:y-960,80:160]=xor_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x-880:y-880,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               green_tr[x-880:y-880,80:160]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x-800:y-800,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               green_tr[x-800:y-800,80:160]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x-720:y-720,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               green_tr[x-720:y-720,80:160]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x-640:y-640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               green_tr[x-640:y-640,80:160]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               green_tr[x-560:y-560,80:160]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               green_tr[x-480:y-480,80:160]=xor_image9[0:80,0:80]
               return green_tr    

def green_xor16(x,y,green_ch,green_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-1200:y-1200,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               green_tr[x-1200:y-1200,0:80]=xor_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-1120:y-1120,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               green_tr[x-1120:y-1120,0:80]=xor_image2[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-1040:y-1040,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               green_tr[x-1040:y-1040,0:80]=xor_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x-960:y-960,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               green_tr[x-960:y-960,0:80]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x-880:y-880,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               green_tr[x-880:y-880,0:80]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x-800:y-800,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               green_tr[x-800:y-800,0:80]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x-720:y-720,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               green_tr[x-720:y-720,0:80]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x-640:y-640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               green_tr[x-640:y-640,0:80]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               green_tr[x-560:y-560,0:80]=xor_image9[0:80,0:80]
               return green_tr            
#Red channel
def red_xor1(x,y,red_ch,red_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               
               rc_image1[0:80,0:80]=red_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               red_tr[x:y,x+1200:y+1200]=xor_image1[0:80,0:80]
               #print("Green channel traspose:",red_tr)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x+80:y+80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               red_tr[x+80:y+80,1200:1280]=xor_image2[0:80,0:80]
               #print("Green channel:",red_tr)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x+160:y+160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]

               #print("After encryption+row column transpose",xor_image)
               red_tr[x+160:y+160,1200:1280]=xor_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x+240:y+240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               red_tr[x+240:y+240,1200:1280]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x+320:y+320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               red_tr[x+320:y+320,1200:1280]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x+400:y+400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               red_tr[x+400:y+400,1200:1280]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x+480:y+480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               red_tr[x+480:y+480,1200:1280]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x+560:y+560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               red_tr[x+560:y+560,1200:1280]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x+640:y+640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               red_tr[x+640:y+640,1200:1280]=xor_image9[0:80,0:80]
               
               return red_tr
               
def red_xor2(x,y,red_ch,red_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               red_tr[x-80:y-80,1120:1200]=xor_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               red_tr[x:y,1120:1200]=xor_image2[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x+80:y+80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               red_tr[x+80:y+80,1120:1200]=xor_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x+160:y+160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               red_tr[x+160:y+160,1120:1200]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x+240:y+240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               red_tr[x+240:y+240,1120:1200]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x+320:y+320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               red_tr[x+320:y+320,1120:1200]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x+400:y+400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               red_tr[x+400:y+400,1120:1200]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x+480:y+480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               red_tr[x+480:y+480,1120:1200]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x+560:y+560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               red_tr[x+560:y+560,1120:1200]=xor_image9[0:80,0:80]
               return red_tr

def red_xor3(x,y,red_ch,red_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               red_tr[x-160:y-160,1040:1120]=xor_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               red_tr[x-80:y-80,1040:1120]=xor_image2[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               red_tr[x:y,1040:1120]=xor_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x+80:y+80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               red_tr[x+80:y+80,1040:1120]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x+160:y+160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               red_tr[x+160:y+160,1040:1120]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x+240:y+240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               red_tr[x+240:y+240,1040:1120]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x+320:y+320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               red_tr[x+320:y+320,1040:1120]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x+400:y+400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               red_tr[x+400:y+400,1040:1120]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x+480:y+480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               red_tr[x+480:y+480,1040:1120]=xor_image9[0:80,0:80]
               return red_tr              

def red_xor4(x,y,red_ch,red_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               red_tr[x-240:y-240,960:1040]=xor_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               red_tr[x-160:y-160,960:1040]=xor_image2[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               red_tr[x-80:y-80,960:1040]=xor_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               red_tr[x:y,960:1040]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x+80:y+80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               red_tr[x+80:y+80,960:1040]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x+160:y+160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               red_tr[x+160:y+160,960:1040]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x+240:y+240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               red_tr[x+240:y+240,960:1040]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x+320:y+320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               red_tr[x+320:y+320,960:1040]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x+400:y+400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               red_tr[x+400:y+400,960:1040]=xor_image9[0:80,0:80]
               return red_tr              

def red_xor5(x,y,red_ch,red_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               red_tr[x-320:y-320,880:960]=xor_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               red_tr[x-240:y-240,880:960]=xor_image2[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               red_tr[x-160:y-160,880:960]=xor_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               red_tr[x-80:y-80,880:960]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               red_tr[x:y,880:960]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x+80:y+80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               red_tr[x+80:y+80,880:960]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x+160:y+160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               red_tr[x+160:y+160,880:960]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x+240:y+240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               red_tr[x+240:y+240,880:960]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x+320:y+320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               red_tr[x+320:y+320,880:960]=xor_image9[0:80,0:80]
               return red_tr              

def red_xor6(x,y,red_ch,red_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               red_tr[x-400:y-400,800:880]=xor_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               red_tr[x-320:y-320,800:880]=xor_image2[0:80,0:80]
               print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               red_tr[x-240:y-240,800:880]=xor_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               red_tr[x-160:y-160,800:880]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               red_tr[x-80:y-80,800:880]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               red_tr[x:y,800:880]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x+80:y+80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               red_tr[x+80:y+80,800:880]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x+160:y+160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               red_tr[x+160:y+160,800:880]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x+240:y+240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               red_tr[x+240:y+240,800:880]=xor_image9[0:80,0:80]
               return red_tr              

def red_xor7(x,y,red_ch,red_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               red_tr[x-480:y-480,720:800]=xor_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               red_tr[x-400:y-400,720:800]=xor_image2[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               red_tr[x-320:y-320,720:800]=xor_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               red_tr[x-240:y-240,720:800]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               red_tr[x-160:y-160,720:800]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               red_tr[x-80:y-80,720:800]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               red_tr[x:y,720:800]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x+80:y+80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               red_tr[x+80:y+80,720:800]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x+160:y+160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               red_tr[x+160:y+160,720:800]=xor_image9[0:80,0:80]
               return red_tr              

def red_xor8(x,y,red_ch,red_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               red_tr[x-560:y-560,640:720]=xor_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               #print("After encryption+row column transpose",xor_image)
               red_tr[x-480:y-480,640:720]=xor_image2[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               #print("After encryption+row column transpose",xor_image)
               red_tr[x-400:y-400,640:720]=xor_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               #print("After encryption+row column transpose",xor_image)
               red_tr[x-320:y-320,640:720]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               red_tr[x-240:y-240,640:720]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               #print("After encryption+row column transpose",xor_image)
               red_tr[x-160:y-160,640:720]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               #print("After encryption+row column transpose",xor_image)
               red_tr[x-80:y-80,640:720]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               red_tr[x:y,640:720]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x+80:y+80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               red_tr[x+80:y+80,640:720]=xor_image9[0:80,0:80]
               return red_tr
            
def red_xor9(x,y,red_ch,red_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-640:y-640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               red_tr[x-640:y-640,560:640]=xor_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               #print("After encryption+row column transpose",xor_image)
               red_tr[x-560:y-560,560:640]=xor_image2[0:80,0:80]
               print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               #print("After encryption+row column transpose",xor_image)
               red_tr[x-480:y-480,560:640]=xor_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               red_tr[x-400:y-400,560:640]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               red_tr[x-320:y-320,560:640]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               #print("After encryption+row column transpose",xor_image)
               red_tr[x-240:y-240,560:640]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               red_tr[x-160:y-160,560:640]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               red_tr[x-80:y-80,560:640]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x:y,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               red_tr[x:y,560:640]=xor_image9[0:80,0:80]
               return red_tr             

def red_xor10(x,y,red_ch,red_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-720:y-720,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               red_tr[x-720:y-720,480:560]=xor_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-640:y-640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               red_tr[x-640:y-640,480:560]=xor_image2[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               red_tr[x-560:y-560,480:560]=xor_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               red_tr[x-480:y-480,480:560]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               red_tr[x-400:y-400,480:560]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               red_tr[x-320:y-320,480:560]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               red_tr[x-240:y-240,480:560]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               red_tr[x-160:y-160,480:560]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x-80:y-80,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               red_tr[x-80:y-80,480:560]=xor_image9[0:80,0:80]
               return red_tr             

def red_xor11(x,y,red_ch,red_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-800:y-800,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               red_tr[x-800:y-800,400:480]=xor_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-720:y-720,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               red_tr[x-720:y-720,400:480]=xor_image2[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-640:y-640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               red_tr[x-640:y-640,400:480]=xor_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               red_tr[x-560:y-560,400:480]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               red_tr[x-480:y-480,400:480]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               red_tr[x-400:y-400,400:480]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               red_tr[x-320:y-320,400:480]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               red_tr[x-240:y-240,400:480]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x-160:y-160,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               red_tr[x-160:y-160,400:480]=xor_image9[0:80,0:80]
               return red_tr              

def red_xor12(x,y,red_ch,red_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-880:y-880,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               red_tr[x-880:y-880,320:400]=xor_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-800:y-800,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               red_tr[x-800:y-800,320:400]=xor_image2[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-720:y-720,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               red_tr[x-720:y-720,320:400]=xor_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x-640:y-640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               red_tr[x-640:y-640,320:400]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               red_tr[x-560:y-560,320:400]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               red_tr[x-480:y-480,320:400]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               red_tr[x-400:y-400,320:400]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               red_tr[x-320:y-320,320:400]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x-240:y-240,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               red_tr[x-240:y-240,320:400]=xor_image9[0:80,0:80]
               return red_tr              

def red_xor13(x,y,red_ch,red_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-960:y-960,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               red_tr[x-960:y-960,240:320]=xor_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-880:y-880,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               
               red_tr[x-880:y-880,240:320]=xor_image2[0:80,0:80]
               print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-800:y-800,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               red_tr[x-800:y-800,240:320]=xor_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x-720:y-720,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               red_tr[x-720:y-720,240:320]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x-640:y-640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               red_tr[x-640:y-640,240:320]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               red_tr[x-560:y-560,240:320]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               red_tr[x-480:y-480,240:320]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               red_tr[x-400:y-400,240:320]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x-320:y-320,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               red_tr[x-320:y-320,240:320]=xor_image9[0:80,0:80]
               return red_tr    

def red_xor14(x,y,red_ch,red_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-1040:y-1040,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
                   
               red_tr[x-1040:y-1040,160:240]=xor_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-960:y-960,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               red_tr[x-960:y-960,160:240]=xor_image2[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-880:y-880,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               red_tr[x-880:y-880,160:240]=xor_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x-800:y-800,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               red_tr[x-800:y-800,160:240]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x-720:y-720,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               red_tr[x-720:y-720,160:240]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x-640:y-640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               red_tr[x-640:y-640,160:240]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               red_tr[x-560:y-560,160:240]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               red_tr[x-480:y-480,160:240]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x-400:y-400,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               red_tr[x-400:y-400,160:240]=xor_image9[0:80,0:80]
               return red_tr    

def red_xor15(x,y,red_ch,red_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-1120:y-1120,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               red_tr[x-1120:y-1120,80:160]=xor_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-1040:y-1040,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               red_tr[x-1040:y-1040,80:160]=xor_image2[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-960:y-960,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               red_tr[x-960:y-960,80:160]=xor_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x-880:y-880,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               red_tr[x-880:y-880,80:160]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x-800:y-800,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               red_tr[x-800:y-800,80:160]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x-720:y-720,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               red_tr[x-720:y-720,80:160]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x-640:y-640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               red_tr[x-640:y-640,80:160]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               red_tr[x-560:y-560,80:160]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x-480:y-480,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               red_tr[x-480:y-480,80:160]=xor_image9[0:80,0:80]
               return red_tr    

def red_xor16(x,y,red_ch,red_tr,key2):
               rc_image1=np.zeros((80, 80), np.uint8)
               xor_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-1200:y-1200,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image1[row,col]=rc_image1[row,col]^key2[row,col]
               red_tr[x-1200:y-1200,0:80]=xor_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",xor_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               xor_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-1120:y-1120,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image2[row,col]=rc_image2[row,col]^key2[row,col]
               red_tr[x-1120:y-1120,0:80]=xor_image2[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               xor_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-1040:y-1040,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image3[row,col]=rc_image3[row,col]^key2[row,col]
               red_tr[x-1040:y-1040,0:80]=xor_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               xor_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x-960:y-960,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image4[row,col]=rc_image4[row,col]^key2[row,col]
               red_tr[x-960:y-960,0:80]=xor_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               xor_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x-880:y-880,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image5[row,col]=rc_image5[row,col]^key2[row,col]
               red_tr[x-880:y-880,0:80]=xor_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               xor_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x-800:y-800,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image6[row,col]=rc_image6[row,col]^key2[row,col]
               red_tr[x-800:y-800,0:80]=xor_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               xor_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x-720:y-720,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image7[row,col]=rc_image7[row,col]^key2[row,col]
               red_tr[x-720:y-720,0:80]=xor_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               xor_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x-640:y-640,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image8[row,col]=rc_image8[row,col]^key2[row,col]
               red_tr[x-640:y-640,0:80]=xor_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               xor_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x-560:y-560,x:y]
               for row in range(80):
                   for col in range(80):
                       xor_image9[row,col]=rc_image9[row,col]^key2[row,col]
               red_tr[x-560:y-560,0:80]=xor_image9[0:80,0:80]
               return red_tr            


r=720
c=1280
t=3
'''enc_start=0
enc_end=0
dec_start=0
dec_end=0'''
pathIn1="G:/impl/linux_backup/enc_rc_keypos_rgb_frames_l2/"
files1 = [f for f in os.listdir(pathIn1) if os.path.isfile(os.path.join(pathIn1, f))]
files1.sort(key=lambda x: int(x[5:-4]))
key=random.randint(256,size=(80,80))
#print(key2)
np.save('keycol_rc_rgb_frames_l3',key)
key1=np.load('keycol_rc_rgb_frames_l3.npy')


for i in range(len(files1)):
    j=files1[i]
    
    frame_no=int(j[5:-4])
    filename=pathIn1+files1[i]
    img=cv2.imread(filename,cv2.IMREAD_UNCHANGED)


    bluech=img[:,:,0]
    greench=img[:,:,1]
    redch=img[:,:,2]

    bluetr=np.zeros((r, c), np.uint8)
    greentr=np.zeros((r, c), np.uint8)
    redtr=np.zeros((r, c), np.uint8)
    

 
    #Blue Channel
    
    blue_xor_img1=blue_xor1(0,80,bluech,bluetr,key1)
    #print("xor image1:",blue_xor_img1)
    blue_xor_img16=blue_xor16(1200,1280,bluech,bluetr,key1)
    blue_xor_img2=blue_xor2(80,160,bluech,bluetr,key1)
    blue_xor_img15=blue_xor15(1120,1200,bluech,bluetr,key1)
    blue_xor_img3=blue_xor3(160,240,bluech,bluetr,key1)
    blue_xor_img14=blue_xor14(1040,1120,bluech,bluetr,key1)
    blue_xor_img4=blue_xor4(240,320,bluech,bluetr,key1)
    blue_xor_img13=blue_xor13(960,1040,bluech,bluetr,key1)
    blue_xor_img5=blue_xor5(320,400,bluech,bluetr,key1)
    blue_xor_img12=blue_xor12(880,960,bluech,bluetr,key1)
    blue_xor_img6=blue_xor6(400,480,bluech,bluetr,key1)
    blue_xor_img11=blue_xor11(800,880,bluech,bluetr,key1)
    blue_xor_img7=blue_xor7(480,560,bluech,bluetr,key1)
    blue_xor_img10=blue_xor10(720,800,bluech,bluetr,key1)
    blue_xor_img8=blue_xor8(560,640,bluech,bluetr,key1)
    blue_xor_img9=blue_xor9(640,720,bluech,bluetr,key1)
    
    #Green Channel
    green_xor_img1=green_xor1(0,80,greench,greentr,key1)
    #print("xor image1:",green_xor_img1)
    green_xor_img16=green_xor16(1200,1280,greench,greentr,key1)
    green_xor_img2=green_xor2(80,160,greench,greentr,key1)
    green_xor_img15=green_xor15(1120,1200,greench,greentr,key1)
    green_xor_img3=green_xor3(160,240,greench,greentr,key1)
    green_xor_img14=green_xor14(1040,1120,greench,greentr,key1)
    green_xor_img4=green_xor4(240,320,greench,greentr,key1)
    green_xor_img13=green_xor13(960,1040,greench,greentr,key1)
    green_xor_img5=green_xor5(320,400,greench,greentr,key1)
    green_xor_img12=green_xor12(880,960,greench,greentr,key1)
    green_xor_img6=green_xor6(400,480,greench,greentr,key1)
    green_xor_img11=green_xor11(800,880,greench,greentr,key1)
    green_xor_img7=green_xor7(480,560,greench,greentr,key1)
    green_xor_img10=green_xor10(720,800,greench,greentr,key1)
    green_xor_img8=green_xor8(560,640,greench,greentr,key1)
    green_xor_img9=green_xor9(640,720,greench,greentr,key1)
    
    #Red Channel
    red_xor_img1=red_xor1(0,80,redch,redtr,key1)
    #print("xor image1:",red_xor_img1)
    red_xor_img16=red_xor16(1200,1280,redch,redtr,key1)
    red_xor_img2=red_xor2(80,160,redch,redtr,key1)
    red_xor_img15=red_xor15(1120,1200,redch,redtr,key1)
    red_xor_img3=red_xor3(160,240,redch,redtr,key1)
    red_xor_img14=red_xor14(1040,1120,redch,redtr,key1)
    red_xor_img4=red_xor4(240,320,redch,redtr,key1)
    red_xor_img13=red_xor13(960,1040,redch,redtr,key1)
    red_xor_img5=red_xor5(320,400,redch,redtr,key1)
    red_xor_img12=red_xor12(880,960,redch,redtr,key1)
    red_xor_img6=red_xor6(400,480,redch,redtr,key1)
    red_xor_img11=red_xor11(800,880,redch,redtr,key1)
    red_xor_img7=red_xor7(480,560,redch,redtr,key1)
    red_xor_img10=red_xor10(720,800,redch,redtr,key1)
    red_xor_img8=red_xor8(560,640,redch,redtr,key1)
    red_xor_img9=red_xor9(640,720,redch,redtr,key1)






    for row in range(720):
        for col in range(1280):
            #Blue
            img[row][col][0]=blue_xor_img1[row][col]
            img[row][col][0]=blue_xor_img2[row][col]
            img[row][col][0]=blue_xor_img3[row][col]
            img[row][col][0]=blue_xor_img4[row][col]
            img[row][col][0]=blue_xor_img5[row][col]
            img[row][col][0]=blue_xor_img6[row][col]
            img[row][col][0]=blue_xor_img7[row][col]
            img[row][col][0]=blue_xor_img8[row][col]
            img[row][col][0]=blue_xor_img9[row][col]
            img[row][col][0]=blue_xor_img10[row][col]
            img[row][col][0]=blue_xor_img11[row][col]
            img[row][col][0]=blue_xor_img12[row][col]
            img[row][col][0]=blue_xor_img13[row][col]
            img[row][col][0]=blue_xor_img14[row][col]
            img[row][col][0]=blue_xor_img15[row][col]
            img[row][col][0]=blue_xor_img16[row][col]
            #green
            img[row][col][1]=green_xor_img1[row][col]
            img[row][col][1]=green_xor_img2[row][col]
            img[row][col][1]=green_xor_img3[row][col]
            img[row][col][1]=green_xor_img4[row][col]
            img[row][col][1]=green_xor_img5[row][col]
            img[row][col][1]=green_xor_img6[row][col]
            img[row][col][1]=green_xor_img7[row][col]
            img[row][col][1]=green_xor_img8[row][col]
            img[row][col][1]=green_xor_img9[row][col]
            img[row][col][1]=green_xor_img10[row][col]
            img[row][col][1]=green_xor_img11[row][col]
            img[row][col][1]=green_xor_img12[row][col]
            img[row][col][1]=green_xor_img13[row][col]
            img[row][col][1]=green_xor_img14[row][col]
            img[row][col][1]=green_xor_img15[row][col]
            img[row][col][1]=green_xor_img16[row][col]
            #Red
            img[row][col][2]=red_xor_img1[row][col]
            img[row][col][2]=red_xor_img2[row][col]
            img[row][col][2]=red_xor_img3[row][col]
            img[row][col][2]=red_xor_img4[row][col]
            img[row][col][2]=red_xor_img5[row][col]
            img[row][col][2]=red_xor_img6[row][col]
            img[row][col][2]=red_xor_img7[row][col]
            img[row][col][2]=red_xor_img8[row][col]
            img[row][col][2]=red_xor_img9[row][col]
            img[row][col][2]=red_xor_img10[row][col]
            img[row][col][2]=red_xor_img11[row][col]
            img[row][col][2]=red_xor_img12[row][col]
            img[row][col][2]=red_xor_img13[row][col]
            img[row][col][2]=red_xor_img14[row][col]
            img[row][col][2]=red_xor_img15[row][col]
            img[row][col][2]=red_xor_img16[row][col]


    cv2.imwrite("G:/impl/linux_backup/enc_rc_keypos_rgb_frames_l3/frame%d.png" %frame_no,img)
    print("End")



