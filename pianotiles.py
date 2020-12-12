# x 543  y 400
# x 631  y 400
# x 718  y 400
# x 808  y 400

from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con


for i in range(3):
    print(i)
    time.sleep(1)

print("\n O bot está funcionando")

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(543, 400)[0] == 0:
        click(543, 400)
    if pyautogui.pixel(631, 400)[0] == 0:
        click(631, 400)
    if pyautogui.pixel(718, 400)[0] == 0:
        click(718, 400)
    if pyautogui.pixel(808, 400)[0] == 0:
        click(808, 400)