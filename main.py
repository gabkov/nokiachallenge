import numpy as np
import cv2
import time

#file_name = 'C:/Users/csiga/Downloads/nokiavideos/pivideo3.mp4'
file_name = 'C:/Users/503127349/Desktop/Junction/pivideo3.mp4'

cap = cv2.VideoCapture(file_name)

time.sleep(2)

#imageMat = np.array((4, 5, 4), np.uint8)
#cap = cv2.VideoCapture(0)
# cap.open('http://192.168.0.190:8080/stream/video.mjpeg')
# cap.read(imageMat)


# Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output7.avi', fourcc, 20.0,(int(cap.get(3)), int(cap.get(4))))

while True:
    ret, image = cap.read()
# define the list of boundaries

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


    #blue
    low = np.array([100, 50, 50])
    high = np.array([140, 255, 255])

    #red
    redLow = np.array([0,100,100])
    redHigh = np.array([10,255,200])
    # find the colors within the specified boundaries and apply
    # the mask
    redMask = cv2.inRange(hsv, redLow, redHigh)
    blueMask = cv2.inRange(hsv, low, high)
    blueOutput = cv2.bitwise_and(image, image, mask=blueMask)
    redOutput = cv2.bitwise_and(image, image, mask=redMask)

    imageOut = np.hstack([image, blueOutput])

    # Display the resulting frame
    cv2.imshow('RGB', imageOut)

    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cap.release()
# out.release()
cv2.destroyAllWindows()
