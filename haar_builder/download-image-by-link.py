# USAGE
# python download-image-by-link.py --link "url" --type "positive/negative"

# import the necessary packages

from urllib2 import urlopen
import argparse
import cv2
import numpy as np
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-l', '--link', required=True,
                help='path to images')
ap.add_argument('-t', '--type', required=True,
                help='positive or negative')
args = vars(ap.parse_args())


def store_raw_images():
    images_link = args['link']
    image_urls = urllib2.urlopen(args['link']).read().decode()
    pic_num = 1
    
    if not os.path.exists(args['type']):
        os.makedirs(args['type'])
        
    for i in image_urls.split('\n'):
        try:
            print(i)
            urllib2.urlretrieve(i, args['type'] + '/' + str(pic_num) + '.jpg')
            img = cv2.imread(args['type'] + '/' +str(pic_num)+'.jpg',cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            if args['type'] == 'negative':
                resized_image = cv2.resize(img, (100, 100))
            else:
                resized_image = cv2.resize(img, (50, 50))
            cv2.imwrite(args['type'] + '/' +str(pic_num)+'.jpg',resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))  
