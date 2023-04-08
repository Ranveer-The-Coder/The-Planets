import cv2
img = cv2.imread('solar-system.jpg')

cv2.putText(img,"Sun",(110,80),cv2.FONT_HERSHEY_COMPLEX,3,(2,109,247))
cv2.putText(img,"Mercury",(120,180),cv2.FONT_HERSHEY_COMPLEX,0.5,(89,81,89))
cv2.putText(img,"Venus",(190,260),cv2.FONT_HERSHEY_COMPLEX,0.5,(7,158,245))
cv2.putText(img,"Earth",(280,170),cv2.FONT_HERSHEY_COMPLEX,0.5,(236,252,3))
cv2.putText(img,"Mars",(380,260),cv2.FONT_HERSHEY_COMPLEX,0.5,(21,21,171))
cv2.putText(img,"Jupiter",(560,55),cv2.FONT_HERSHEY_COMPLEX,0.5,(151,217,204))
cv2.putText(img,"Saturn",(700,270),cv2.FONT_HERSHEY_COMPLEX,0.5,(151,217,204))
cv2.putText(img,"Uranus",(960,140),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Neptune",(1111,140),cv2.FONT_HERSHEY_COMPLEX,0.5,(168,58,24))

cv2.imwrite('Solar_systemwithname.jpg',img)
cv2.imshow('output',img)
cv2.waitKey(0)