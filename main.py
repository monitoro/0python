from helper import *
import pyautogui as pag
import mss, cv2
import numpy as np

# 아이콘 위치 좌표값
left_icon_pos = {'left': 2688, 'top': 681, 'width': 100, 'height':100}
right_icon_pos = {'left': 2906, 'top': 681, 'width': 100, 'height':100}

# 버튼 위치

left_button = [2688,681]
right_button = [3050,865]



while True:
    x, y = pag.position()
    position_str = 'X:' + str(x) + ' Y:' + str(y)
    print(position_str)

# # get_colors / click / macro

# while True:
#     with mss.mss() as sct:
#         left_img = np.array(sct.grab(left_icon_pos))[:,:,:3]
#         right_img = np.array(sct.grab(right_icon_pos))[:,:,:3]

#         cv2.imshow('left_img',left_img)
#         cv2.imshow('right_img',right_img)
#         cv2.waitKey(0)