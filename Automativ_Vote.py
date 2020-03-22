import os
import pyautogui
import time
import sys

TIME0 = float(sys.argv[1])
TIME1 = float(sys.argv[2])

for i in range(5000):
    Command = os.system("chromium-browser -incognito http://yasouj.irib.ir/dena-40 &")
    time.sleep(TIME0)
    pyautogui.moveTo(1479,656)  # vote
    pyautogui.click(1479,656)
    time.sleep(.1)
    pyautogui.moveTo(1479,688) # send
    pyautogui.click(1479,688)
    time.sleep(TIME1) 
    pyautogui.moveTo(2039,17)  # close
    pyautogui.click(2039,17)
    time.sleep(.25)
    print('Vote number is : {} :)'.format(i))
    # pyautogui.moveTo(1150,500)  # vote  
    # 
    # pyautogui.click(777, 250)
