import pyautogui
import random
import time

def move_mouse_and_type():
    screen_width, screen_height = pyautogui.size()
    while True:
   
     # Mouse movement

        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        pyautogui.moveTo(x, y, duration=0.5)

        # Keystrokes

        keys = ['backspace', 'space']
        key = random.choice(keys)
        pyautogui.press(key)

        time.sleep(30)

move_mouse_and_type()

#####
# 👀#
#####