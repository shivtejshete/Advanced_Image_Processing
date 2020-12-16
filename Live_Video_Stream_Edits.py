import cv2
import random
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#set captured video with different properties
ht = cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 3000)
wd= cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3000)

counter = 0
counter_1 = 1
while cap.isOpened():
    ret, frame=cap.read()
    if ret==True:
        print(frame.shape)
        text = f'Width X Height : {str(wd)} X {str(ht)}'
        font= cv2.FONT_HERSHEY_COMPLEX_SMALL
        frame = cv2.putText(frame, text,(20,50), font, 1,(24,200,150), 1 )

        #printing date and time in real time on the video stream
        time= datetime.datetime.now()
        frame = cv2.putText(frame, str(time), (20, 100), font, 1, (24, 200, 150), 1)
        cv2.imshow('Frame1',frame)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
print('yes')
