import cv2

ssg = cv2.imread(r"C:\Users\leemh\Desktop\opencv-snake-game-master\opencv-snake-game-master\sausage.png", cv2.IMREAD_COLOR)

cv2.imshow("sausage", ssg)
cv2.waitKey(0)
cv2.destroyAllWindows()
