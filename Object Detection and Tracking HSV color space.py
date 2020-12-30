import numpy as np
import cv2

#sample function - dummy callback function
def nothing(x):
    pass

#capture live video
cap = cv2.VideoCapture(0)

#window for trackbars
cv2.namedWindow('Track')
#defining trackbars to control HSV values of given video stream
cv2.createTrackbar('L_HUE', 'Track', 0, 255, nothing)
cv2.createTrackbar('L_Sat', 'Track', 0, 255, nothing)
cv2.createTrackbar('L_Val', 'Track', 0, 255, nothing)
cv2.createTrackbar('H_HUE', 'Track', 255, 255, nothing)
cv2.createTrackbar('H_Sat', 'Track', 255, 255, nothing)
cv2.createTrackbar('H_Val', 'Track', 255, 255, nothing)


while cap.isOpened()==True :
    #read the video feed
    _, frame = cap.read()
    cv2.imshow('Actual_Feed', frame)

    #get current trackbar positions for every frame
    l_hue = cv2.getTrackbarPos('L_HUE', 'Track')
    l_sat = cv2.getTrackbarPos('L_Sat', 'Track')
    l_val = cv2.getTrackbarPos('L_Val', 'Track')
    h_hue = cv2.getTrackbarPos('H_HUE', 'Track')
    h_sat = cv2.getTrackbarPos('H_Sat', 'Track')
    h_val = cv2.getTrackbarPos('H_Val', 'Track')

    #convert the captured frame into HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  #Hue(0), Saturation(1) and Value(2)
    # print(hsv.shape)

    #trim video feed HSV to a range
    lower_bound = np.array([l_hue, l_sat, l_val])
    upper_bound = np.array([h_hue, h_sat, h_val])
    mask = cv2.inRange(hsv, lower_bound,upper_bound  )

    frame = cv2.bitwise_and(frame, frame,mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    # cv2.imshow('converted', hsv)



    key = cv2.waitKey(1)
    if key==27:
        break

cap.release()
cv2.destroyAllWindows()