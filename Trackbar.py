import numpy as np
import cv2

#black image with given size
img = np.zeros((300,512,3), dtype=np.uint8)
cv2.namedWindow('image')

#create a callback function to operate on trackbar value change
def nothing(x):
    print(x)

#create trackbar
cv2.createTrackbar('B','image', 0, 255, nothing)  #unique trackbar identified by its name
cv2.createTrackbar('G','image', 0, 255, nothing)  #unique trackbar identified by its name
cv2.createTrackbar('R','image', 0, 255, nothing)  #unique trackbar identified by its name

#adding switch trackbar so that changes to image will be made when switch is on
switch_bar_name = '1:ON/0:OFF'
cv2.createTrackbar(switch_bar_name,'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)

    key = cv2.waitKey(1)
    if key == 27:
        break

    #get trackbar position which are accessible through out this while loop
    b= cv2.getTrackbarPos('B','image')
    g = cv2.getTrackbarPos('G', 'image')
    r = cv2.getTrackbarPos('R', 'image')

    #use of switch trackbar
    s= cv2.getTrackbarPos(switch_bar_name, 'image')
    if s==0:
        img[:]=0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()
