Image Classification using OpenCV and sklearn

## Install python modules needed to run
	$ pip install matplotlib
	$ pip intall scipy
	$ pip install sklearn

## Training the classifier
	$ python findFeatures.py -t dataset/train/

## Testing the classifier for all test images
	$ python getClass.py -t dataset/test 
	$ python getClass.py -t dataset/test --visualize
		
		The `--visualize` flag will display the image with the corresponding label printed on the image

## Testing a single image
	$ python getClass.py -i dataset/test/aeroplane/test_1.jpg --visualize


# Troubleshooting

AttributeError: 'LinearSVC' object has no attribute 'classes_'
	retrain the model. 

".DS_Store is not a directory"
	go into test and train directories of dataset
	$ ls -a
	if there are .DS_Store files, remove them
	$ rm .DS_Store
