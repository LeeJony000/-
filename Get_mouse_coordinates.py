import os
import time
import pyautogui as pag

try:
    while True:
        print("Press Ctrl-C to stop")
        x, y = pag.position()
        positionStr = "(" + str(x).rjust(4) + "," + str(y).rjust(4) + ")"
        print(positionStr)
        time.sleep(0.2)
        os.system('cls')
except KeyboardInterrupt:
    print('end...')
