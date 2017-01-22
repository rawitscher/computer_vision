# USAGE
# python shirt_breakdown.py --image images/person_01.jpg

# import the necessary packages
import argparse
import cv2
import numpy as np

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
args = vars(ap.parse_args())

# load the input image and convert it to grayscale
image = cv2.imread(args["image"])
im_height, im_width, im_channels = image.shape
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

'''detector = cv2.CascadeClassifier("haarcascade_face.xml")
rects = detector.detectMultiScale(gray, scaleFactor=1.3,
	minNeighbors=5, minSize=(10, 10))

print rects.size
# check if image has a face
if (rects.size):
  # loop over detected pixels and draw a rectangle surrounding
	for (i, (x, y, w, h)) in enumerate(rects):
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 150), 2)
		# label face
		cv2.putText(image, "face" + "#{}".format(i + 1), (x, y - 10),
    	cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 150), 1),
		# print face pixel coordinates
    	cv2.putText(image, "face: ("+str(x)+", "+str(y)+"), ("+str(x+w)+", "+str(y+h)+")"+"#{}".format(i + 1), (0, 0),
    	cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 0), 1),
else:
		cv2.putText(image, "no face in image" + "#{}".format(i + 1), (0, 0),
  		cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 0), 1),
'''

# load shirt finding Haar cascade, then detect input image
detector = cv2.CascadeClassifier("haarcascade_shirt_finder.xml")
rects = detector.detectMultiScale(gray, scaleFactor=1.3,
	minNeighbors=5, minSize=(20, 20))

# check if model was detected
if (rects.size):

    # label shirt region
    print "starting shirt"
    for (i, (x, y, w, h)) in enumerate(rects):

        x_min = x
        rect_w = w
        y_min = y + h
        rect_h = h
        shirt = "shirt: ("+str(x_min)+", "+str(y_min)+"), ("+str(x_min + rect_w)+", "+str(y_min + rect_h)+")"
        cv2.rectangle(image, (x_min, y_min), (x_min + rect_w, y_min + rect_h), (0, 150, 0), 2)
        cv2.putText(image,shirt ,(int(im_width * 0.2), 20), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 0), 1)
    print "shirt done"

    # label collar region
    print "starting collar"
    for (i, (x_min, y_min, w, h)) in enumerate(rects):

        x_min = int(x+ w*0.1)
        rect_w = int(w*0.8)
        y_min = y + int(0.65*h)
        rect_h = int(0.35*h)
        collar = "collar: ("+str(x_min)+", "+str(y_min)+"), ("+str(x_min + rect_w)+", "+str(y_min + rect_h)+")"
        cv2.rectangle(image, (x_min, y_min), (x_min + rect_w, y_min + rect_h), (150, 0, 0), 2)
        cv2.putText(image,collar , (int(im_width * 0.2), 40), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 0), 1)
    print "collar done"

    # label sleeves
    print "starting left sleeve"
    for (i, (x_min, y_min, w, h)) in enumerate(rects):

        x_min = int(x - 0.3*w)
        rect_w = int(0.3*w)
        y_min = y + int(0.75*h)
        rect_h = int(1.25*h)
        left_sleeve = "left sleeve: ("+str(x_min)+", "+str(y_min)+"), ("+str(x_min + rect_w)+", "+str(y_min + rect_h)+")"
        rect = cv2.rectangle(image, (int(x_min*(np.cos(30)) - y_min*(np.sin(30))), int(x_min*(np.sin(30)) + y_min*(np.cos(30)))), (int((x_min + rect_w)*(np.cos(30)) - ((y_min + rect_h)*(np.sin(30)))), int((x_min + rect_w)*(np.sin(30)) + (y_min + rect_h)*(np.cos(30)))), (150, 150, 0), 2)
        #box = cv2.boxPoints(rect)
        #box = np.int0(box)
        #cv2.drawContours(im,[box],0,(0,0,255),2)
        cv2.putText(image, left_sleeve, (int(im_width * 0.6), 20), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 0), 1)
    print "left sleeve done"

    print "starting right sleeve"
    for (i, (x_min, y_min, w, h)) in enumerate(rects):

        x_min = x + w
        rect_w = int(0.3*w)
        y_min = y + int(0.75*h)
        rect_h = int(1.25*h)
        right_sleeve = "right sleeve: ("+str(x_min)+", "+str(y_min)+"), ("+str(x_min + rect_w)+", "+str(y_min + rect_h)+")"
        cv2.rectangle(image, (x_min, y_min), (x_min + rect_w, y_min + rect_h), (150, 150, 0), 2)
        cv2.putText(image, right_sleeve, (int(im_width * 0.6), 40), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 0), 1)
    print "right sleeve done"
else:
	cv2.putText(image, "no model in image...stay tuned for clothing" + "#{}".format(i + 1), (0, 0), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 0), 1)

# show labelled image
cv2.imshow("Feature Detection", image)
cv2.waitKey(0)
