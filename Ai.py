import cv2

#load pre-trained data from haarcascade
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


#image for detection
image1=cv2.imread("face1.jpg")

#img show
cv2.imshow("Face detection",image1)

cv2.waitKey()

print("code completed")