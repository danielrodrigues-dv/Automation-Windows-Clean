import pyautogui
from time import sleep


def clean():
    # First step
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('temp')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('del')
    sleep(1)
    pyautogui.hotkey('enter')
    pyautogui.hotkey('alt', 'F4')

    # Second step
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('%temp%')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('del')
    sleep(1)
    pyautogui.press('left')
    pyautogui.hotkey('enter')
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.hotkey('enter')
    sleep(6)
    pyautogui.hotkey('alt', 'F4')
    print('Limpeza finalizada')


clean()
