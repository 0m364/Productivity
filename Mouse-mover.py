## prerequisite...
 pip install pyautogui
##############################
#Save the shit after the hashes in a text  #
# then rename it to whatever you want.py#
# then you type $ python3 filename.py      #
# 👀                                                                  #
###############################

import pyautogui
import random
import time

def move_mouse():
    screen_width, screen_height = pyautogui.size()
    while True:
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        pyautogui.moveTo(x, y, duration=0.5)
        time.sleep(10)

move_mouse()