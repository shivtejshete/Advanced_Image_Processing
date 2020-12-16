import cv2
import os

###to work with video cam on the device use 0 or -1 to point at resource
cap = cv2.VideoCapture(0)   #Video file path can also be used

#to save the video captured, use cv2.VideoWriter
fourcc= cv2.VideoWriter_fourcc(*'mp4v')        #compression code used for video codec, eg avi, mp4 etc
print(fourcc)   #for mp4v = 1983148141 this is the fourcc code
out = cv2.VideoWriter('sample_output.mp4',fourcc, 20 , (640,480) )

print(cap.isOpened())

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            cv2.imshow("frame", frame)
            out.write(frame)

            if cv2.waitKey(2) & 0xFF==ord('q'):
                break   #waitKey waits for 2 sec for user key input, if not give takes -1, ord gets unicode of char
        else:
            print('stream_ended')
            break
except:
    print('done with video')

cap.release()  #release hold on camera if specified
cv2.destroyWindow('frame')   #remove all display windows
print('done')
