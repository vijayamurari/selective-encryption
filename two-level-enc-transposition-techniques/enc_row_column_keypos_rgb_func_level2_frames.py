import cv2
import numpy as np
from numpy import random
import random as rd
import os
import time

#Blue Channel
def blue_permutation1(x,y,blue_ch,blue_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               
               rc_image1[0:80,0:80]=blue_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               blue_tr[x:y,x+1200:y+1200]=transpose_image1[0:80,0:80]
               #print("Green channel traspose:",blue_tr)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x+80:y+80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+80:y+80,1200:1280]=transpose_image2[0:80,0:80]
               #print("Green channel:",blue_tr)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x+160:y+160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for g in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,g]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[g,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+160:y+160,1200:1280]=transpose_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x+240:y+240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for h in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,h]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[h,0:80]
                   #transpose_image4[0:80,h]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+240:y+240,1200:1280]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x+320:y+320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for i in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,i]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[i,0:80]
                   #transpose_image5[0:80,i]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               blue_tr[x+320:y+320,1200:1280]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x+400:y+400,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for j in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,j]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[j,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+400:y+400,1200:1280]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x+480:y+480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+480:y+480,1200:1280]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x+560:y+560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+560:y+560,1200:1280]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x+640:y+640,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+640:y+640,1200:1280]=transpose_image9[0:80,0:80]
               print("blue_tr:",blue_tr)
               return blue_tr
               
               
def blue_permutation2(x,y,blue_ch,blue_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               blue_tr[x-80:y-80,1120:1200]=transpose_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x:y,1120:1200]=transpose_image2[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x+80:y+80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+80:y+80,1120:1200]=transpose_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x+160:y+160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+160:y+160,1120:1200]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x+240:y+240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               blue_tr[x+240:y+240,1120:1200]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x+320:y+320,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+320:y+320,1120:1200]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x+400:y+400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+400:y+400,1120:1200]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x+480:y+480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+480:y+480,1120:1200]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x+560:y+560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+560:y+560,1120:1200]=transpose_image9[0:80,0:80]
               return blue_tr


def blue_permutation3(x,y,blue_ch,blue_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               blue_tr[x-160:y-160,1040:1120]=transpose_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-80:y-80,1040:1120]=transpose_image2[0:80,0:80]
               print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x:y,1040:1120]=transpose_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x+80:y+80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+80:y+80,1040:1120]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x+160:y+160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               blue_tr[x+160:y+160,1040:1120]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x+240:y+240,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+240:y+240,1040:1120]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x+320:y+320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+320:y+320,1040:1120]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x+400:y+400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+400:y+400,1040:1120]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x+480:y+480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+480:y+480,1040:1120]=transpose_image9[0:80,0:80]
               return blue_tr              


def blue_permutation4(x,y,blue_ch,blue_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               blue_tr[x-240:y-240,960:1040]=transpose_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-160:y-160,960:1040]=transpose_image2[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-80:y-80,960:1040]=transpose_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x:y,960:1040]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x+80:y+80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               blue_tr[x+80:y+80,960:1040]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x+160:y+160,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+160:y+160,960:1040]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x+240:y+240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+240:y+240,960:1040]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x+320:y+320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+320:y+320,960:1040]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x+400:y+400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   row_data=rc_image9[f,0:80]
                   transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+400:y+400,960:1040]=transpose_image9[0:80,0:80]
               return blue_tr              
   

def blue_permutation5(x,y,blue_ch,blue_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               blue_tr[x-320:y-320,880:960]=transpose_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-240:y-240,880:960]=transpose_image2[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-160:y-160,880:960]=transpose_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-80:y-80,880:960]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               blue_tr[x:y,880:960]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x+80:y+80,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+80:y+80,880:960]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x+160:y+160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+160:y+160,880:960]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x+240:y+240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+240:y+240,880:960]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x+320:y+320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+320:y+320,880:960]=transpose_image9[0:80,0:80]
               return blue_tr              
   

def blue_permutation6(x,y,blue_ch,blue_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               blue_tr[x-400:y-400,800:880]=transpose_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-320:y-320,800:880]=transpose_image2[0:80,0:80]
               print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-240:y-240,800:880]=transpose_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-160:y-160,800:880]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               blue_tr[x-80:y-80,800:880]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x:y,800:880]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x+80:y+80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+80:y+80,800:880]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x+160:y+160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+160:y+160,800:880]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x+240:y+240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+240:y+240,800:880]=transpose_image9[0:80,0:80]
               return blue_tr              
             

def blue_permutation7(x,y,blue_ch,blue_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               blue_tr[x-480:y-480,720:800]=transpose_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-400:y-400,720:800]=transpose_image2[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-320:y-320,720:800]=transpose_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-240:y-240,720:800]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               blue_tr[x-160:y-160,720:800]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-80:y-80,720:800]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x:y,720:800]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x+80:y+80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+80:y+80,720:800]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x+160:y+160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+160:y+160,720:800]=transpose_image9[0:80,0:80]
               return blue_tr                           

def blue_permutation8(x,y,blue_ch,blue_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               blue_tr[x-560:y-560,640:720]=transpose_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-480:y-480,640:720]=transpose_image2[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-400:y-400,640:720]=transpose_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-320:y-320,640:720]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               blue_tr[x-240:y-240,640:720]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-160:y-160,640:720]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-80:y-80,640:720]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               blue_tr[x:y,640:720]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x+80:y+80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x+80:y+80,640:720]=transpose_image9[0:80,0:80]
               return blue_tr

            
def blue_permutation9(x,y,blue_ch,blue_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-640:y-640,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               blue_tr[x-640:y-640,560:640]=transpose_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-560:y-560,560:640]=transpose_image2[0:80,0:80]
               print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-480:y-480,560:640]=transpose_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-400:y-400,560:640]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               blue_tr[x-320:y-320,560:640]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-240:y-240,560:640]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-160:y-160,560:640]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-80:y-80,560:640]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x:y,560:640]=transpose_image9[0:80,0:80]
               return blue_tr             
       

def blue_permutation10(x,y,blue_ch,blue_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-720:y-720,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               blue_tr[x-720:y-720,480:560]=transpose_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-640:y-640,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-640:y-640,480:560]=transpose_image2[0:80,0:80]
               print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-560:y-560,480:560]=transpose_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-480:y-480,480:560]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               blue_tr[x-400:y-400,480:560]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-320:y-320,480:560]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-240:y-240,480:560]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-160:y-160,480:560]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-80:y-80,480:560]=transpose_image9[0:80,0:80]
               return blue_tr                    

def blue_permutation11(x,y,blue_ch,blue_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-800:y-800,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               blue_tr[x-800:y-800,400:480]=transpose_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-720:y-720,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-720:y-720,400:480]=transpose_image2[0:80,0:80]
               print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-640:y-640,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-640:y-640,400:480]=transpose_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-560:y-560,400:480]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               blue_tr[x-480:y-480,400:480]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-400:y-400,400:480]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-320:y-320,400:480]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-240:y-240,400:480]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-160:y-160,400:480]=transpose_image9[0:80,0:80]
               return blue_tr              

def blue_permutation12(x,y,blue_ch,blue_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-880:y-880,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               blue_tr[x-880:y-880,320:400]=transpose_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-800:y-800,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-800:y-800,320:400]=transpose_image2[0:80,0:80]
               print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-720:y-720,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-720:y-720,320:400]=transpose_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x-640:y-640,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-640:y-640,320:400]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               blue_tr[x-560:y-560,320:400]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-480:y-480,320:400]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-400:y-400,320:400]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-320:y-320,320:400]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-240:y-240,320:400]=transpose_image9[0:80,0:80]
               return blue_tr
            
def blue_permutation13(x,y,blue_ch,blue_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-960:y-960,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               blue_tr[x-960:y-960,240:320]=transpose_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-880:y-880,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-880:y-880,240:320]=transpose_image2[0:80,0:80]
               print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-800:y-800,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-800:y-800,240:320]=transpose_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x-720:y-720,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-720:y-720,240:320]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x-640:y-640,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               blue_tr[x-640:y-640,240:320]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-560:y-560,240:320]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-480:y-480,240:320]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-400:y-400,240:320]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-320:y-320,240:320]=transpose_image9[0:80,0:80]
               return blue_tr    

def blue_permutation14(x,y,blue_ch,blue_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-1040:y-1040,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
                   
               blue_tr[x-1040:y-1040,160:240]=transpose_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-960:y-960,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
                   
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-960:y-960,160:240]=transpose_image2[0:80,0:80]
               print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-880:y-880,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-880:y-880,160:240]=transpose_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x-800:y-800,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-800:y-800,160:240]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x-720:y-720,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               blue_tr[x-720:y-720,160:240]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x-640:y-640,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-640:y-640,160:240]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-560:y-560,160:240]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-480:y-480,160:240]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-400:y-400,160:240]=transpose_image9[0:80,0:80]
               return blue_tr
            
def blue_permutation15(x,y,blue_ch,blue_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-1120:y-1120,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               blue_tr[x-1120:y-1120,80:160]=transpose_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-1040:y-1040,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-1040:y-1040,80:160]=transpose_image2[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-960:y-960,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-960:y-960,80:160]=transpose_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x-880:y-880,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-880:y-880,80:160]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x-800:y-800,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               blue_tr[x-800:y-800,80:160]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x-720:y-720,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-720:y-720,80:160]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x-640:y-640,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-640:y-640,80:160]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-560:y-560,80:160]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-480:y-480,80:160]=transpose_image9[0:80,0:80]
               return blue_tr    


def blue_permutation16(x,y,blue_ch,blue_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=blue_ch[x-1200:y-1200,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               blue_tr[x-1200:y-1200,0:80]=transpose_image1[0:80,0:80]
                #print("Green channel:",blue_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=blue_ch[x-1120:y-1120,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-1120:y-1120,0:80]=transpose_image2[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=blue_ch[x-1040:y-1040,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-1040:y-1040,0:80]=transpose_image3[0:80,0:80]
               #print("Green channel:",blue_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=blue_ch[x-960:y-960,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-960:y-960,0:80]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=blue_ch[x-880:y-880,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               blue_tr[x-880:y-880,0:80]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=blue_ch[x-800:y-800,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-800:y-800,0:80]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=blue_ch[x-720:y-720,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-720:y-720,0:80]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=blue_ch[x-640:y-640,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-640:y-640,0:80]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=blue_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               blue_tr[x-560:y-560,0:80]=transpose_image9[0:80,0:80]
               return blue_tr

            
#Green Channel
def green_permutation1(x,y,green_ch,green_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               
               rc_image1[0:80,0:80]=green_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               green_tr[x:y,x+1200:y+1200]=transpose_image1[0:80,0:80]
               #print("Green channel traspose:",green_tr)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x+80:y+80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+80:y+80,1200:1280]=transpose_image2[0:80,0:80]
               #print("Green channel:",green_tr)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x+160:y+160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for g in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,g]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[g,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+160:y+160,1200:1280]=transpose_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x+240:y+240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for h in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,h]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[h,0:80]
                   #transpose_image4[0:80,h]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+240:y+240,1200:1280]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x+320:y+320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for i in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,i]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[i,0:80]
                   #transpose_image5[0:80,i]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               green_tr[x+320:y+320,1200:1280]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x+400:y+400,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for j in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,j]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[j,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+400:y+400,1200:1280]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x+480:y+480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+480:y+480,1200:1280]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x+560:y+560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               green_tr[x+560:y+560,1200:1280]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x+640:y+640,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+640:y+640,1200:1280]=transpose_image9[0:80,0:80]
               print("green_tr:",green_tr)
               return green_tr
               
               
def green_permutation2(x,y,green_ch,green_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               green_tr[x-80:y-80,1120:1200]=transpose_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x:y,1120:1200]=transpose_image2[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x+80:y+80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+80:y+80,1120:1200]=transpose_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x+160:y+160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+160:y+160,1120:1200]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x+240:y+240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               green_tr[x+240:y+240,1120:1200]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x+320:y+320,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+320:y+320,1120:1200]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x+400:y+400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+400:y+400,1120:1200]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x+480:y+480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               green_tr[x+480:y+480,1120:1200]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x+560:y+560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+560:y+560,1120:1200]=transpose_image9[0:80,0:80]
               return green_tr


def green_permutation3(x,y,green_ch,green_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               green_tr[x-160:y-160,1040:1120]=transpose_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-80:y-80,1040:1120]=transpose_image2[0:80,0:80]
               print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x:y,1040:1120]=transpose_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x+80:y+80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+80:y+80,1040:1120]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x+160:y+160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               green_tr[x+160:y+160,1040:1120]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x+240:y+240,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+240:y+240,1040:1120]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x+320:y+320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+320:y+320,1040:1120]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x+400:y+400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               green_tr[x+400:y+400,1040:1120]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x+480:y+480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+480:y+480,1040:1120]=transpose_image9[0:80,0:80]
               return green_tr              


def green_permutation4(x,y,green_ch,green_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               green_tr[x-240:y-240,960:1040]=transpose_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-160:y-160,960:1040]=transpose_image2[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-80:y-80,960:1040]=transpose_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x:y,960:1040]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x+80:y+80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               green_tr[x+80:y+80,960:1040]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x+160:y+160,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+160:y+160,960:1040]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x+240:y+240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+240:y+240,960:1040]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x+320:y+320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               green_tr[x+320:y+320,960:1040]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x+400:y+400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   row_data=rc_image9[f,0:80]
                   transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+400:y+400,960:1040]=transpose_image9[0:80,0:80]
               return green_tr              
   

def green_permutation5(x,y,green_ch,green_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               green_tr[x-320:y-320,880:960]=transpose_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-240:y-240,880:960]=transpose_image2[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-160:y-160,880:960]=transpose_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-80:y-80,880:960]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               green_tr[x:y,880:960]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x+80:y+80,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+80:y+80,880:960]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x+160:y+160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+160:y+160,880:960]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x+240:y+240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               green_tr[x+240:y+240,880:960]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x+320:y+320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+320:y+320,880:960]=transpose_image9[0:80,0:80]
               return green_tr              
   

def green_permutation6(x,y,green_ch,green_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               green_tr[x-400:y-400,800:880]=transpose_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-320:y-320,800:880]=transpose_image2[0:80,0:80]
               print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-240:y-240,800:880]=transpose_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-160:y-160,800:880]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               green_tr[x-80:y-80,800:880]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x:y,800:880]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x+80:y+80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+80:y+80,800:880]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x+160:y+160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               green_tr[x+160:y+160,800:880]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x+240:y+240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+240:y+240,800:880]=transpose_image9[0:80,0:80]
               return green_tr              
             

def green_permutation7(x,y,green_ch,green_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               green_tr[x-480:y-480,720:800]=transpose_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-400:y-400,720:800]=transpose_image2[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-320:y-320,720:800]=transpose_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-240:y-240,720:800]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               green_tr[x-160:y-160,720:800]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-80:y-80,720:800]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x:y,720:800]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x+80:y+80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               green_tr[x+80:y+80,720:800]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x+160:y+160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+160:y+160,720:800]=transpose_image9[0:80,0:80]
               return green_tr                           

def green_permutation8(x,y,green_ch,green_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               green_tr[x-560:y-560,640:720]=transpose_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-480:y-480,640:720]=transpose_image2[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-400:y-400,640:720]=transpose_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-320:y-320,640:720]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               green_tr[x-240:y-240,640:720]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-160:y-160,640:720]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-80:y-80,640:720]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               green_tr[x:y,640:720]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x+80:y+80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x+80:y+80,640:720]=transpose_image9[0:80,0:80]
               return green_tr

            
def green_permutation9(x,y,green_ch,green_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-640:y-640,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               green_tr[x-640:y-640,560:640]=transpose_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-560:y-560,560:640]=transpose_image2[0:80,0:80]
               print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-480:y-480,560:640]=transpose_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-400:y-400,560:640]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               green_tr[x-320:y-320,560:640]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-240:y-240,560:640]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-160:y-160,560:640]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               green_tr[x-80:y-80,560:640]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x:y,560:640]=transpose_image9[0:80,0:80]
               return green_tr             
       

def green_permutation10(x,y,green_ch,green_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-720:y-720,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               green_tr[x-720:y-720,480:560]=transpose_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-640:y-640,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-640:y-640,480:560]=transpose_image2[0:80,0:80]
               print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-560:y-560,480:560]=transpose_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-480:y-480,480:560]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               green_tr[x-400:y-400,480:560]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-320:y-320,480:560]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-240:y-240,480:560]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               green_tr[x-160:y-160,480:560]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-80:y-80,480:560]=transpose_image9[0:80,0:80]
               return green_tr                    

def green_permutation11(x,y,green_ch,green_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-800:y-800,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               green_tr[x-800:y-800,400:480]=transpose_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-720:y-720,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-720:y-720,400:480]=transpose_image2[0:80,0:80]
               print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-640:y-640,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-640:y-640,400:480]=transpose_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-560:y-560,400:480]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               green_tr[x-480:y-480,400:480]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-400:y-400,400:480]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-320:y-320,400:480]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               green_tr[x-240:y-240,400:480]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-160:y-160,400:480]=transpose_image9[0:80,0:80]
               return green_tr              

def green_permutation12(x,y,green_ch,green_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-880:y-880,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               green_tr[x-880:y-880,320:400]=transpose_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-800:y-800,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-800:y-800,320:400]=transpose_image2[0:80,0:80]
               print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-720:y-720,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-720:y-720,320:400]=transpose_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x-640:y-640,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-640:y-640,320:400]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               green_tr[x-560:y-560,320:400]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-480:y-480,320:400]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-400:y-400,320:400]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               green_tr[x-320:y-320,320:400]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-240:y-240,320:400]=transpose_image9[0:80,0:80]
               return green_tr
            
def green_permutation13(x,y,green_ch,green_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-960:y-960,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               green_tr[x-960:y-960,240:320]=transpose_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-880:y-880,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-880:y-880,240:320]=transpose_image2[0:80,0:80]
               print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-800:y-800,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-800:y-800,240:320]=transpose_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x-720:y-720,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-720:y-720,240:320]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x-640:y-640,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               green_tr[x-640:y-640,240:320]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-560:y-560,240:320]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-480:y-480,240:320]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               green_tr[x-400:y-400,240:320]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-320:y-320,240:320]=transpose_image9[0:80,0:80]
               return green_tr    

def green_permutation14(x,y,green_ch,green_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-1040:y-1040,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
                   
               green_tr[x-1040:y-1040,160:240]=transpose_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-960:y-960,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
                   
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-960:y-960,160:240]=transpose_image2[0:80,0:80]
               print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-880:y-880,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-880:y-880,160:240]=transpose_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x-800:y-800,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-800:y-800,160:240]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x-720:y-720,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               green_tr[x-720:y-720,160:240]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x-640:y-640,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-640:y-640,160:240]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-560:y-560,160:240]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               green_tr[x-480:y-480,160:240]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-400:y-400,160:240]=transpose_image9[0:80,0:80]
               return green_tr
            
def green_permutation15(x,y,green_ch,green_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-1120:y-1120,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               green_tr[x-1120:y-1120,80:160]=transpose_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-1040:y-1040,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-1040:y-1040,80:160]=transpose_image2[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-960:y-960,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-960:y-960,80:160]=transpose_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x-880:y-880,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-880:y-880,80:160]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x-800:y-800,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               green_tr[x-800:y-800,80:160]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x-720:y-720,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-720:y-720,80:160]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x-640:y-640,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-640:y-640,80:160]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               green_tr[x-560:y-560,80:160]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-480:y-480,80:160]=transpose_image9[0:80,0:80]
               return green_tr    


def green_permutation16(x,y,green_ch,green_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=green_ch[x-1200:y-1200,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               green_tr[x-1200:y-1200,0:80]=transpose_image1[0:80,0:80]
                #print("Green channel:",green_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=green_ch[x-1120:y-1120,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-1120:y-1120,0:80]=transpose_image2[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=green_ch[x-1040:y-1040,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-1040:y-1040,0:80]=transpose_image3[0:80,0:80]
               #print("Green channel:",green_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=green_ch[x-960:y-960,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-960:y-960,0:80]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=green_ch[x-880:y-880,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               green_tr[x-880:y-880,0:80]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=green_ch[x-800:y-800,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-800:y-800,0:80]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=green_ch[x-720:y-720,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-720:y-720,0:80]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=green_ch[x-640:y-640,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               green_tr[x-640:y-640,0:80]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=green_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               green_tr[x-560:y-560,0:80]=transpose_image9[0:80,0:80]
               return green_tr

            


#Red Channel
def red_permutation1(x,y,red_ch,red_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               
               rc_image1[0:80,0:80]=red_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               red_tr[x:y,x+1200:y+1200]=transpose_image1[0:80,0:80]
               #print("Green channel traspose:",red_tr)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x+80:y+80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+80:y+80,1200:1280]=transpose_image2[0:80,0:80]
               #print("Green channel:",red_tr)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x+160:y+160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for g in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,g]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[g,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+160:y+160,1200:1280]=transpose_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x+240:y+240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for h in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,h]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[h,0:80]
                   #transpose_image4[0:80,h]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+240:y+240,1200:1280]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x+320:y+320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for i in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,i]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[i,0:80]
                   #transpose_image5[0:80,i]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               red_tr[x+320:y+320,1200:1280]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x+400:y+400,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for j in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,j]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[j,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+400:y+400,1200:1280]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x+480:y+480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+480:y+480,1200:1280]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x+560:y+560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               red_tr[x+560:y+560,1200:1280]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x+640:y+640,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+640:y+640,1200:1280]=transpose_image9[0:80,0:80]
               print("red_tr:",red_tr)
               return red_tr
               
               
def red_permutation2(x,y,red_ch,red_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               red_tr[x-80:y-80,1120:1200]=transpose_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x:y,1120:1200]=transpose_image2[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x+80:y+80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+80:y+80,1120:1200]=transpose_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x+160:y+160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+160:y+160,1120:1200]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x+240:y+240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               red_tr[x+240:y+240,1120:1200]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x+320:y+320,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+320:y+320,1120:1200]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x+400:y+400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+400:y+400,1120:1200]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x+480:y+480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               red_tr[x+480:y+480,1120:1200]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x+560:y+560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+560:y+560,1120:1200]=transpose_image9[0:80,0:80]
               return red_tr


def red_permutation3(x,y,red_ch,red_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               red_tr[x-160:y-160,1040:1120]=transpose_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-80:y-80,1040:1120]=transpose_image2[0:80,0:80]
               print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x:y,1040:1120]=transpose_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x+80:y+80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+80:y+80,1040:1120]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x+160:y+160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               red_tr[x+160:y+160,1040:1120]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x+240:y+240,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+240:y+240,1040:1120]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x+320:y+320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+320:y+320,1040:1120]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x+400:y+400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               red_tr[x+400:y+400,1040:1120]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x+480:y+480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+480:y+480,1040:1120]=transpose_image9[0:80,0:80]
               return red_tr              


def red_permutation4(x,y,red_ch,red_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               red_tr[x-240:y-240,960:1040]=transpose_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-160:y-160,960:1040]=transpose_image2[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-80:y-80,960:1040]=transpose_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x:y,960:1040]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x+80:y+80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               red_tr[x+80:y+80,960:1040]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x+160:y+160,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+160:y+160,960:1040]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x+240:y+240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+240:y+240,960:1040]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x+320:y+320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               red_tr[x+320:y+320,960:1040]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x+400:y+400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   row_data=rc_image9[f,0:80]
                   transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+400:y+400,960:1040]=transpose_image9[0:80,0:80]
               return red_tr              
   

def red_permutation5(x,y,red_ch,red_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               red_tr[x-320:y-320,880:960]=transpose_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-240:y-240,880:960]=transpose_image2[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-160:y-160,880:960]=transpose_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-80:y-80,880:960]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               red_tr[x:y,880:960]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x+80:y+80,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+80:y+80,880:960]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x+160:y+160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+160:y+160,880:960]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x+240:y+240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               red_tr[x+240:y+240,880:960]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x+320:y+320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+320:y+320,880:960]=transpose_image9[0:80,0:80]
               return red_tr              
   

def red_permutation6(x,y,red_ch,red_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               red_tr[x-400:y-400,800:880]=transpose_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-320:y-320,800:880]=transpose_image2[0:80,0:80]
               print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-240:y-240,800:880]=transpose_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-160:y-160,800:880]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               red_tr[x-80:y-80,800:880]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x:y,800:880]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x+80:y+80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+80:y+80,800:880]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x+160:y+160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               red_tr[x+160:y+160,800:880]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x+240:y+240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+240:y+240,800:880]=transpose_image9[0:80,0:80]
               return red_tr              
             

def red_permutation7(x,y,red_ch,red_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               red_tr[x-480:y-480,720:800]=transpose_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-400:y-400,720:800]=transpose_image2[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-320:y-320,720:800]=transpose_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-240:y-240,720:800]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               red_tr[x-160:y-160,720:800]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-80:y-80,720:800]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x:y,720:800]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x+80:y+80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               red_tr[x+80:y+80,720:800]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x+160:y+160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+160:y+160,720:800]=transpose_image9[0:80,0:80]
               return red_tr                           

def red_permutation8(x,y,red_ch,red_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               red_tr[x-560:y-560,640:720]=transpose_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-480:y-480,640:720]=transpose_image2[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-400:y-400,640:720]=transpose_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-320:y-320,640:720]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               red_tr[x-240:y-240,640:720]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-160:y-160,640:720]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-80:y-80,640:720]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               red_tr[x:y,640:720]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x+80:y+80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x+80:y+80,640:720]=transpose_image9[0:80,0:80]
               return red_tr

            
def red_permutation9(x,y,red_ch,red_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-640:y-640,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               red_tr[x-640:y-640,560:640]=transpose_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-560:y-560,560:640]=transpose_image2[0:80,0:80]
               print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-480:y-480,560:640]=transpose_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-400:y-400,560:640]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               red_tr[x-320:y-320,560:640]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-240:y-240,560:640]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-160:y-160,560:640]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               red_tr[x-80:y-80,560:640]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x:y,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x:y,560:640]=transpose_image9[0:80,0:80]
               return red_tr             
       

def red_permutation10(x,y,red_ch,red_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-720:y-720,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               red_tr[x-720:y-720,480:560]=transpose_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-640:y-640,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-640:y-640,480:560]=transpose_image2[0:80,0:80]
               print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-560:y-560,480:560]=transpose_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-480:y-480,480:560]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               red_tr[x-400:y-400,480:560]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-320:y-320,480:560]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-240:y-240,480:560]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               red_tr[x-160:y-160,480:560]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x-80:y-80,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-80:y-80,480:560]=transpose_image9[0:80,0:80]
               return red_tr                    

def red_permutation11(x,y,red_ch,red_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-800:y-800,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               red_tr[x-800:y-800,400:480]=transpose_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-720:y-720,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-720:y-720,400:480]=transpose_image2[0:80,0:80]
               print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-640:y-640,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-640:y-640,400:480]=transpose_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-560:y-560,400:480]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               red_tr[x-480:y-480,400:480]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-400:y-400,400:480]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-320:y-320,400:480]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               red_tr[x-240:y-240,400:480]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x-160:y-160,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-160:y-160,400:480]=transpose_image9[0:80,0:80]
               return red_tr              

def red_permutation12(x,y,red_ch,red_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-880:y-880,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               red_tr[x-880:y-880,320:400]=transpose_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-800:y-800,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-800:y-800,320:400]=transpose_image2[0:80,0:80]
               print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-720:y-720,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-720:y-720,320:400]=transpose_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x-640:y-640,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-640:y-640,320:400]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               red_tr[x-560:y-560,320:400]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-480:y-480,320:400]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-400:y-400,320:400]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               red_tr[x-320:y-320,320:400]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x-240:y-240,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-240:y-240,320:400]=transpose_image9[0:80,0:80]
               return red_tr
            
def red_permutation13(x,y,red_ch,red_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-960:y-960,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               red_tr[x-960:y-960,240:320]=transpose_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-880:y-880,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-880:y-880,240:320]=transpose_image2[0:80,0:80]
               print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-800:y-800,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-800:y-800,240:320]=transpose_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x-720:y-720,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-720:y-720,240:320]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x-640:y-640,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               red_tr[x-640:y-640,240:320]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-560:y-560,240:320]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-480:y-480,240:320]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               red_tr[x-400:y-400,240:320]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x-320:y-320,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-320:y-320,240:320]=transpose_image9[0:80,0:80]
               return red_tr    

def red_permutation14(x,y,red_ch,red_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-1040:y-1040,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
                   
               red_tr[x-1040:y-1040,160:240]=transpose_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-960:y-960,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
                   
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-960:y-960,160:240]=transpose_image2[0:80,0:80]
               print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-880:y-880,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-880:y-880,160:240]=transpose_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x-800:y-800,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-800:y-800,160:240]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x-720:y-720,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               red_tr[x-720:y-720,160:240]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x-640:y-640,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-640:y-640,160:240]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-560:y-560,160:240]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               red_tr[x-480:y-480,160:240]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x-400:y-400,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-400:y-400,160:240]=transpose_image9[0:80,0:80]
               return red_tr
            
def red_permutation15(x,y,red_ch,red_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-1120:y-1120,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               red_tr[x-1120:y-1120,80:160]=transpose_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-1040:y-1040,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-1040:y-1040,80:160]=transpose_image2[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-960:y-960,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-960:y-960,80:160]=transpose_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x-880:y-880,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-880:y-880,80:160]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x-800:y-800,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               red_tr[x-800:y-800,80:160]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x-720:y-720,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-720:y-720,80:160]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x-640:y-640,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-640:y-640,80:160]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               red_tr[x-560:y-560,80:160]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x-480:y-480,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-480:y-480,80:160]=transpose_image9[0:80,0:80]
               return red_tr    


def red_permutation16(x,y,red_ch,red_tr,keycol1):
               rc_image1=np.zeros((80, 80), np.uint8)
               transpose_image1=np.zeros((80, 80), np.uint8)
               rc_image1[0:80,0:80]=red_ch[x-1200:y-1200,x:y]
               #print("Before encryption and  transpose",rc_image)
               aa=len(keycol1)-1
               for e in keycol1:
                   #print("e:",e)
                   col_data=rc_image1[:,e]
                   #print("Col:",col_data)
                   #row_data=rc_image1[e,0:80]
                   #transpose_image1[0:80,e]=row_data
                   transpose_image1[aa,:80]=col_data
                   aa=aa-1
               red_tr[x-1200:y-1200,0:80]=transpose_image1[0:80,0:80]
                #print("Green channel:",red_ch)
                #print("After encryption+row column transpose",transpose_image)

               rc_image2=np.zeros((80, 80), np.uint8)
               transpose_image2=np.zeros((80, 80), np.uint8)
               rc_image2[0:80,0:80]=red_ch[x-1120:y-1120,x:y]
               #print("Before encryption and  transpose",rc_image)
               ab=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image2[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image2[f,0:80]
                   #transpose_image2[0:80,f]=row_data
                   transpose_image2[ab,:80]=col_data
                   ab=ab-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-1120:y-1120,0:80]=transpose_image2[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image3=np.zeros((80, 80), np.uint8)
               transpose_image3=np.zeros((80, 80), np.uint8)
               rc_image3[0:80,0:80]=red_ch[x-1040:y-1040,x:y]
               #print("Before encryption and  transpose",rc_image)
               ac=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image3[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image3[f,0:80]
                   #transpose_image3[0:80,f]=row_data
                   transpose_image3[ac,:80]=col_data
                   ac=ac-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-1040:y-1040,0:80]=transpose_image3[0:80,0:80]
               #print("Green channel:",red_ch)

               rc_image4=np.zeros((80, 80), np.uint8)
               transpose_image4=np.zeros((80, 80), np.uint8)
               rc_image4[0:80,0:80]=red_ch[x-960:y-960,x:y]
               #print("Before encryption and  transpose",rc_image)
               ad=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image4[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image4[f,0:80]
                   #transpose_image4[0:80,f]=row_data
                   transpose_image4[ad,:80]=col_data
                   ad=ad-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-960:y-960,0:80]=transpose_image4[0:80,0:80]

               rc_image5=np.zeros((80, 80), np.uint8)
               transpose_image5=np.zeros((80, 80), np.uint8)
               rc_image5[0:80,0:80]=red_ch[x-880:y-880,x:y]
               #print("Before encryption and  transpose",rc_image)
               ae=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image5[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image5[f,0:80]
                   #transpose_image5[0:80,f]=row_data
                   transpose_image5[ae,:80]=col_data
                   ae=ae-1
               red_tr[x-880:y-880,0:80]=transpose_image5[0:80,0:80]

               rc_image6=np.zeros((80, 80), np.uint8)
               transpose_image6=np.zeros((80, 80), np.uint8)
               rc_image6[0:80,0:80]=red_ch[x-800:y-800,x:y]
               #print("Before encryption and  transpose",rc_image)
               af=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image6[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image6[f,0:80]
                   #transpose_image6[0:80,f]=row_data
                   transpose_image6[af,:80]=col_data
                   af=af-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-800:y-800,0:80]=transpose_image6[0:80,0:80]

               rc_image7=np.zeros((80, 80), np.uint8)
               transpose_image7=np.zeros((80, 80), np.uint8)
               rc_image7[0:80,0:80]=red_ch[x-720:y-720,x:y]
               #print("Before encryption and  transpose",rc_image)
               ag=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image7[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image7[f,0:80]
                   #transpose_image7[0:80,f]=row_data
                   transpose_image7[ag,:80]=col_data
                   ag=ag-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-720:y-720,0:80]=transpose_image7[0:80,0:80]

               rc_image8=np.zeros((80, 80), np.uint8)
               transpose_image8=np.zeros((80, 80), np.uint8)
               rc_image8[0:80,0:80]=red_ch[x-640:y-640,x:y]
               #print("Before encryption and  transpose",rc_image)
               ah=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image8[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image8[f,0:80]
                   #transpose_image8[0:80,f]=row_data
                   transpose_image8[ah,:80]=col_data
                   ah=ah-1
                   #print("After encryption+row column transpose",transpose_image)
               red_tr[x-640:y-640,0:80]=transpose_image8[0:80,0:80]

               rc_image9=np.zeros((80, 80), np.uint8)
               transpose_image9=np.zeros((80, 80), np.uint8)
               rc_image9[0:80,0:80]=red_ch[x-560:y-560,x:y]
               #print("Before encryption and  transpose",rc_image)
               ai=len(keycol1)-1
               for f in keycol1:
                   #print("f:",f)
                   col_data=rc_image9[:,f]
                   #print("Col:",col_data)f
                   #row_data=rc_image9[f,0:80]
                   #transpose_image9[0:80,f]=row_data
                   transpose_image9[ai,:80]=col_data
                   ai=ai-1
               #print("After encryption+row column transpose",transpose_image)
               red_tr[x-560:y-560,0:80]=transpose_image9[0:80,0:80]
               return red_tr

            

r=720
c=1280
t=3
'''enc_start=0
enc_end=0
dec_start=0
dec_end=0'''
pathIn1="G:/impl/linux_backup/png_frames/"
files1 = [f for f in os.listdir(pathIn1) if os.path.isfile(os.path.join(pathIn1, f))]
#files1.sort(key=lambda x: int(x[5:-4]))

keycol2=rd.sample(range(0,80),80)
#print(keycol1)
np.save('keycol_rc_rgb_frames_l2',keycol2)
keycol=np.load('keycol_rc_rgb_frames_l2.npy')

n=30
for i in range(n):
    j=random.choice(files1)
    print("i:",i)
    #np.save('enc_rc_green_frames',j)
    frame_no=int(j[5:-4])
    #print("frameno:",frame_no)
    #print("Path In1:",pathIn1)
    filename=pathIn1+j
    #print("Filename:",filename)
    #print("Length:",len(j))
    img=cv2.imread(filename)


    bluech=img[:,:,0]
    greench=img[:,:,1]
    redch=img[:,:,2]

    bluetr=np.zeros((r, c), np.uint8)
    greentr=np.zeros((r, c), np.uint8)
    redtr=np.zeros((r, c), np.uint8)

    #Blue Channel
    permuted_img_blue1=blue_permutation1(0,80,bluech,bluetr,keycol)
    permuted_img_blue2=blue_permutation2(80,160,bluech,bluetr,keycol)
    permuted_img_blue3=blue_permutation3(160,240,bluech,bluetr,keycol)
    permuted_img_blue4=blue_permutation4(240,320,bluech,bluetr,keycol)
    permuted_img_blue5=blue_permutation5(320,400,bluech,bluetr,keycol)
    permuted_img_blue6=blue_permutation6(400,480,bluech,bluetr,keycol)
    permuted_img_blue7=blue_permutation7(480,560,bluech,bluetr,keycol)
    permuted_img_blue8=blue_permutation8(560,640,bluech,bluetr,keycol)
    permuted_img_blue9=blue_permutation9(640,720,bluech,bluetr,keycol)
    permuted_img_blue10=blue_permutation10(720,800,bluech,bluetr,keycol)
    permuted_img_blue11=blue_permutation11(800,880,bluech,bluetr,keycol)
    permuted_img_blue12=blue_permutation12(880,960,bluech,bluetr,keycol)
    permuted_img_blue13=blue_permutation13(960,1040,bluech,bluetr,keycol)
    permuted_img_blue14=blue_permutation14(1040,1120,bluech,bluetr,keycol)
    permuted_img_blue15=blue_permutation15(1120,1200,bluech,bluetr,keycol)
    permuted_img_blue16=blue_permutation16(1200,1280,bluech,bluetr,keycol)

    #greenchannel

    permuted_img_green1=green_permutation1(0,80,greench,greentr,keycol)
    permuted_img_green2=green_permutation2(80,160,greench,greentr,keycol)
    permuted_img_green3=green_permutation3(160,240,greench,greentr,keycol)
    permuted_img_green4=green_permutation4(240,320,greench,greentr,keycol)
    permuted_img_green5=green_permutation5(320,400,greench,greentr,keycol)
    permuted_img_green6=green_permutation6(400,480,greench,greentr,keycol)
    permuted_img_green7=green_permutation7(480,560,greench,greentr,keycol)
    permuted_img_green8=green_permutation8(560,640,greench,greentr,keycol)
    permuted_img_green9=green_permutation9(640,720,greench,greentr,keycol)
    permuted_img_green10=green_permutation10(720,800,greench,greentr,keycol)
    permuted_img_green11=green_permutation11(800,880,greench,greentr,keycol)
    permuted_img_green12=green_permutation12(880,960,greench,greentr,keycol)
    permuted_img_green13=green_permutation13(960,1040,greench,greentr,keycol)
    permuted_img_green14=green_permutation14(1040,1120,greench,greentr,keycol)
    permuted_img_green15=green_permutation15(1120,1200,greench,greentr,keycol)
    permuted_img_green16=green_permutation16(1200,1280,greench,greentr,keycol)


    #Red Channel
    permuted_img_red1=red_permutation1(0,80,redch,redtr,keycol)
    permuted_img_red2=red_permutation2(80,160,redch,redtr,keycol)
    permuted_img_red3=red_permutation3(160,240,redch,redtr,keycol)
    permuted_img_red4=red_permutation4(240,320,redch,redtr,keycol)
    permuted_img_red5=red_permutation5(320,400,redch,redtr,keycol)
    permuted_img_red6=red_permutation6(400,480,redch,redtr,keycol)
    permuted_img_red7=red_permutation7(480,560,redch,redtr,keycol)
    permuted_img_red8=red_permutation8(560,640,redch,redtr,keycol)
    permuted_img_red9=red_permutation9(640,720,redch,redtr,keycol)
    permuted_img_red10=red_permutation10(720,800,redch,redtr,keycol)
    permuted_img_red11=red_permutation11(800,880,redch,redtr,keycol)
    permuted_img_red12=red_permutation12(880,960,redch,redtr,keycol)
    permuted_img_red13=red_permutation13(960,1040,redch,redtr,keycol)
    permuted_img_red14=red_permutation14(1040,1120,redch,redtr,keycol)
    permuted_img_red15=red_permutation15(1120,1200,redch,redtr,keycol)
    permuted_img_red16=red_permutation16(1200,1280,redch,redtr,keycol)

    for row in range(720):
        for col in range(1280):
            #Blue
            img[row][col][0]=permuted_img_blue1[row][col]
            img[row][col][0]=permuted_img_blue2[row][col]
            img[row][col][0]=permuted_img_blue3[row][col]
            img[row][col][0]=permuted_img_blue4[row][col]
            img[row][col][0]=permuted_img_blue5[row][col]
            img[row][col][0]=permuted_img_blue6[row][col]
            img[row][col][0]=permuted_img_blue7[row][col]
            img[row][col][0]=permuted_img_blue8[row][col]
            img[row][col][0]=permuted_img_blue9[row][col]
            img[row][col][0]=permuted_img_blue10[row][col]
            img[row][col][0]=permuted_img_blue11[row][col]
            img[row][col][0]=permuted_img_blue12[row][col]
            img[row][col][0]=permuted_img_blue13[row][col]
            img[row][col][0]=permuted_img_blue14[row][col]
            img[row][col][0]=permuted_img_blue15[row][col]
            img[row][col][0]=permuted_img_blue16[row][col]
            #Green
            img[row][col][1]=permuted_img_green1[row][col]
            img[row][col][1]=permuted_img_green2[row][col]
            img[row][col][1]=permuted_img_green3[row][col]
            img[row][col][1]=permuted_img_green4[row][col]
            img[row][col][1]=permuted_img_green5[row][col]
            img[row][col][1]=permuted_img_green6[row][col]
            img[row][col][1]=permuted_img_green7[row][col]
            img[row][col][1]=permuted_img_green8[row][col]
            img[row][col][1]=permuted_img_green9[row][col]
            img[row][col][1]=permuted_img_green10[row][col]
            img[row][col][1]=permuted_img_green11[row][col]
            img[row][col][1]=permuted_img_green12[row][col]
            img[row][col][1]=permuted_img_green13[row][col]
            img[row][col][1]=permuted_img_green14[row][col]
            img[row][col][1]=permuted_img_green15[row][col]
            img[row][col][1]=permuted_img_green16[row][col]
            #Red
            img[row][col][2]=permuted_img_red1[row][col]
            img[row][col][2]=permuted_img_red2[row][col]
            img[row][col][2]=permuted_img_red3[row][col]
            img[row][col][2]=permuted_img_red4[row][col]
            img[row][col][2]=permuted_img_red5[row][col]
            img[row][col][2]=permuted_img_red6[row][col]
            img[row][col][2]=permuted_img_red7[row][col]
            img[row][col][2]=permuted_img_red8[row][col]
            img[row][col][2]=permuted_img_red9[row][col]
            img[row][col][2]=permuted_img_red10[row][col]
            img[row][col][2]=permuted_img_red11[row][col]
            img[row][col][2]=permuted_img_red12[row][col]
            img[row][col][2]=permuted_img_red13[row][col]
            img[row][col][2]=permuted_img_red14[row][col]
            img[row][col][2]=permuted_img_red15[row][col]
            img[row][col][2]=permuted_img_red16[row][col]

    print("Frame No:\n",frame_no)
    cv2.imwrite("G:/impl/linux_backup/enc_rc_keypos_rgb_frames_l2/frame%d.png" %frame_no,img)
    print("End")



