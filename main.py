import numpy as np
import cv2
import time


#file_name = 'C:/Users/csiga/Downloads/nokiavideos/pivideo3.mp4'
file_name = 'D:/codes/hackaton/nokia/output5.avi'

cap = cv2.VideoCapture(file_name)

# time.sleep(2)

#imageMat = np.array((4, 5, 4), np.uint8)
#cap = cv2.VideoCapture(0)
# cap.open('http://192.168.0.190:8080/stream/video.mjpeg')
# cap.read(imageMat)


# Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('new3.avi', fourcc, 20.0,(int(cap.get(3)), int(cap.get(4))))

while True:
    ret, frame = cap.read()

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red color
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

    # Blue color
    low_blue = np.array([100, 50, 50])
    high_blue = np.array([246, 96, 57])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # yellow color
    low_yellow = np.array([25, 146, 190])
    high_yellow = np.array([62, 174, 250])
    yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
    yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)

    # master color
    low = np.array([152, 35, 12])
    high = np.array([255, 255, 147])
    mask = cv2.inRange(hsv_frame, low, high)
    barmi = cv2.bitwise_and(frame, frame, mask=mask)

    # grey color
    low_grey = np.array([103, 86, 65])
    high_grey = np.array([145, 133, 128])
    mask_grey = cv2.inRange(hsv_frame, low_grey, high_grey)
    grey = cv2.bitwise_and(frame, frame, mask=mask_grey)

    # create NumPy arrays from the boundaries
    lower = np.array([103, 86, 65], dtype="uint8")
    upper = np.array([145, 133, 128], dtype="uint8")

    # find the colors within the specified boundaries and apply
    # the mask
    mask_grey2 = cv2.inRange(frame, lower, upper)
    output = cv2.bitwise_and(frame, frame, mask=mask_grey2)

    #imageOut = np.hstack([frame, red, blue, yellow])
    imageOut = np.hstack([frame])

    cv2.rectangle(imageOut,(50,50),(250,240),(0,255,0),1)

    cv2.imshow("Frame", imageOut)
    #cv2.imshow("Red", red)
    #cv2.imshow("Blue", blue)
    #cv2.imshow("Yellow", yellow)

    # out.write(frame)

    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cap.release()
# out.release()
cv2.destroyAllWindows()
