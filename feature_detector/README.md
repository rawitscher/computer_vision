Minimum input to execute:
	$ python feature_detector.py --image /path_to_image/image.jpg

Additional inputs: 

	Default cascade is face detection, to use different cascade, add this argument.  The cascade must be in the current directory

	--cascade "new_cascade_name.xml"

	Default feature is face, to specify different feature, add this argument.

	--feature "name"


Example call:

To detect head and shoulders:
	$ python feature_detector.py --image images/image.jpg --cascade "haarcascade_mcs_upperbody.xml" --feature "head+shoulders"


If detecting anything smaller than a face (ie facial features), go into feature_detector.py and change the min size values in line 27.