import cv2
#reading the image
# img=cv2.imread("last.jpg")
# #showing the image
# cv2.imshow('gfg', img)
# #waiting using waitkey method
# cv2.waitKey(1000)
#displaying videos
# cap=cv2.VideoCapture('doctors.mp4')
# while(cap.isOpened()):
#     ret,frame=cap.read()
#     if ret==True:
#         cv2.imshow('frame',frame)
#         if cv2.waitKey(16) & 0xFF==ord('q'):
#             break
#access local camera
cap=cv2.VideoCapture(0)
# while(cap.isOpened()):
#     ret,frame=cap.read()
#     if ret==True:
#         cv2.imshow('frame',frame)
#         if cv2.waitKey(16) & 0xFF==ord('q'):
#             break

import cv2
img=cv2.imread('last.jpg',-1)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
key=cv2.waitKey(0)
print(key)
cv2.destroyAllWindows()

