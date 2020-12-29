
import cv2
import numpy as np
#list of all mouse events present in cv2 package
# events = [ event for event in dir(cv2)]

print([i for i in dir(cv2) if 'EVENT' in i])

#define a callback function after an event happen
def click_event(event, x, y , flags, param ):
    if event == cv2.EVENT_LBUTTONDOWN:
        text = str(x) + ' , '+ str(y)
        cv2.putText(img, text, (x, y ) , cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,(250,250,0), 1)
        cv2.imshow('image', img)
    elif event==cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        text = str(blue)+' , '+str(green)+ ' , '+ str(red)
        cv2.putText(img, text,(x,y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,(100,100,100), 1)
        cv2.imshow('image', img)

# img = np.zeros([512,512,3], dtype=np.uint8)
# cv2.imshow('image',img)

#following image will act as base image
img = cv2.imread('lena.jpg', 1)
cv2.imshow('image',img)

#calling call back on given image after it becomes visible in 'image' window
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)  #wait for key from user
cv2.destroyAllWindows()







