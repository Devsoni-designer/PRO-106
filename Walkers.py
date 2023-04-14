# import the opencv library
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Define a video capture object
cap = cv2.VideoCapture('walking.avi')

while(True):
   
    # Capture the video frame by frame
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    
    # Display the resulting frame
    
    for(x,y,w,h) in faces:
      cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
             
    cv2.imshow("Web cam", frame)   
    
    # Quit Window by Spacebar Key
    if cv2.waitKey(60) == 32:
        break

# After the loop release the cap object
cap.release()

# Destroy all the windows
cv2.destroyAllWindows()
