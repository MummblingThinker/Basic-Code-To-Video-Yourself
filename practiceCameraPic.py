#Camera library 
import cv2

camera = cv2.VideoCapture(1)

#keeps running until the user types the letter q
while True:
    success, image = camera.read()

    #if camera not found break out of loop
    if not success:
        print("Couldn't access camera")
        break

    #imshow() is a cv2 function that basically takes a picture
        #Because it is in a loop these images combine into one to make it look like a video
    cv2.imshow("Card Scanner", image)

    #Escape while loop when q is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Don't forget these this closes the camera window and stops recording 
camera.release()
cv2.destroyAllWindows()