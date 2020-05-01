import cv2
import numpy as np

item = cv2.imread(r'C:\Users\leemh\Desktop\opencv-snake-game-master\opencv-snake-game-master\sausage.png', cv2.IMREAD_ANYCOLOR)
# item = cv2.imdecode(np.fromfile(ssg, np.uint8), -1)

number_list = item.shape  # 이미지의 3차원 배열을 변수에 저장
number = int(number_list[2]) - 1
item_mask = item[:, :, number]
item_mask_inv = cv2.bitwise_not(item_mask)
item = item[:, :, 0:3]
item = cv2.resize(item, (40, 40), interpolation=cv2.INTER_AREA)
item_mask = cv2.resize(item_mask, (40, 40), interpolation=cv2.INTER_AREA)
item_mask_inv = cv2.resize(item_mask_inv, (40, 40), interpolation=cv2.INTER_AREA)

def mouse_callback(event, x, y, flags, param):
    print('마우스 위치는 x :', x, 'y: ', y)
    roi = img[y:y + 40, x:x + 40]
    img_bg = cv2.bitwise_and(roi, roi, mask=item_mask_inv)
    img_fg = cv2.bitwise_and(item, item, mask=item_mask)
    dst = cv2.add(img_bg, img_fg)
    img[y:y + 40, x:x + 40] = dst


img = np.zeros((480, 640, 3), np.uint8)

cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

while True:
    cv2.imshow('image', img)

    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        print('end')
        break





cv2.destroyAllWindows()
