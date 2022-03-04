import cv2
import numpy as np
import os
from PIL import Image

img1=cv2.imread(r'''C:\Users\hp\Desktop\A\Finalised Project\org.jpg''');
# Playing video from file:
cap = cv2.VideoCapture('minions.mp4')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print('Error: Creating directory of data')
    
img = np.zeros((1200,1200,3), np.uint8)
currentFrame = 0;
while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #z = cv2.imread('org.jpg');
    #z = cv2.resize(z, (frame.shape[1], frame.shape[0]));

    if currentFrame == 5:#for the first image with first 2 MSBs
        for i in range(frame.shape[1]):
            for j in range(frame.shape[0]):#height
                y = frame[j, i];
                for k in range(3):#for the first image with first 2 MSBs
                    y[k]=y[k]&0b11;
                    y[k]=y[k]<<6;
                    img[j, i,k] += y[k];           
    #print("creating.." + str(currentFrame));

    if currentFrame == 10:#for the first image with first 2 MSBs
        for i in range(frame.shape[1]):
            for j in range(frame.shape[0]):
                y = frame[j, i];
                for k in range(3):#for the first image with first 2 MSBs
                    y[k]=y[k]&0b11;
                    y[k]=y[k]<<4;
                    img[j, i,k] += y[k];
    #print("creating.." + str(currentFrame));
                
    if currentFrame == 15:#for the first image with first 2 MSBs
        for i in range(frame.shape[1]):
            for j in range(frame.shape[0]):
                y = frame[j, i];
                for k in range(3):#for the first image with first 2 MSBs
                    y[k]=y[k]&0b11;
                    y[k]=y[k]<<2;
                    img[j, i,k] += y[k];
    #print("creating.." + str(currentFrame));

    if currentFrame == 20:#for the first image with first 2 MSBs
        for i in range(frame.shape[1]):
            for j in range(frame.shape[0]):
                y = frame[j, i];
                for k in range(3):#for the first image with first 2 MSBs
                    y[k]=y[k]&0b11;
                    y[k]=y[k];
                    img[j, i,k] += y[k];
    print("extracting.." + str(currentFrame));

    #if currentFrame ==25:
        #ret=0;

    if not ret: break;
    currentFrame += 1

cv2.imwrite('original_decrypted_opencv.tif',img1);
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()



