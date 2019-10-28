import numpy as np
import cv2
import time
import track_tracking

local = True
save_to_file = False

def main_loop():
    if local:
        file_name = './videos/output12.avi'
        cap = cv2.VideoCapture(file_name)
    else:
        cap = cv2.VideoCapture(0)
        cap.open('http://192.168.0.190:8080/stream/video.mjpeg')

    if save_to_file:
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('new5.avi', fourcc, 20.0,(int(cap.get(3)), int(cap.get(4))))

    frame_counter = 0
    detect_counter = 0
    last = "possible"


    width = cap.get(3)
    height = cap.get(4)

    cropped_width_start = int(width/4)
    cropped_width_end = int(width/1.07)

    cropped_height_start = int(height/2.4)
    cropped_height_end = int(height/1.3)

    while True:
        ret, frame = cap.read()

        #frame = frame[80:300, 100:185]
        frame = frame[cropped_width_start:cropped_width_end, cropped_height_start: cropped_height_end]

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        lego_cascade = cv2.CascadeClassifier("./cascade/cascade.xml")


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
                    if not local:
                        track_tracking.possible_obstacle()
                    last = "possible"
            else:
                if last != "moved":
                    if not local:
                        track_tracking.obstacle_moved_away()
                    last = "moved"

            detect_counter = 0


        imageOut = np.hstack([frame])

        cv2.imshow("Frame", imageOut)
        if save_to_file:
            out.write(frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    if save_to_file:
        out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main_loop()