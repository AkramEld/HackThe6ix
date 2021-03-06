import cv2
import numpy as np
import os
import time
import argparse
# Playing video from file:
parser = argparse.ArgumentParser(description='videoName')
parser.add_argument('--vidName', type=str, default='')
args = parser.parse_args()
cap = cv2.VideoCapture('./static/'+args.vidName)

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
ret = True
starttime=time.time()
while(ret):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if currentFrame%7==0:
        # Saves image of the current frame in jpg file
        name = './data/frame' + str(currentFrame) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
