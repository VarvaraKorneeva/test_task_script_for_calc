import os
import time

import pyautogui


def click_button(button_img_file):
    button_location = pyautogui.locateOnScreen(button_img_file, confidence=0.9)
    button_center = pyautogui.center(button_location)
    pyautogui.click(*button_center)


os.startfile(r'C:\Windows\System32\calc.exe')
time.sleep(5)

example = [
    r'elements_screenshots\button_1.png',
    r'elements_screenshots\button_2.png',
    r'elements_screenshots\button_plus.png',
    r'elements_screenshots\button_7.png',
    r'elements_screenshots\button_equals.png',
]
for button in example:
    click_button(button)
