import cv2
import numpy as np

img = cv2.imread(r'C:\Users\SShete2\PycharmProjects\pythonProject1\lena.jpg', 1)
print(img.shape)
cv2.imshow('frame', img)

#top left side corner is (0,0), and X-rows +ve, Y-down +ve
img = cv2.line(img, (0,0),(255,255), (131,19,71),1)  #line
img = cv2.arrowedLine(img, (50,250), (500,500), (15,44,35), 1)   #arrow line
img = cv2.rectangle(img, (50,50), (150,200), (200,200,0), -1)  #thickness = 1 to ..,-1 fill with BGR, X1=l-vertex,X2-R-bottom Vertex
img = cv2.circle(img,(200,45), 30,(13,14,24), -1)  #circle

font = cv2.FONT_HERSHEY_PLAIN      #font type
img = cv2.putText(img, 'Sample Text', (15,300), font, 1 , (14,242,24), 1)
cv2.imshow('frame1', img)

#zeros method of numpy
img2 = np.zeros([512,512,3], dtype=np.uint8)   #np.uint - necessary (unassigned int, for image pixel val (0-255-8bits)
print(img2.shape)

cv2.imshow('Zeros_frame',img2.reshape(512,512,3))
img2=cv2.putText(img2,'Zeros Matrix', (0,150) , cv2.FONT_HERSHEY_PLAIN, 3,(255,255,255), 5)

cv2.imshow('texted_zeros', img2)


if cv2.waitKey(0)==27:   #27 is key ASCII
    cv2.destroyAllWindows()


