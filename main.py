import numpy as np
import cv2
import time
import track_tracking


#file_name = 'C:/Users/csiga/Downloads/nokiavideos/pivideo3.mp4'
file_name = '/Users/bozsadam/PycharmProjects/nokiachallenge/output12.avi'

cap = cv2.VideoCapture(file_name)

#cap = cv2.VideoCapture(0)

# time.sleep(2)

#imageMat = np.array((4, 5, 4), np.uint8)
#cap = cv2.VideoCapture(0)
# cap.open('http://192.168.0.190:8080/stream/video.mjpeg')
# cap.read(imageMat)


# Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('new3.avi', fourcc, 20.0,(int(cap.get(3)), int(cap.get(4))))

frame_counter = 0
detect_counter = 0
last = "possible"

while True:
    ret, frame = cap.read()

    frame = frame[80:300, 100:185]

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    lego_cascade = cv2.CascadeClassifier("cascade.xml")


    legos = lego_cascade.detectMultiScale(gray, scaleFactor=1.01, minNeighbors=65)
    for(x, y, w, h) in legos:
        print("x: {} y: {} w: {} h: {}".format(x, y, w, h))
        if(w > 10):
            frame = cv2.rectangle(frame, (x, y), (x+y, y+h), (0, 255, 0), 1)
            detect_counter += 1


    frame_counter += 1
    if frame_counter % 5 == 0:
        if detect_counter >= 2:
            if last != "possible":
                track_tracking.possible_obstacle()
                last = "possible"
        else:
            if last != "moved":
                track_tracking.obstacle_moved_away()
                last = "moved"

        detect_counter = 0


    imageOut = np.hstack([frame])

    cv2.imshow("Frame", imageOut)

    # out.write(frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
# out.release()
cv2.destroyAllWindows()
