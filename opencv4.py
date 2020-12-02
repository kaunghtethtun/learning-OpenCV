import cv2

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
print(cap.get(3))
print(cap.get(4))

while(True):
    ret,vd = cap.read()
    font = cv2.FONT_HERSHEY_COMPLEX
    text = 'width: '+ str(cap.get(3))+',height: '+str(cap.get(4))
    vd = cv2.putText(vd,text,(10,100),font,3,(50,50,200),3,cv2.LINE_AA)
    cv2.imshow("Testing",vd)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()