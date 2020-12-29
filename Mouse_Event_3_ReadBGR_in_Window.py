
import cv2
import numpy as np

#this will open a new window once clicked on the image to showcase the point color

print([i for i in dir(cv2) if 'EVENT' in i])

#define a callback function after an event happen
def click_event(event, x, y , flags, param ):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x, y, 2]
        frame= np.zeros([512,512,3],dtype=np.uint8)
        frame[:,:,0], frame[:,:,1], frame[:,:,2] =blue, green, red

        cv2.imshow('second', frame)
        cv2.imshow('image', img)


#following image will act as base image
img = cv2.imread('lena.jpg', 1)
cv2.imshow('image',img)


#calling call back on given image after it becomes visible in 'image' window
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)  #wait for key from user
cv2.destroyAllWindows()







