This code connects your camera from your laptop to your python program. Then it starts rolling. Where you can see a video of yourself. To quit type the letter q on the keyboard. 

Feel free to use this code I don't care I was just messing around with it



IMPORTANT NOTE: 
  Look at this line of code here:
  camera = cv2.VideoCapture(1)
  
  If your camera isn't working, change the number 1 to 0. If it still isn't working, then try 2, 3, 4, etc. 
  My camera on my MacBook is considered number 1. 
  
  Normally the count starts at 0 then goes up.
  So for example:
  Camera 0: Built-in camera on laptop, computer, etc
  Camera 1: Web Camera, or some other attached camera.
  Camera 2: Another attached camera (3 Cameras connected to your laptop)
  Camera 3: Another attached camera (4 cameras connected to your laptop)

  Note: 
    The number only signifies which camera is going to videotape you. You can't run all of them at once with that one line. 
  
  The number goes up for each camera you add. So, for most people, change the code to be this: 
  camera = cv2.VideoCapture(0)
