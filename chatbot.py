# 曹雪龙 18600961258 微信同号
# 改变标准输出的默认编码
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding = 'utf8')

import tkinter as tk
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # 用户名
        self.helloLabel = tk.Label(self, text='用户名')
        self.helloLabel.pack()
        self.nameInput = tk.Entry(self)
        self.nameInput.pack()
        # 用户密码
        self.helloLabel = tk.Label(self, text='密码')
        self.helloLabel.pack()
        self.passwordInput = tk.Entry(self)
        self.passwordInput.pack()
        # 登录按钮
        self.alertButton = tk.Button(self, text='登录', command=self.hello)
        self.alertButton.pack()
        # 登录后，将用户信息存储下来，再次登录进行对比
        # 退出按钮
        self.quit = tk.Button(self, text="取消", fg="red",
                              command= root.destroy)
        self.quit.pack(side="bottom")
        # 人脸识别
        self.faceButton = tk.Checkbutton(self, text='人脸识别')
        self.faceButton.pack()

        # 语音识别-语音聊天
        self.voiceButton = tk.Checkbutton(self, text='语音聊天')
        self.voiceButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        if (self.faceButton.getboolean ):
            name = name + ',请进行人脸识别'
        if (self.voiceButton.getboolean ):
            name = name + ',可以和机器人进行语音聊天！'
        else:
            name = name + ',只能和机器人进行文本聊天！'
        messagebox.showinfo('登录提示', 'Hello, %s' % name)

#app = Application()
root = tk.Tk()
app = Application(master=root)
# 设置窗口标题:
app.master.title('聊天机器人')
# 主消息循环:
app.mainloop()

# 待解决的问题
# 1、窗口要固定大小
# 2、窗口内控件的布局