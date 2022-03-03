# import the necessary packages
import random

import numpy as np
import argparse
import imutils
import cv2
import os
import glob
import time

start = time.time()
print("hello")

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="img1.png", help="path to the input image")
args = vars(ap.parse_args())

dirName = 'processedImages'
imagesList = glob.glob("images/*.png")
try:
    # Create target Directory
    os.mkdir(dirName)
    print("Directory ", dirName, " Created ")
except FileExistsError:
    print("Directory ", dirName, " already exists")

for image in imagesList:
    # print(random.randint(-1, 1))
    translateX = random.randint(-1, 1) * 3
    translateY = random.randint(-1, 1) * 3
    imageFileName = os.path.basename(image)
    readImage = cv2.imread(image)
    M = np.float32([[1, 0, 4.3], [0, 1, 3.5]])
    shifted = cv2.warpAffine(readImage, M, (readImage.shape[1], readImage.shape[0]))
    cv2.imwrite(dirName + "/prc_" + imageFileName, shifted)

end = time.time()
print(end - start)
cv2.waitKey(1000)
cv2.destroyAllWindows()
