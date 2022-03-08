"""
Code for Deleting Similar Images from Extraced Our Video Data

Usage:
    Change <ENTER DATASET PATH> to your data directory
    RUN: python3 delete_similar_images.py

"""

import os
from sklearn.metrics import mean_squared_error # Use the mean_squred_error method provided already
from math import sqrt
from os.path import join
import cv2
import numpy as np
import shutil


 
def getBwLittleImgs(datasetPath):
    """
    Reads the image dataset path, creates a new folder, and convert the images
        to grayscale--to make them easier to work with.

    Args:
      datasetPath (str) --> Path to the image data (must be a folder).

    Return:
      None.
    """
    # Find all classes paths in directory and iterate over it
    for (i, classPath) in enumerate(os.listdir(datasetPath)):

        # Construct detected directory with images from MobileNET SSD
        imgDir = join(datasetPath, classPath)
        # Construct directory to write 32x32 pix images
        bwDir = join(datasetPath, classPath, "bwdir")

        print(classPath)

        # Create bwDir patch or delete existing!
        if not os.path.exists(bwDir):
            os.makedirs(bwDir)
        else:
            shutil.rmtree(bwDir)
            os.makedirs(bwDir)

        # Iterate over all images in detected directory
        for (j, imgName) in enumerate(os.listdir(imgDir)):

            # Construct patch to single image
            imgPath = join(imgDir, imgName)
            # Read image using OpenCV as grayscale
            image = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)
        try:
            # Check if we opened an image.
            if image is not None:
                # Resize opened image
                resized_image = cv2.resize(image, (900, 450))
                resized_image = np.array(resized_image)
                # Save image to bwdir. Name should be the same as name in "detected" directory
                cv2.imwrite(os.path.join(bwDir, imgName), resized_image)
            else:
                # remove a file that is not an image. I don't need it.
                print(imgPath)
                os.remove(imgPath)
        except PermissionError as p:
            continue

def findDelDuplBw(searchedName, bwDir):
    """
    Reads the newly created folder of grayscale images, takes in image files from
    the original image folder, calulates the root mean squared error on the grayscale
    images, and if the root mean square is < 3, it indicates similarity. It compares 
    original and grayscale images, and removes images in the original image folder
    with root mean square error < 3.

    Args:
      searchedName (str) --> Image files in the original image folder.
      bwDir (str) --> Newly created grayscale images folder.

    Return:
      None. 
      """
        # Join path to orginal image that we are looking duplicates
    searchedImg = join(bwDir, searchedName)

        # Start iterate over all bw images
    for (j, cmpImageName) in enumerate(os.listdir(bwDir)):

            if cmpImageName == searchedName:
                # If name in bwDir is equal to searched image - pass. I don't wan to deleted searched image in bw dir
                pass
            else:
                # If name is different - concatenate path to image
                cmpImageBw = join(bwDir, cmpImageName)

                try:
                    # Open image in bwDir - The searched image
                    searchedImageBw = np.array(cv2.imread(searchedImg, cv2.IMREAD_GRAYSCALE))
                    # Open image to be compared
                    cmpImage = np.array(cv2.imread(cmpImageBw, cv2.IMREAD_GRAYSCALE))
                    # Count root mean square between both images (RMS)
                    rms = sqrt(mean_squared_error(searchedImageBw, cmpImage))
                except:
                    continue

                # If RMS is smaller than 3 - this means that images are simmilar or the same
                if rms < 3:
                    # Delete compared image in BW dir
                    os.remove(cmpImageBw)
                    print(searchedImg, cmpImageName, rms)

def main():
    datasetPath = "<ENTER DATASET PATH>"
    getBwLittleImgs(datasetPath)

    for (i, classPath) in enumerate(os.listdir(datasetPath)):

        # Join detected by previous script path
        detectedDir = join(datasetPath, classPath)
        # Join black-white images path
        bwDir = join(datasetPath, classPath, "bwdir")

        # Iterate over images in one class - detected images previously by MobileSSD net
        for (i, detectedImg) in enumerate(os.listdir(detectedDir)):
            # Find duplicated BW images and delete duplicates.
            findDelDuplBw(detectedImg, bwDir)

if __name__ == "__main__":
    main()