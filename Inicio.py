import cv2
import numpy as np
from Function1 import movility
#Video capture
cap = cv2.VideoCapture(0)
#Variables
value2=900
value1=0
d=0
f=0
#Classes
#Random square movements

#Functions



#Instance from Function1
c= movility(value1,value2,f)

while(True):
    ret, frame = cap.read()
    # Capture frame-by-frame
    
    # Gray theme
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.rectangle(frame, (30, 30), (300, 200), (0, 255, 0), 5)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    c.f=c.f+1
    c.mov(d,f)
    print("this is F", c.f)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
