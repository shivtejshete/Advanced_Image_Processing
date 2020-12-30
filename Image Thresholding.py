import cv2
import numpy as np

img = cv2.imread('gradient.png')

_, th1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)  #converts image to binary - 0 to 255 value only
_, th2 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY_INV)  #inverse - value < thresh is 255 and vice versa
_, th3 = cv2.threshold(img, 100, 255, cv2.THRESH_TRUNC)  #until thresh it keeps the values as 0 and then it keeps
                                                        # same value of thresh for rest of image pixel values
_, th4 = cv2.threshold(img, 100, 255, cv2.THRESH_TOZERO)  #lower than thresh become zero, upper remain same as original
_, th5 = cv2.threshold(img, 100, 255, cv2.THRESH_TOZERO_INV)  #lower than thresh remain same, upper become zero


print(_)


cv2.imshow('frame_1', th1)
cv2.imshow('frame_2', th2)
cv2.imshow('frame_3', th3)
cv2.imshow('frame_4', th4)
cv2.imshow('frame_5', th5)

cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


