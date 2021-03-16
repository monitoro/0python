import pyautogui as pag
import numpy as np
import mss, cv2


# 아이콘 위치 좌표값
left_icon_pos = {'left': 2688, 'top': 681, 'width': 100, 'height':100}
right_icon_pos = {'left': 2906, 'top': 681, 'width': 100, 'height':100}

# 버튼 위치

left_button = [2688,681]
right_button = [3050,865]



pag.PAUSE = 0.08


def get_colors(img):
    mean = np.mean(img, axis=(0,1)) # img 변수의 0번, 1번 축의 평균값을 구함
    result = None

    # 회색
    if mean[0] > 50 and mean[0] < 60 and mean[1] > 50 and mean[1] < 60 and mean[2] >50 and mean[2] <60:
        result = 'BOMB'

    elif mean[0] > 245 and mean[1] > 85 and mean[1] < 120 and mean[2] > 240:
        result = 'SWORD'

    elif mean[0] > 100 and mean[0] < 130 and mean[1] > 150 and mean[1] < 200 and mean[2] > 90 and mean[2] < 110:
        result = 'POISON'

    elif mean[0] > 210 and mean[0] < 230 and mean[1] > 210 and mean[1] < 230 and mean[2] > 120 and mean[2] < 150:
        result = 'JEWEL'

    return (result, mean)


          
def click(coords):
    pag.moveTo( x=coords[0], y=coords[1], duration=0.0 )
    pag.mouseDown()
    pag.mouseUp()

def macro(left_img, right_img, left_button, right_button):
    left_icon, m1 = get_colors(left_img)
    right_icon, m2 = get_colors(right_img)

    if left_icon == 'SWORD' and (right_icon == 'BOMB' or right_icon == 'POISON'):
        print('CLICK LEFT')
        click(left_button)

    elif right_icon == 'SWORD' and (left_icon == 'BOMB' or left_icon == 'POISON'):
        print('CLICK LEFT')
        click(right_button)

    elif left_icon == 'JEWEL' and right_icon == 'JEWEL':
        print('!!!!! FEVER !!!!!')
        click(left_button)
        click(right_button)

    else:
        print (left_icon,right_icon)
        print(m1, m2)

while True:
    # x,y = pag.position()
    # position_str = 'X: ' + str(x) + ' Y: ' + str(y) 
    # print(position_str)
    with mss.mss() as sct:

        left_img = np.array(sct.grab(left_icon_pos))[:,:,:3]
        right_img = np.array(sct.grab(right_icon_pos))[:,:,:3]
    macro(left_img,right_img,left_button,right_button)
      