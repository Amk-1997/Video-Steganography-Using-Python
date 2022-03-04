import cv2
import numpy as np
import os
from PIL import Image

# Playing video from file:
cap = cv2.VideoCapture('minions.mp4')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print('Error: Creating directory of data')

currentFrame = 0;
while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    z = cv2.imread('org.jpg');
    z = cv2.resize(z, (frame.shape[1], frame.shape[0]));
    cv2.imwrite('resised_org.jpg',z);

    if currentFrame == 5:#for the first image with first 2 MSBs
        for i in range(frame.shape[1]):
            for j in range(frame.shape[0]):
                x = z[j, i];
                y = frame[j, i];
                for k in range(3):
                    xa = x[k] & 0b11000000;
                    xa = xa >> 6;
                    y[k] = y[k] & 0b11111100;
                    y[k] = y[k] | xa;
                frame[j, i] = y;
        #cv2.imwrite('imga.bmp',frame);
    #print("creating.." + str(currentFrame));

    if currentFrame == 10:#for the second image with next 2 MSBs
        for i in range(frame.shape[1]):
            for j in range(frame.shape[0]):
                x = z[j, i];
                y = frame[j, i];
                for k in range(3):
                    xa = x[k] & 0b00110000;
                    xa = xa >> 4;
                    y[k] = y[k] & 0b11111100;
                    y[k] = y[k] | xa;
                frame[j, i] = y;
        #cv2.imwrite('imgb.bmp',frame);
    #print("creating.." + str(currentFrame));

    if currentFrame == 15:#for the second image with next 2 LSBs
        for i in range(frame.shape[1]):
            for j in range(frame.shape[0]):
                x = z[j, i];
                y = frame[j, i];
                for k in range(3):
                    xa = x[k] & 0b00001100;
                    xa = xa >> 2;
                    y[k] = y[k] & 0b11111100;
                    y[k] = y[k] | xa;
                frame[j, i] = y;
        #cv2.imwrite('imgc.bmp',frame);                
    #print("creating.." + str(currentFrame));

    if currentFrame == 20:#for the second image with LSBs
        for i in range(frame.shape[1]):
            for j in range(frame.shape[0]):
                x = z[j, i];
                y = frame[j, i];
                for k in range(3):
                    xa = x[k] & 0b0000000011;
                    xa = xa;
                    y[k] = y[k] & 0b11111100;
                    y[k] = y[k] | xa;
                frame[j, i] = y;
        #cv2.imwrite('imgd.bmp',frame);                
    print("creating.." + str(currentFrame));

    if currentFrame ==25:
        ret=0;
        
    if not ret: break;
    currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
