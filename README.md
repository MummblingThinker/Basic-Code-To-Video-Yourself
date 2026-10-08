Created By AI
Written by Adam Larson (Human guy)

The purpose for me was to practice using the camera with coding


Description: This code connects your MacBook camera to your Python program. Then it starts rolling, and you can see a video of yourself. To quit, type the letter q on the keyboard. 

Feel free to use this code; I didn't make it, I just messed around with it. 


Steps to download the cv2 Library
1) Open computer terminal
2) Type in this: pip install opencv-python
3) Check it installed: python -c "import cv2; print(cv2.__version__)"
4) Close Visual Studio Code or wherever you type in Python code
5) Reopen it and try again


NOTE: If you are trying to connect a window's webcam: 
  Replace this code: camera = cv2.VideoCapture(1)
  With This code: cv2.VideoCapture(1, cv2.CAP_DSHOW)

  But it may not work depending on the webcam or the Windows version you have.
  So good luck with that.


IMPORTANT NOTE: 
  Look at this line of code here:
  camera = cv2.VideoCapture(1)
  
  If your camera isn't working, change the number 1 to 0. If it still isn't working, then try 2, 3, 4, etc. 
  My MacBook camera is number 1. 
        #I personally ran into this problem where I couldn't find my camera right away so I had to just guess and check
  
  Normally the count starts at 0 then goes up.
  So for example:
  Camera 0: Built-in camera on laptop, computer, etc
  Camera 1: Web Camera, or some other attached camera.
  Camera 2: Another attached camera (3 Cameras connected to your laptop)
  Camera 3: Another attached camera (4 cameras connected to your laptop)

  The number goes up for each camera you add. So, for most people, change the code to be this: 
  camera = cv2.VideoCapture(0)

Note: 
The number only signifies which camera is going to videotape you. You can't run all of them at once with that one line.
    Well you can try it with like a while loop counter thing, but that would make the video quality bad for all of the cameras. 
    Unless your computer is fast enough to run them all without it looking weird. But that could cause some other weird bugs too.


