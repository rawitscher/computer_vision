# USAGE
# python download-image-by-link.py --link "url" --type "positive/negative"

# import the necessary packages

from urllib2 import urlopen
import argparse
import cv2
import imutils
import numpy as np
import os

# Construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--images', required=True,
                help='path to images')
ap.add_argument('-t', '--type', required=True,
                help='positive or negative')
args = vars(ap.parse_args())

# Get the input images and store them in a list
dir = args["images"]
image_names = os.listdir(dir)

index = 0
for name in image_names:
    image_names[index] = os.path.join(dir, name)
    index+=1

def store_raw_images():
    pic_num = 1
    print pic_num
    if not os.path.exists(args['type']):
        os.makedirs(args['type'])
        
    for i in image_names:
        try:
            print(i)
            #urllib2.urlretrieve(i, args['type'] + '/' + str(pic_num) + '.jpg')
            img = cv2.imread(i, cv2.IMREAD_GRAYSCALE)
            #img = cv2.imread(args['type'] + '/' +str(pic_num)+'.jpg',cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            if args['type'] == 'negative':
                resized_image = cv2.resize(img, (100, 100))
            else:
                resized_image = cv2.resize(img, (50, 50))
            cv2.imwrite(args['type'] + '/' +str(pic_num)+'.jpg',resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))  

store_raw_images()
