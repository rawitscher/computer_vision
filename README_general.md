## Instructions for downloading OpenCV 3 and binding Python 2.7 + OpenCV 3
## Below is a waaay simplified version of: 
			http://www.pyimagesearch.com/2016/11/28/macos-install-opencv-3-and-python-2-7/

	1. Make sure that Xcode has command line tools installed 
		$ sudo xcode-select --install


	2. Install homebrew 
		$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
		$ brew update


	3. Update bash profile to avoid weird segfault issues..not 100% sure why
		$ nano ~/.bash_profile

		# add the following lines to EOF, ctrl+O (save), ctrl+X (exit) #
			# Homebrew
			export PATH=/usr/local/bin:$PATH

		# manually source the bash profile
			$ source ~/.bash_profile


	4. Install and link python if you haven't yet *with homebrew*, this is seperate from system version
		$ brew install python
		$ brew linkapps python


	5. Tap homebrew science repo
		$ brew tap homebrew/science


	6. Install OpenCV 3 (takes a bit)
		$ brew install opencv3 --with-contrib --HEAD


	7.  Create a .pth file to pseudo sym-link python and packages
		$ echo /usr/local/opt/opencv3/lib/python2.7/site-packages >> /usr/local/lib/python2.7/site-packages/opencv3.pth


	8. Verify that all is well (these commands should give these responses)
	Install OpenCV 3 on macOS with Homebrew (the easy way)Shell
		$ python
		Python 2.7.13
		[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
		Type "help", "copyright", "credits" or "license" for more information.
		>>> import cv2
		>>> cv2.__version__
		'3.2.0-dev'
		>>>

	9. Install numpy if you don't have it; OpenCV uses it 
		$ pip install numpy


		