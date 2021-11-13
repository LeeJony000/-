import pyautogui
import pyperclip
import time
from Get_exact_coordinates import get_exact_coordinates


def auto_message():
    with open("message.txt", "rb+") as f:
        byt = f.read()
        byt = byt.decode("utf-8")
        x, y = get_exact_coordinates()
        for line in byt.split("\n") * 10:
            if line:
                # pyautogui.mouseDown()  按下鼠标按键（左键）
                # pyautogui.mouseUp()  释放鼠标按键（左键）
                # pyautogui.click()  向计算机发送虚拟的鼠标点击(click()函数只是前面两个函数调用的方便封装),默认在当前光标位置，使用鼠标左键点击
                pyautogui.click(x, y)  # 鼠标定位到聊天窗口并点击
                # pyautogui.click([x,y,button='left/right/middle'])，在(x,y)处点击鼠标左键、右键、中键
                # 但不推荐使用这种方法，下面这种方法效果更好
                # pyautogui.moveTo(x,y,duration=t) duration指定鼠标光标移动到目标位置
                # pyautogui.click()
                pyperclip.copy(line)
                pyautogui.hotkey("ctrl", "v")  # 粘贴，mac电脑则把ctrl换成command
                pyautogui.typewrite("\n")  # 发送
                time.sleep(0.2)


if __name__ == "__main__":
    auto_message()
