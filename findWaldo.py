import numpy as np
import cv2

# Import the cascade file
findWaldoClassifier = cv2.CascadeClassifier('data/cascade.xml')

# Import the test image
test_img_num = 1
img = cv2.imread('src_img/test_img/'+str(test_img_num)+'.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Finding Waldo
waldo = findWaldoClassifier.detectMultiScale(gray, 1.105, 25, minSize=(25,25), maxSize=(50,50))

if waldo is ():
    print("Waldo not found")

# Give some borders if Waldo is found
for (x,y,w,h) in waldo:
    cv2.rectangle(img, (x,y), (x+w,y+h), (127,0,255), 2)

# Saving the result image
cv2.imwrite('res-'+str(test_img_num)+'.jpg',img)