# -- ** -- UTF-8
import tkinter as tk
import tkinter.messagebox
from atexit import register
from Tools.scripts.serve import app
from db.connectDB import connect_DB

class GUI():

    def mainInterface(self):
        tk.Button(app, text='登录', bg='white', font=("Arial,12"), width=12, height=1, command=self.login).place(x=260,y=200)
        tk.Button(app, text='注册', bg='white', font=("Arial,12"), width=12, height=1, command=self.register).place(x=260,y=240)
        tk.Button(app, text='退出', bg='white', font=("Arial,12"), width=12, height=1, command=self.quit_mainloop).place(x=260, y=280)

    def login(self):
        login = tk.Toplevel(app)
        login.title('用户登录')
        login.geometry("600x400")
        tk.Label(login, text="欢迎登录", font=("KaiTi", 40)).place(x=200, y=20)
        tk.Label(login, text='管理员姓名：', font=("Arial", 9)).place(x=80, y=120)
        tk.Label(login, text='管理员编号：', font=('Arial', 9)).place(x=80, y=150)
        entry1 = tk.Entry(login, font=("Arial, 9"), width=46)
        entry2 = tk.Entry(login, font=("Arial, 9"), width=46, show="*")
        entry1.pack()
        entry2.pack()
        entry1.place(x=180, y=120, width=350, height=25)
        entry2.place(x=180, y=150, width=350, height=25)

        def user_check():
            user_name = entry1.get()
            user_code = entry2.get()
            content = "SELECT * FROM user_info WHERE user_name = '%s';" % user_name
            data = connect_DB(database="vaccine_info", content=content)
            try:
                if user_name == data[1] and user_code == data[2]:
                    tkinter.messagebox.showinfo(title="信息", message="欢迎登录！")
                    self.options()
                elif user_name != data[1]:
                    tkinter.messagebox.showerror(title="错误", message="请注册后再进行登录！")
                elif user_name == data[1] and user_code != data[2]:
                    tkinter.messagebox.showerror(title="错误", message="密码错误！")
            except TypeError:
                tkinter.messagebox.showerror(title="错误", message="请注册后再进行登录！")
        tk.Button(self.login(), text="登录", bg='white', font=("Arial,9"), width=12, height=0, command=user_check).place(x=250, y=250)

    def register(self):
        register = tkinter.Toplevel(app)
        register.title('用户注册')
        register.geometry("600x400")
        tk.Label(register, text="欢迎注册", font=("KaiTi", 40)).place(x=200, y=20)
        tk.Label(register, text='添加管理员姓名：', font=("Arial", 9)).place(x=80, y=120)
        tk.Label(register, text='确认管理员编号：', font=('Arial', 9)).place(x=80, y=150)
        entry1 = tk.Entry(register, font=("Arial, 9"), width=46, )
        entry2 = tk.Entry(register, font=("Arial, 9"), width=46, )
        entry1.pack()
        entry2.pack()
        entry1.place(x=180, y=120, width=350, height=25)
        entry2.place(x=180, y=150, width=350, height=25)
        def user_register():
            user_name = entry1.get()
            user_code = entry2.get()
            if user_name == "" or user_code == "":
                tkinter.messagebox.showwarning(title="警告", message="用户名或密码不能为空！")
            else:
                content = "INSERT INTO user_info (user_name, user_code) VALUES ('%s', '%s');" % (user_name, user_code)
                connect_DB(database="vaccine_info", content=content)
                tkinter.messagebox.showinfo(title="信息", message="注册成功！")
        tk.Button(register, text="注册", bg='white', font=("Arial,9"), width=12, height=0, command=user_register).place(x=250,y=250)
    def quit_mainloop(self):
        pass