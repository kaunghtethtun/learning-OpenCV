import cv2

img = cv2.imread('lena.jpg',1)

img = cv2.line(img,(100,200),(100,300),(0,0,255),5)
img = cv2.rectangle(img,(200,0),(400,500),(0,255,0),5)
img = cv2.circle(img,(400,100),40,(255,0,0),-1)
text = 'testing blah blah'
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img,text,(100,500),font,1,(200,110,50),1,cv2.LINE_AA)
cv2.imshow('image',img)

cv2.waitKey()
cv2.destroyAllWindows()