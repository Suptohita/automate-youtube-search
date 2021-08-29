import pyautogui
import time

# python -m pyautogui(to know cursor position)

pyautogui.hotkey('win', 'd')

pyautogui.press('winleft')
time.sleep(0.5)

pyautogui.typewrite('chrome')
time.sleep(0.5)

pyautogui.press('enter')  # open chrome
time.sleep(5)

pyautogui.hotkey('win', 'up')
pyautogui.hotkey('win', 'down')
pyautogui.hotkey('win', 'up')
time.sleep(1)

pyautogui.typewrite('Youtube.com')
pyautogui.press('enter')
time.sleep(3)


pyautogui.click(700, 131)
pyautogui.typewrite('Bebe Rexha')
pyautogui.press('enter')
time.sleep(4)

pyautogui.click(902, 249)

