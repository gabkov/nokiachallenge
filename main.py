import numpy as np
import cv2
#import time

#file_name = 'C:/Users/csiga/Downloads/nokiavideos/pivideo3.mp4'
#file_name = 'D:/codes/hackaton/nokia/output3.avi'

#cap = cv2.VideoCapture(file_name)

# time.sleep(2)

#imageMat = np.array((4, 5, 4), np.uint8)
cap = cv2.VideoCapture(0)
cap.open('http://192.168.0.190:8080/stream/video.mjpeg')
# cap.read(imageMat)


# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output7.avi', fourcc, 20.0,(int(cap.get(3)), int(cap.get(4))))

while True:
    ret, frame = cap.read()

    out.write(frame)

    cv2.imshow('train-path', frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
