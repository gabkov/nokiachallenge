import numpy as np
import cv2
#import time

#file_name = 'C:/Users/csiga/Downloads/nokiavideos/pivideo3.mp4'

#cap = cv2.VideoCapture(file_name)

# time.sleep(2)

imageMat = np.array((4, 5, 4), np.uint8)
cap = cv2.VideoCapture(0)
cap.open('http://192.168.0.190:8080/stream/video.mjpeg')
cap.read(imageMat)


# Define the codec and create VideoWriter object

fourcc = cv2.VideoWriter_fourcc(*'XVID')
#fourcc = cv2.cv.CV_FOURCC(*'X264')
#out = cv2.VideoWriter('outputvideo4.avi', fourcc, 20.0, (640, 480))
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
#out = cv2.VideoWriter('video.avi', -1, 25, (640, 480))

while True:
    ret, frame = cap.read()

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    out.write(frame)

    cv2.imshow('train-path', frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
