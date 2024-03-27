import pyautogui
import time
import keyboard


while not keyboard.is_pressed('esc'):
    time.sleep(0.5)

    try :
        if pyautogui.locateOnScreen('./img/red.png', region=(1073, 591, 70, 25), confidence=0.8) != None:
            if pyautogui.locateOnScreen('./img/sell.png', region=(793, 797, 100, 40), confidence=0.8) != None:
                pyautogui.click(pyautogui.locateOnScreen('./img/sell.png', region=(793, 797, 100, 40), confidence=0.8))
    except :
        pass

    try :
        if pyautogui.locateOnScreen('./img/green.png', region=(1073, 591, 70, 25), confidence=0.8) != None:
            if pyautogui.locateOnScreen('./img/equip.png', region=(978, 795, 120, 50), confidence=0.8) != None:
                pyautogui.click(pyautogui.locateOnScreen('./img/equip.png', region=(978, 795, 120, 50), confidence=0.8))
    except :
        pass
