# USAGE
# python feature_detector.py --image images/person_01.jpg

# import the necessary packages
import argparse
import cv2
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
ap.add_argument("-c", "--cascade",
	default="haarcascade_frontalface_default.xml",
	help="path to feature detector haar cascade")
ap.add_argument("-f", "--feature",
    default="Face",
    help="label for features discovered in image")
args = vars(ap.parse_args())

# load the input image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# load the feature detector Haar cascade, then detect input image
detector = cv2.CascadeClassifier(args["cascade"])
rects = detector.detectMultiScale(gray, scaleFactor=1.3,
	minNeighbors=5, minSize=(20, 20))

# loop over detected features and draw a rectangle surrounding each
for (i, (x, y, w, h)) in enumerate(rects):
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.putText(image, args["feature"] + "#{}".format(i + 1), (x, y - 10),
    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2),
        cv2.rectangle(image, (x, y + h), (x + w, y + 2*h), (0, 0, 255), 2)
        cv2.putText(image, "shirt" + "#{}".format(i + 1), (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2),


# show the detected cat faces
cv2.imshow("Feature Detection", image)
cv2.waitKey(0)
