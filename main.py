import numpy as np
import cv2
import time

#file_name = 'C:/Users/csiga/Downloads/nokiavideos/pivideo3.mp4'
#file_name = 'D:/codes/hackaton/nokia/output6.avi'

#cap = cv2.VideoCapture(file_name)

time.sleep(2)

#imageMat = np.array((4, 5, 4), np.uint8)
cap = cv2.VideoCapture(0)
cap.open('http://192.168.0.190:8080/stream/video.mjpeg')
# cap.read(imageMat)


# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output17.avi', fourcc, 20.0,(int(cap.get(3)), int(cap.get(4))))

while True:
    ret, frame = cap.read()
    #define the list of boundaries
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   # boundaries = [
       # ([86, 31, 4], [246, 96, 57])
        #([17, 15, 100], [50, 56, 200])
      #  ([22, 60, 200], [60, 174, 250])
        #([103, 86, 65], [145, 133, 128])
    #]

     # Red color
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

     # Blue color
    low_blue = np.array([86, 31, 4])
    high_blue = np.array( [246, 96, 57])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # yellow color
    low_yellow = np.array([25, 146, 190])
    high_yellow = np.array([62, 174, 250])
    green_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    cv2.imshow("Frame", frame)
    cv2.imshow("Red", red)
    cv2.imshow("Blue", blue)
    cv2.imshow("Yellow", green)

    out.write(frame)

    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
