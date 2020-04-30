# _*_ coding:utf-8 _*_
import cv2
import numpy as np
from time import time
import random
import math
import webcolors
import random
import threading

font = cv2.FONT_HERSHEY_COMPLEX_SMALL  # 글꼴을 손글씨 글꼴로 지정

apple = cv2.imread("images/apple.png", -1)
grape = cv2.imread("images/grape.png", -1)
orange = cv2.imread("images/orange.png", -1)
strawberry = cv2.imread("images/strawberry.png", -1)
shit = cv2.imread("images/shit.png", -1)
bomb = cv2.imread("images/bomb.png", -1)
items = [apple, grape, orange, strawberry, shit, bomb]
item = strawberry

'''
def changeitem():
    # 과일 이미지들을 저장할 리스트
    fitem = random.sample(items, 1)

    return np.array(fitem)
'''

'''
if changeitem() == 'apple':
    item = cv2.imread("images/apple.png", -1)
elif changeitem() == 'grape':
    item = cv2.imread("images/grape.png", -1)
elif changeitem() == 'orange':
    item = cv2.imread("images/orange.png", -1)
elif changeitem() == 'strawberry':
    item = cv2.imread("images/strawberry.png", -1)
elif changeitem() == 'shit':
    item = cv2.imread("images/shit.png", -1)
elif changeitem() == 'bomb':
    item = cv2.imread("images/bomb.png", -1)
'''

item_mask = item[:, :, 3]
item_mask_inv = cv2.bitwise_not(item_mask)
item = item[:, :, 0:3]
item = cv2.resize(item, (40, 40), interpolation=cv2.INTER_AREA)
item_mask = cv2.resize(item_mask, (40, 40), interpolation=cv2.INTER_AREA)
item_mask_inv = cv2.resize(item_mask_inv, (40, 40), interpolation=cv2.INTER_AREA)

'''
apple = cv2.imread("apple.png", -1)                 #cv2.imread = 이미지 읽기
apple_mask = apple[:, :, 3]                         #불러온 apple 이미지를 ???하여 apple_mask
apple_mask_inv = cv2.bitwise_not(apple_mask)        #색상 bitwise not 연산 - 색이 반대로 보임
apple = apple[:, :, 0:3]                            #???
apple = cv2.resize(apple, (40, 40), interpolation=cv2.INTER_AREA)                       #apple 이미지 크기 재설정(이미지 축소?)
apple_mask = cv2.resize(apple_mask, (40, 40), interpolation=cv2.INTER_AREA)             #apple_mask 이미지 크기 재설정
apple_mask_inv = cv2.resize(apple_mask_inv, (40, 40), interpolation=cv2.INTER_AREA)     #apple_mask_inv 이미지 크기 재설정
'''

# 여기서 아이템 교체 실행?
# changeitem()

blank_img = np.zeros((480, 640, 3), np.uint8)  # 0으로 초기화된 480*640 size 배열 blank_img

video = cv2.VideoCapture(0)  # 디바이스로부터 카메라 촬영 영상을 불러옴
kernel_erode = np.ones((4, 4), np.uint8)  # np.ones : 1로 초기화된 배열 생성
kernel_close = np.ones((15, 15), np.uint8)
# 딱풀 색 설정
color = 'yellow'
rgb = webcolors.name_to_rgb(color)  # 입력받은 색상은 rgb 값으로 변환해서 반환
red = rgb.red
blue = rgb.blue
green = rgb.green

lower_upper = []


def color_convert(r, bl, g):
    co = np.uint8([[[bl, g, r]]])  # 색상을 정수형 숫자로 변환하여 저장
    hsv_color = cv2.cvtColor(co, cv2.COLOR_BGR2HSV)  # 이미지를 hsv로 변환

    hue = hsv_color[0][0][0]
    lower_upper.append([hue - 10, 100, 100])
    lower_upper.append([hue + 10, 255, 255])
    return lower_upper


def detect_color(h):
    lu = color_convert(red, blue, green)
    lower = np.array(lu[0])
    upper = np.array(lu[1])
    mask = cv2.inRange(h, lower, upper)
    mask = cv2.erode(mask, kernel_erode, iterations=1)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel_close)
    return mask


def orientation(p, q, r):
    val = int(((q[1] - p[1]) * (r[0] - q[0])) - ((q[0] - p[0]) * (r[1] - q[1])))
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2


def intersect(p, q, r, s):
    o1 = orientation(p, q, r)
    o2 = orientation(p, q, s)
    o3 = orientation(r, s, p)
    o4 = orientation(r, s, q)
    if o1 != o2 and o3 != o4:
        return True

    return False


# 시간 반복용 flag 변수
end = False

count = 0


# 점수 줄이기 함수
def score_decrease(second=5.0):
    global end, score, count
    if end:
        return
    if count != 0:
        score -= 10
    count += 1

    threading.Timer(second, score_decrease, [second]).start()


start_time = int(time())
# score 처음 선언 부분
q, snake_len, score, temp = 0, 200, 0, 1
point_x, point_y = 0, 0
last_point_x, last_point_y, dist, length = 0, 0, 0, 0
points = []
list_len = []
random_x = random.randint(10, 550)
random_y = random.randint(10, 400)
a, b, c, d = [], [], [], []

# 일정시간 경과 뒤 점수 감소하도록 조절!!!
score_decrease(5)

while 1:
    xr, yr, wr, hr = 0, 0, 0, 0
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)
    if q == 0 and point_x != 0 and point_y != 0:
        last_point_x = point_x
        last_point_y = point_y
        q = 1

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = detect_color(hsv)
    # finding contours
    contour, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # drawing rectangle around the accepted blob
    try:
        for i in range(0, 10):
            xr, yr, wr, hr = cv2.boundingRect(contour[i])
            if (wr * hr) > 2000:
                break
    except:
        pass

    cv2.rectangle(frame, (xr, yr), (xr + wr, yr + hr), (0, 0, 255), 2)

    point_x = int(xr + (wr / 2))
    point_y = int(yr + (hr / 2))

    dist = int(math.sqrt(pow((last_point_x - point_x), 2) + pow((last_point_y - point_y), 2)))
    if point_x != 0 and point_y != 0 and dist > 5:
        list_len.append(dist)
        length += dist
        last_point_x = point_x
        last_point_y = point_y
        points.append([point_x, point_y])

    if length >= snake_len:
        for i in range(len(list_len)):
            length -= list_len[0]
            list_len.pop(0)
            points.pop(0)
            if length <= snake_len:
                break

    blank_img = np.zeros((480, 640, 3), np.uint8)

    for i, j in enumerate(points):
        if i == 0:
            continue
        cv2.line(blank_img, (points[i - 1][0], points[i - 1][1]), (j[0], j[1]), (blue, green, red), 5)
    cv2.circle(blank_img, (last_point_x, last_point_y), 5, (10, 200, 150), -1)

    # 여기서 스코어 처리!
    if random_x < last_point_x < (random_x + 40) and random_y < last_point_y < (random_y + 40):
        score += 50
        random_x = random.randint(10, 550)
        random_y = random.randint(10, 400)

    frame = cv2.add(frame, blank_img)


    roi = frame[random_y:random_y + 40, random_x:random_x + 40]
    img_bg = cv2.bitwise_and(roi, roi, mask=item_mask_inv)
    img_fg = cv2.bitwise_and(item, item, mask=item_mask)
    dst = cv2.add(img_bg, img_fg)
    frame[random_y:random_y + 40, random_x:random_x + 40] = dst
    cv2.putText(frame, str("Score - " + str(score)), (250, 450), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

    if len(points) > 5:

        b = points[len(points) - 2]
        a = points[len(points) - 1]
        for i in range(len(points) - 3):
            c = points[i]
            d = points[i + 1]
            if intersect(a, b, c, d) and len(c) != 0 and len(d) != 0:
                temp = 0
                break
        if temp == 0:
            break

    cv2.imshow("frame", frame)

    if (int(time()) - start_time) > 1:
        snake_len += 40
        start_time = int(time())
    key = cv2.waitKey(1)
    if key == 27:
        break
    if score < 0:
        break

video.release()
cv2.destroyAllWindows()
cv2.putText(frame, str("Game Over!"), (100, 230), font, 3, (255, 0, 0), 3, cv2.LINE_AA)
cv2.putText(frame, str("Press any key to Exit."), (180, 260), font, 1, (255, 200, 0), 2, cv2.LINE_AA)
cv2.imshow("frame", frame)
k = cv2.waitKey(0)
cv2.destroyAllWindows()
