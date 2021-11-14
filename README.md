# 项目文件：

+ Get_exact_coordinates.py

  ​	每 2s 记录并打印当前鼠标的坐标，并进行判断：

  ​		当前鼠标坐标和上次鼠标坐标相同时，说明用户已经将鼠标放置到聊天框中等待脚本开始发送消息，返回当前坐标信息

  ​		当前鼠标坐标和上次鼠标坐标不同时，说明用户鼠标处在运动状态，依然处在准备阶段

+ auto_message.py

  ​	Get_exact_coordinates.py返回坐标信息后，打开message.txt文本文件，鼠标根据坐标进行点击定位到聊天框

  ​	将文本文件中的每行内容复制到剪贴板，再粘贴到聊天框中发送文本文件中的内容，默认重复发送十遍文本中的内容

+ message.txt

  ​	发送的内容，用户可自行设置，以回车符(\n)分隔

# 运行环境
+ Python 3.0 +
# 运行脚本
+ python auto_message.py
