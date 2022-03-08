"""Code for compressing the size of extracted images

Usage:
    
    Change label directory in line 50
    RUN python3 compress_image_size.py

"""

from PIL import Image
import PIL
import os
import glob


def compress_images(directory=False, quality=30):
    """
    Compress images from a given directory using the Image module from the Python
    Imaging Library with a defined image quality and optimization set to True.

    Args:
      directory (str) --> Provide a path to the class folder. False by default.
      quality (int) --> Numeric value for the quality of optimization using PIL.

    Return:
      None.
    """
    
    
    # 1. If there is a directory then change into it, else perform the next operations inside of the
    # current working directory:

    if directory:
        os.chdir(directory)

    # 2. Extract all of the .png and .jpeg files:
    files = os.listdir()

    # 3. Extract all of the images:
    images = [file for file in files if file.endswith(('jpg', 'png'))]

    # 4. Loop over every image:
    for image in images:
        print(image)

        # 5. Open every image:
        img = Image.open(image)

        # 5. Compress every image and save it with a new name:
        img.save("Compressed_and_resized_with_function_"+image, optimize=True, quality=quality)

# Enter label directory
compress_images(directory="../FAW")