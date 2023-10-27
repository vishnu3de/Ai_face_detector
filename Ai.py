import cv2

#load pre-trained data from haarcascade
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


#image for detection
image1=cv2.imread("image2.jpg")

#chnage image to grayscale because this support bw image
bwimage=cv2.cvtColor(image1, cv2.COLOR_RGB2GRAY)

#code for detect face coordinates
detectedimage=trained_face_data.detectMultiScale(bwimage)

#appply this coordinates into image
for (x,y,w,h) in detectedimage:
    cv2.rectangle(image1,(x,y),(x+w,y+h),(0,250,0), 2)

#img show
cv2.imshow("Face detection",image1)

cv2.waitKey()

print("code completed")