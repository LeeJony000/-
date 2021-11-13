import os
import time
import pyautogui


def get_exact_coordinates():
    old_positionStr = ""
    try:
        while True:
            print("Press Ctrl-C to stop")
            x, y = pyautogui.position()  # 确定鼠标当前位置，返回x,y坐标的元组
            positionStr = "(" + str(x).rjust(4) + "," + str(y).rjust(4) + ")"  # Python rjust() 返回一个原字符串右对齐,并使用空格填充至长度
            print(positionStr)
            if old_positionStr == positionStr:
                return x, y
            else:
                old_positionStr = positionStr
            time.sleep(2)
            os.system('cls')
    except KeyboardInterrupt:
        print('end...')


if __name__ == "__main__":
    x, y = get_exact_coordinates()
