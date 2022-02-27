# FindingWaldo

This project is the main assignment of undergraduate coursework called 'Team-based Engineering'. 
Although the name is 'Team-based Engineering', this project is an individual project.

In this project, I created and trained my own Haar Cascade by using OpenCV on top of Python to find Waldo from 'Where's Waldo' series. I used 57 positive and 1100 negative images which I collected myself from the internet. The goal of this project is to identify Waldo from a webcam/camera input.

In order to make the cascade robust to any distortion, I created additional positive samples (double the negatives) from all the positive images by using the following command which ran automatically by the script in `commands.py`:

`opencv_createsamples -img src_img/pos/waldo{0}.png -bg bg.txt -info info/info{0}/info{0}.lst -pngoutput info -maxxangle 0.5 + -maxyangle 0.5 -num {1}`

{0} &#8594; str(num), num++

{1} &#8594; int(2*number_of_negative_images / num_pf_positive_images)

All the `info.lst` are merged to create the vector file with the following command:

`opencv_createsamples -info info/info.lst -num 2200 -w 25 -h 25 -vec positives.vec`

Finally I trained the cascade with the following command:

`opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 2000 -numNeg 1000 -numStages 10 -w 25 -h 25`

After the cascade is trained, I try using some test images to test out the result. However,....

<strong>... the result is not satisfiable 😢. </strong>

Might be caused by the images collected (low resolution, number of images, etc..). Not sure, gonna look into it and try again 💪. Might consider other tools such as TensorFlow or Keras in the future 👀.

Note: I used OpenCV ver 3.2.0 in Ubuntu 18.04 LTS as the newest version removed the createsamples and traincascade features...

### Code Files and Folders Description

Folders:
* `data` - contains the trained `cascade.xml` file
* `info` - the positive images samples directory
* `result` - the result images directory
* `src_img` - location of positive and negative images as well as the test images

Files:
* `bg.txt` - text file containing the list of negative images
* `positives.vec` - the vector file containing the list of positive images description
* `commands.py` - contains script to create samples and the vector file
* `runCommands.py` - run the above file scripts'

### References

OpenCV Documentation

https://docs.opencv.org/3.2.0/dc/d88/tutorial_traincascade.html

Creating your own Haar Cascade OpenCV Python Tutorial - sentdex

https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/

Crazy Data Science - Where is Wally / Waldo ?

https://www.youtube.com/watch?v=wKt3EwHgRtM