import cv2

ssg = cv2.imread("sausage.png", cv2.IMREAD_UNCHANGED)

cv2.imshow("sausage", ssg)
cv2.waitkey(0)
cv2.destroyAllWindows()