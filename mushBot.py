import pyautogui
import time
import keyboard


while not keyboard.is_pressed('esc'):
    time.sleep(0.5)

    try :
        if pyautogui.locateOnScreen('./img/red.png', region=(1084, 625, 25, 25), confidence=0.8) != None:
            if pyautogui.locateOnScreen('./img/sell.png', region=(810, 835, 70, 30), confidence=0.8) != None:
                pyautogui.click(pyautogui.locateOnScreen('./img/sell.png', region=(793, 797, 100, 40), confidence=0.8))
    except :
        pass

    try :
        if pyautogui.locateOnScreen('./img/green.png', region=(1084, 625, 25, 25), confidence=0.8) != None:
            if pyautogui.locateOnScreen('./img/equip.png', region=(991, 832, 80, 40), confidence=0.8) != None:
                pyautogui.click(pyautogui.locateOnScreen('./img/equip.png', region=(991, 832, 80, 40), confidence=0.8))
    except :
        pass
