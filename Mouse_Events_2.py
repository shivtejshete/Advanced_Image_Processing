
import cv2
import numpy as np


print([i for i in dir(cv2) if 'EVENT' in i])

#define a callback function after an event happen
def click_event(event, x, y , flags, param ):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 1,(255,255,150),-1)
        points.append((x,y))

        #test if the mouse is clicked on the screen
        if len(points)>=2:
            cv2.line(img, points[-2],points[-1],(255,40,80), 1)

        cv2.imshow('image', img)


#following image will act as base image
img = cv2.imread('lena.jpg', 1)
cv2.imshow('image',img)

points = []

#calling call back on given image after it becomes visible in 'image' window
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)  #wait for key from user
cv2.destroyAllWindows()







