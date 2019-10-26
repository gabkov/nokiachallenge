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
    ret, image = cap.read()
# define the list of boundaries
    boundaries = [
        ([86, 31, 4], [246, 96, 57])
        #([17, 15, 100], [50, 56, 200]),
        #([25, 146, 190], [62, 174, 250]),
        #([103, 86, 65], [145, 133, 128])
    ]

    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)

        imageOut = np.hstack([image, output])

    # Display the resulting frame
    cv2.imshow('RGB', imageOut)

    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cap.release()
# out.release()
cv2.destroyAllWindows()
