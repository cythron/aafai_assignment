#!/usr/bin/python

import numpy as np
import os
from PIL import Image
import cv2
import sys

if len(sys.argv) == 1:
    LOCATION = ""
else:
    LOCATION = sys.argv[1]

os.chdir(LOCATION)
images_dir = [image for image in os.listdir() if (image.endswith(".jpg") or image.endswith(".png"))]
if not images_dir:
    print(f"No images found inside {LOCATION}")

try:
    os.mkdir('cropped')
except:
    pass

for image_orig in images_dir:
    image = Image.open(image_orig)
    h,w = image.height - image.height * 0.07, image.width - image.width * 0.08
    (left, upper, right, lower) = (30, 40, w, h)
    im_crop = image.crop((left, upper, right, lower))
    im_crop.save(f'cropped/{image_orig}')

os.chdir('cropped')
images_dir = [image for image in os.listdir() if (image.endswith(".jpg") or image.endswith(".png"))]

try:
    os.mkdir('../final')
except:
    pass

for image_orig in images_dir:
    image = cv2.imread(image_orig)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
	#cv2.imshow('image', image)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()

    cv2.imwrite(f'../final/{image_orig}', image)
    print(f'Final: {image_orig}')


