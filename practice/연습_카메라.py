import cv2

#cv2.VideoCapture로 카메라에서 영상 받아옴
#n은 카메라 장치 번호, 노트북 기본캠은 0번
capture = cv2.VideoCapture(0)
#capture.set으로 카메로 속성 설정
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#while 문으로 영상출력 반복
while True:
    #카메라 상태 받아오기
    #ret = 카메라 상태 저장됨-작동 시 true
    #frame = 현재 프레임 저장
    ret, frame = capture.read()
    #윈도우 창에 이미지 띄움, 프레임 제목 표시
    cv2.imshow("Test Frame", frame)
    #waitkey로 타임마다 아스키 형태의 입력값 받아옴
    #어떤 키라도 눌린다면 창 종료
    if cv2.waitKey(1) > 0:
        break

#메모리 해제
capture.release()
#모든 창 닫기
cv2.destroyAllWindows()