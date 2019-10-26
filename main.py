import numpy as np
import cv2
import time

#file_name = 'C:/Users/csiga/Downloads/nokiavideos/pivideo3.mp4'
file_name = 'D:/codes/hackaton/nokia/output6.avi'

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
    ret, frame = cap.read()

    # converting frame(img) from BGR (Blue-Green-Red) to HSV (hue-saturation-value)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # defining the range of Yellow color
    yellow_lower = np.array([22, 60, 200], np.uint8)
    yellow_upper = np.array([60, 255, 255], np.uint8)

    # finding the range yellow colour in the image
    yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)

    # Morphological transformation, Dilation
    kernal = np.ones((5, 5), "uint8")
    blue = cv2.dilate(yellow, kernal)
    res = cv2.bitwise_and(frame, frame, mask=yellow)

    # Tracking Colour (Yellow)
    contours,hierarchy =cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)

    #Display results
    cv2.imshow("Yellow", res)

    # out.write(frame)

    cv2.imshow('train-path', frame)

    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cap.release()
# out.release()
cv2.destroyAllWindows()
