import cv2
import datetime

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
print(cap.get(3))
print(cap.get(4))

while(True):
    ret,vd = cap.read()
    # put text in image show
    font = cv2.FONT_HERSHEY_COMPLEX
    datet = str(datetime.datetime.now())
    text = 'width: '+ str(cap.get(3))+',height: '+str(cap.get(4))
    vd = cv2.putText(vd,datet,(10,100),font,3,
                        (50,50,200),2,cv2.LINE_8)
    # put text in image show
    cv2.imshow("Testing",vd)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()