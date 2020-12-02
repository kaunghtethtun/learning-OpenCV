import cv2
img = cv2.imread("lena.jpg",1)
cv2.imshow("image", img)

k = cv2.waitKey()
if k == 27:
    cv2.destroyAllWindows()
elif k == ord("s"):
    cv2.imwrite("image_copy.jpg",img)
    cv2.destroyAllWindows()
