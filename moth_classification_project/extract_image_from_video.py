""" Code for Extracting Image Data from Footage

Usage:

    python3 extract_image_from_video.py

"""

import cv2 # For the frame extraction from the video data

import numpy as np

import os # For interacting with the local machine

# Playing video from file:
# Change to directory containing your own videos
cap = cv2.VideoCapture('Video 1.mp4')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    name = './data/FAW' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1


# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()