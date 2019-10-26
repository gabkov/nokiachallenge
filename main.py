import cv2
import time

file_name = 'C:/Users/csiga/Downloads/nokiavideos/pivideo3.mp4'

cap = cv2.VideoCapture(file_name)

time.sleep(2)

# Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('outputvideo.avi',fourcc, 20.0, (640,480))

while True:
    ret, frame = cap.read()

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #out.write(frame)

    cv2.imshow('train-path', frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
#out.release()
cv2.destroyAllWindows()
