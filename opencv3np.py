import numpy as np
import cv2


img = np.zeros([512,512,3],np.uint8) #make black image using np

img = cv2.rectangle(img,(10,100),(100,10),(200,200,50),1)
img = cv2.line(img,(10,100),(100,10),(100,50,100),1,cv2.LINE_AA)
img = cv2.arrowedLine(img,(10,100),(100,10),(50,50,100),2)
cv2.imshow("image",img)

cv2.waitKey()
cv2.destroyAllWindows()