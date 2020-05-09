# _*_ coding:utf-8 _*_
# 명환
import cv2
import numpy as np
from time import time
import random
import math
import webcolors
import threading # 시간(초) 측정
import os  # 파일 리스트 가져오기 위함

# 과일 아이템이 들어있는 경로 지정
path_fruits = r"images\fruits"
file_list_fruits = os.listdir(path_fruits)  # 폴더에 있는 모든 파일명을 리스트 형태로 저장
file_dir_list_fruits = []  # 사진별 상대경로를 담을 리스트

# 음식 아이템이 들어있는 경로 지정
path_foods = r"images\foods"
file_list_foods = os.listdir(path_foods)  # 폴더에 있는 모든 파일명을 리스트 형태로 저장
file_dir_list_foods = []  # 사진별 상대경로를 담을 리스트

# 감점 아이템이 들어있는 경로 지정
path_bad = r"images\bad_things"
file_list_bad = os.listdir(path_bad)  # 폴더에 있는 모든 파일명을 리스트 형태로 저장
file_dir_list_bad = []  # 사진별 상대경로를 담을 리스트

# 게임종료 아이템이 들어있는 경로 지정
path_end = r"images\game_end"
file_list_end = os.listdir(path_end)  # 폴더에 있는 모든 파일명을 리스트 형태로 저장
file_dir_list_end = []  # 사진별 상대경로를 담을 리스트


# 과일 아이템 사진별 상대경로 만들기
for i in range(len(file_list_fruits)):
    real_path_fruits = path_fruits + '\\' + file_list_fruits[i]
    file_dir_list_fruits.append(real_path_fruits)

# 음식 아이템 사진별 상대경로 만들기
for i in range(len(file_list_foods)):
    real_path_foods = path_foods + '\\' + file_list_foods[i]
    file_dir_list_foods.append(real_path_foods)

# 감점 아이템 사진별 상대경로 만들기
for i in range(len(file_list_bad)):
    real_path_bad = path_bad + '\\' + file_list_bad[i]
    file_dir_list_bad.append(real_path_bad)

# 게임종료 아이템 사진별 상대경로 만들기
for i in range(len(file_list_end)):
    real_path_end = path_end + '\\' + file_list_end[i]
    file_dir_list_end.append(real_path_end)

'''
print(file_dir_list_fruits)
print(file_dir_list_foods)
print(file_dir_list_bad)
print(file_dir_list_end)
'''

'''
cv2.imread는 파일경로에 한글과 같은 유니코드가 포함되어 있으면, 인식하지 못함.
따라서,cv2.imdecode를 사용해야 함.
'''
# font = cv2.FONT_HERSHEY_COMPLEX_SMALL
font = cv2.FONT_HERSHEY_DUPLEX

# 랜덤으로 아이템 이미지 불러오는 함수
def create_random_item():
    # 아이템 구분하는 flag 변수
    # 0 = 50점 추가 / 1 = 100점 추가 / 2 = 50점 감소 / -1 = 게임종료
    item_flag = 0

    fruits_item = str(random.choice(file_dir_list_fruits))
    foods_item = str(random.choice(file_dir_list_foods))
    bad_item = str(random.choice(file_dir_list_bad))
    end_item = str(random.choice(file_dir_list_end))

    selected_item = random.choice([fruits_item, fruits_item, fruits_item, foods_item, foods_item, bad_item, bad_item, end_item])

    if selected_item == fruits_item:
        item_flag = 0
    elif selected_item == foods_item:
        item_flag = 1
    elif selected_item == bad_item:
        item_flag = 2
    elif selected_item == end_item:
        item_flag = -1

    item = cv2.imdecode(np.fromfile(selected_item, np.uint8), -1)
    # item_pos = cv2.imdecode(np.fromfile(positive_item, np.uint8), -1)
    # item_neg = cv2.imdecode(np.fromfile(negative_item, np.uint8), -1)

    # print(item.shape)
    number_list = item.shape  # 이미지의 3차원 배열을 변수에 저장
    number = int(number_list[2]) - 1
    item_mask = item[:, :, number]
    item_mask_inv = cv2.bitwise_not(item_mask)
    item = item[:, :, 0:3]
    # print('item')
    # print(item)
    # print(item_flag)

    item = cv2.resize(item, (40, 40), interpolation=cv2.INTER_AREA)
    item_mask = cv2.resize(item_mask, (40, 40), interpolation=cv2.INTER_AREA)
    item_mask_inv = cv2.resize(item_mask_inv, (40, 40), interpolation=cv2.INTER_AREA)
    return item, item_mask, item_mask_inv, item_flag


# 시간 반복용 flag 변수
end = False # 점수가 0점 이하가 되면, 게임오버 되게 하는 변수
count = 0

# 일정 시간마다 점수 감점 함수
def score_decrease(second = 10.0):
    global end, score, count
    if end:
        return None
    if count != 0:
        score -= 10
    count += 1

    # 10초마다 score_decrease 함수 반복실행
    # print('timer 작동됨 1')
    threading.Timer(second, score_decrease, [second]).start() 
    # print('timer 작동됨 2')
     
# 3초마다 아이템을 변경하는 함수
def expired_item(second=3.0):
    global item, item_mask, item_mask_inv, item_flag, random_x, random_y
    if end:
        return None
    # print('random 함수 호출')
    item, item_mask, item_mask_inv, item_flag = create_random_item()
    random_x = random.randint(10, 550)
    random_y = random.randint(10, 400)
    # print('변경됨')
    
    #3초마다 expired_item 함수 반복실행
    # print('timer 작동됨 3')
    threading.Timer(second, expired_item, [second]).start()
    # print('timer 작동됨 4')
###################################################
'''
apple = cv2.imread("apple.png", -1)
apple_mask = apple[:, :, 3]
apple_mask_inv = cv2.bitwise_not(apple_mask)
apple = apple[:, :, 0:3]
print('apple')
print(apple)
apple = cv2.resize(apple, (40, 40), interpolation=cv2.INTER_AREA)
apple_mask = cv2.resize(apple_mask, (40, 40), interpolation=cv2.INTER_AREA)
apple_mask_inv = cv2.resize(apple_mask_inv, (40, 40), interpolation=cv2.INTER_AREA)
'''
blank_img = np.zeros((480, 640, 3), np.uint8)

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# 비디오 사이즈 고정용
video.set(3, 640)
video.set(4, 480)

kernel_erode = np.ones((4, 4), np.uint8)
kernel_close = np.ones((15, 15), np.uint8)
# 딱풀 색 설정
color = 'yellow'
rgb = webcolors.name_to_rgb(color)
red = rgb.red
blue = rgb.blue
green = rgb.green

lower_upper = []


def color_convert(r, bl, g):
    co = np.uint8([[[bl, g, r]]])
    hsv_color = cv2.cvtColor(co, cv2.COLOR_BGR2HSV)

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

##############################################
start_time = int(time())
q, snake_len, score, temp = 0, 200, 0, 1
point_x, point_y = 0, 0
last_point_x, last_point_y, dist, length = 0, 0, 0, 0
points = []
list_len = []
random_x = random.randint(10, 550)
random_y = random.randint(10, 400)
a, b, c, d = [], [], [], []
################# 추가 2 ###############
item, item_mask, item_mask_inv, item_flag = create_random_item()
#########################################

# 10초마다 점수 감소하도록 조절
score_decrease()
# 3초마다 아이템 변경되도록 조절
expired_item()


while True:
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

    print('xr: %d, yr: %d, wr: %d, hr: %d' % (xr, yr, wr, hr))
    
    # 플레이 오브젝트 인식선 그리기
    cv2.rectangle(frame, (xr, yr), (xr + wr, yr + hr), (0, 0, 255), 2)
    # 플레이 화면에 테두리 그리기
    cv2.rectangle(frame, (0, 0), (640, 480), (255, 0, 0), 10)

    point_x = int(xr + (wr / 2))
    point_y = int(yr + (hr / 2))


    dist = int(math.sqrt(pow((last_point_x - point_x), 2) + pow((last_point_y - point_y), 2)))
    ##########
    # print(dist)
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
        # 라인 그리는 부분
        cv2.line(blank_img, (points[i - 1][0], points[i - 1][1]), (j[0], j[1]), (blue, green, red), 5)
    cv2.circle(blank_img, (last_point_x, last_point_y), 5, (10, 200, 150), -1)
    ################################################################
    if random_x < last_point_x < (random_x + 40) and random_y < last_point_y < (random_y + 40):
        if item_flag == 0:
            score += 50
        elif item_flag == 1:
            score += 100
        elif item_flag == 2:
            score -= 50
        elif item_flag == -1:
            break

        random_x = random.randint(10, 550)
        random_y = random.randint(10, 400)
        ######################## 추가 3 ############
        item, item_mask, item_mask_inv, item_flag = create_random_item()  # 점수가 오를때마다,랜덤 아이템 생성 함수 호출
        # 아이템을 먹을 시, 뱀 몸통이 길어짐
        snake_len += 40
        # start_time = int(time())
        ############################################
    frame = cv2.add(frame, blank_img)
    '''
    roi = frame[random_y:random_y+40, random_x:random_x+40]
    img_bg = cv2.bitwise_and(roi, roi, mask=apple_mask_inv)
    img_fg = cv2.bitwise_and(apple, apple, mask=apple_mask)
    dst = cv2.add(img_bg, img_fg)
    frame[random_y:random_y + 40, random_x:random_x + 40] = dst
    cv2.putText(frame, str("Score - "+str(score)), (250, 450), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    
    ################추가 부분
    roi_2 = frame[random_y:random_y+40, random_x:random_x+40]
    img_bg2 = cv2.bitwise_and(roi_2, roi_2, mask=lemon_mask_inv)
    img_fg2 = cv2.bitwise_and(lemon, lemon, mask=lemon_mask)
    dst_2 = cv2.add(img_bg2, img_fg2)
    frame[random_y:random_y + 40, random_x:random_x + 40] = dst_2
    #cv2.putText(frame, str("Score - "+str(score)), (250, 450), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    #########################
    '''
    ############### 추가 4 ##################
    roi = frame[random_y:random_y + 40, random_x:random_x + 40]
    img_bg = cv2.bitwise_and(roi, roi, mask=item_mask_inv)
    img_fg = cv2.bitwise_and(item, item, mask=item_mask)
    dst = cv2.add(img_bg, img_fg)
    frame[random_y:random_y + 40, random_x:random_x + 40] = dst
    cv2.putText(frame, str("Score : " + str(score)), (240, 450), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    ##########################################
    # 플레이시간 표시
    # play_time = 'play time : ' + str(int(time())-start_time)
    play_time = int(time() - start_time)
    cv2.putText(frame, str('play time : ' + str(play_time)), (480, 50), font, 0.6, (0, 0, 0), 1, cv2.LINE_AA)

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

    # 시간마다 뱀 몸통 길이가 길어지는 것이 아니라, 아이템을 먹을 떄마다 길어지게 구현!
    '''
    if (int(time()) - start_time) > 1:
        snake_len += 40
        start_time = int(time())
    '''
    key = cv2.waitKey(1)
    if key == 27:
        break
    if score < 0:
        end = True
        break


    # 테두리에 닿으면 게임오버
    # xr, yr = x, y 좌표 / wr, hr = 사각형의 너비, 높이
    if play_time >= 10:
        if xr == 0 and yr == 0 and wr == 0 and hr == 0:
            break


############################################################################
# Threading 종료용 변수
end = True

video.release()
cv2.destroyAllWindows()
# 색상은 (B, G, R)로 표현!
cv2.putText(frame, str("Game Over!"), (50, 230), font, 3, (0, 0, 255), 3, cv2.LINE_AA)
cv2.putText(frame, str("Press any key to Exit"), (140, 280), font, 1, (0, 228, 255), 2, cv2.LINE_AA)
cv2.imshow("frame", frame)
k = cv2.waitKey(0)
cv2.destroyAllWindows()