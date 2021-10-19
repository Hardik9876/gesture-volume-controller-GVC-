# Gesture-volume-controller-GVC-

Gesture Control to change the volume of a computer. We first look into hand tracking and then we will use the hand landmarks to find gesture of our hand to change the volume. This project is module based which means we will be using a previously created hand module which makes the hand tracking very easy.
Volume control system using gestures
In this project we are going to learn how to use Gesture Control to change the volume of a computer. We first look into hand tracking and then we will use the hand landmarks to find gesture of our hand to change the volume.

Introduction :
This project is a use case of Hand Tracking technology.
As soon as the user shows up his hand in the camera the application detects it & draws a bounding box around the hand. 
Then according to the distance between user's Index finger and Thumb it displays the volume in the volume bar on the screen,
to set this volume as the system's volume user has to bend his pinky finger simultaneously.

Features
Can change your computer's volume based on your hand activity
Can track your hand in real-time
How to use?
Step 1: Clone this repository on your local computer

git clone https://github.com/Diwas524/Volume-Control-using-gesture.git

Step 2: Install all the requirements

pip install -r requirements.txt

Step 3: Run the program


Note: You might have to wait for sometime usually 1-2 minutes for program to start and work properly.


Special help
You might face issue with webcam not showing or something related to webcam. To solve it just change the value/webcam from python files.

cv2.VideoCapture(0)

You can increment the number 0 until you see your webcam.

Used opencv-python , mediapipe and pycaw Package for Controlling the System Volume using the Finger Gesture!

Purpose
The purpose of this project was to detect hands through webcam input  without using Machine/Deep Learning. 
With accuracy of 75% it works fine in every scenario and in low end pcs as well.


Main Libs Used :
OpenCV lib(for image processing and drawing)
Mediapipe lib(for Hand Tracking)
Pycaw lib(to link up with the system's volume)

For more info : https://google.github.io/mediapipe/solutions/hands.html
