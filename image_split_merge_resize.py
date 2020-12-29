import cv2

img = cv2.imread('lena.jpg', 1 )

print(img.shape)
print(img.size)
print(img.dtype)

b,g,r = cv2.split(img)    #splits image into multiple channels

print(b.shape, g.shape, r.shape)

img1 = cv2.merge((b,g,r))  #merges arrays together - stack them in line

cv2.imshow('image1', img1)

#ROI
#work with certain region only from the image
img11 = img1[300:350, 350:400]
img1[100:150, 200:250] = img11
cv2.imshow('image1', img1)

##Add two images together
logo= cv2.imread('opencv-logo.png', 1)   #this is a bigger sized image than lesa image
print(logo.shape)
cv2.imshow('logo', logo)

#resize the image
logo_resized = cv2.resize(logo, (512,512))
cv2.imshow('resized', logo_resized)

#add those two images which are of same size now
added = cv2.add(img1, logo_resized)
cv2.imshow('added', added)

#add images with certain weight for each image
weighted =  cv2.addWeighted(img1, 0.8,logo_resized,0.2,0)
cv2.imshow('weighted', weighted)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
