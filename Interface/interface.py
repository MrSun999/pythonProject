# -- ** -- UTF-8
import tkinter as tk
import tkinter.messagebox
from db.connectDB import connect_DB

app = tkinter.Tk()


class GUI():

    def mainInterface(self):  # 主界面
        loginbutten = tk.Button(app, text='登录', bg='white', font=("Arial,12"), width=12, height=1, command=self.login)
        registerbutten = tk.Button(app, text='注册', bg='white', font=("Arial,12"), width=12, height=1,
                                   command=self.register)
        quitmainloopbutten = tk.Button(app, text='退出', bg='white', font=("Arial,12"), width=12, height=1,
                                       command=self.quit_mainloop)
        loginbutten.place(x=260, y=200), registerbutten.place(x=260, y=240), quitmainloopbutten.place(x=260, y=280)
        loginbutten.pack(), registerbutten.pack(), quitmainloopbutten.pack()
        app.mainloop()

    def login(self):
        login = tk.Toplevel(app)
        login.title('用户登录')
        login.geometry("600x400")
        tk.Label(login, text="欢迎登录", font=("KaiTi", 40)).place(x=200, y=20)
        tk.Label(login, text='管理员姓名：', font=("Arial", 9)).place(x=80, y=120)
        tk.Label(login, text='管理员编号：', font=('Arial', 9)).place(x=80, y=150)
        entry1 = tk.Entry(login, font=("Arial, 9"), width=46)
        entry2 = tk.Entry(login, font=("Arial, 8"), width=46, show="*")
        entry1.pack()
        entry2.pack()
        entry1.place(x=180, y=120, width=350, height=25)
        entry2.place(x=180, y=150, width=350, height=25)

        def user_check():
            user_name = entry1.get()
            user_code = entry2.get()
            content = "SELECT * FROM user_info WHERE user_name = '%s';" % user_name
            # print('执行sql:', content)
            data = connect_DB(database="vaccine-test", content=content)
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

        tk.Button(login, text="登录", bg='white', font=("Arial,9"), width=12, height=0, command=user_check).place(x=250,
                                                                                                                y=250)

    def register(self):
        register = tk.Toplevel(app)
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
                connect_DB(database="vaccine-test", content=content)
                tkinter.messagebox.showinfo(title="信息", message="注册成功！")

        tk.Button(register, text="注册", bg='white', font=("Arial,9"), width=12, height=0, command=user_register).place(
            x=250, y=250)

    def quit_mainloop(self):
        app.destroy()

    def options(self):  # 功能区主界面
        options = tk.Toplevel(app)
        options.title('功能选项')
        options.geometry("600x500")
        tk.Label(options, text="欢迎使用！", font=("KaiTi", 40)).place(x=180, y=15)
        tk.Button(options, text='新建疫苗信息', bg='white', font=("Arial,12"), width=20, height=2,
                  command=self.addVaccInfo).place(x=100, y=100)
        tk.Button(options, text='新建疫苗分配信息', bg='white', font=("Arial,12"), width=20, height=2,
                  command=self.addVaccineDistrInfo).place(x=100, y=160)
        tk.Button(options, text='新建疫苗养护信息', bg='white', font=("Arial,12"), width=20, height=2,
                  command=self.addVaccineMaintenanceInfo).place(x=100, y=220)
        tk.Button(options, text='新建接种人员信息', bg='white', font=("Arial,12"), width=20, height=2,
                  command=self.addVcinationPersonInfo).place(x=100, y=280)
        tk.Button(options, text='查询疫苗分配信息', bg='white', font=("Arial,12"), width=20, height=2,
                  command=self.vaccineDistrInfoQuery).place(x=100, y=340)
        tk.Button(options, text='查询疫苗养护信息', bg='white', font=("Arial,12"), width=20, height=2,
                  command=self.vaccinationMaintenanceInfoQuery).place(x=320, y=100)
        tk.Button(options, text='查询接种人员信息', bg='white', font=("Arial,12"), width=20, height=2,
                  command=self.vaccinationPersonInfoQuery).place(x=320, y=160)
        tk.Button(options, text='查询疫苗信息', bg='white', font=("Arial,12"), width=20, height=2,
                  command=self.vaccineInfoQuery).place(x=320, y=220)
        tk.Button(options, text='修改疫苗信息', bg='white', font=("Arial,12"), width=20, height=2,
                  command=self.modifyVaccineInfo).place(x=320, y=280)
        tk.Button(options, text='删除疫苗信息', bg='white', font=("Arial,12"), width=20, height=2,
                  command=self.delVaccineInfo).place(x=320, y=340)

    def addVaccInfo(self):
        add_vacc_info = tk.Toplevel(app)
        add_vacc_info.title('添加疫苗信息')
        add_vacc_info.geometry("600x400")
        tk.Label(add_vacc_info, text='疫苗批号：', font=("Arial", 9)).place(x=80, y=60)
        tk.Label(add_vacc_info, text='疫苗名称：', font=('Arial', 9)).place(x=80, y=90)
        tk.Label(add_vacc_info, text='企业名称：', font=('Arial', 9)).place(x=80, y=120)
        tk.Label(add_vacc_info, text='企业编号：', font=('Arial', 9)).place(x=80, y=150)
        tk.Label(add_vacc_info, text='    规格：', font=('Arial', 9)).place(x=80, y=180)
        tk.Label(add_vacc_info, text='    进价：', font=('Arial', 9)).place(x=80, y=210)
        tk.Label(add_vacc_info, text='  预售价：', font=('Arial', 9)).place(x=80, y=240)
        tk.Label(add_vacc_info, text='企业上限：', font=('Arial', 9)).place(x=80, y=270)
        tk.Label(add_vacc_info, text='企业下限：', font=('Arial', 9)).place(x=80, y=300)
        entry1 = tk.Entry(add_vacc_info, font=("Arial, 9"), width=46)
        entry2 = tk.Entry(add_vacc_info, font=("Arial, 9"), width=46)
        entry3 = tk.Entry(add_vacc_info, font=("Arial, 9"), width=46)
        entry4 = tk.Entry(add_vacc_info, font=("Arial, 9"), width=46)
        entry5 = tk.Entry(add_vacc_info, font=("Arial, 9"), width=46)
        entry6 = tk.Entry(add_vacc_info, font=("Arial, 9"), width=46)
        entry7 = tk.Entry(add_vacc_info, font=("Arial, 9"), width=46)
        entry8 = tk.Entry(add_vacc_info, font=("Arial, 9"), width=46)
        entry9 = tk.Entry(add_vacc_info, font=("Arial, 9"), width=46)
        entry1.pack(), entry2.pack(), entry3.pack(), entry4.pack(),
        entry5.pack(), entry6.pack(), entry7.pack(), entry8.pack(),
        entry9.pack()
        entry1.place(x=180, y=60, width=350), entry2.place(x=180, y=90, width=350), entry3.place(x=180, y=120,
                                                                                                 width=350),
        entry4.place(x=180, y=150, width=350), entry5.place(x=180, y=180, width=350), entry6.place(x=180, y=210,
                                                                                                   width=350),
        entry7.place(x=180, y=240, width=350), entry8.place(x=180, y=270, width=350), entry9.place(x=180, y=300,
                                                                                                   width=350)

        def add():
            text1 = entry1.get()
            text2 = entry2.get()
            text3 = entry3.get()
            text4 = entry4.get()
            text5 = entry5.get()
            text6 = entry6.get()
            text7 = entry7.get()
            text8 = entry8.get()
            text9 = entry9.get()
            content = "INSERT INTO vaccine_info (" \
                      "vaccine_num, vaccine_name, company_name, company_num, size, buy_price, pre_sale_price, limit_up, limit_down" \
                      ")" \
                      " VALUES (%s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (
                          text1, text2, text3, text4, text5, text6, text7, text8, text9)
            connect_DB(database = "vaccine-test", content=content)
            tkinter.messagebox.showinfo(title="信息", message="数据添加成功！")

        def clear():
            entry1.delete(0, "end"),entry2.delete(0, "end"),entry3.delete(0, "end"),entry4.delete(0, "end")
            entry5.delete(0, "end"),entry6.delete(0, "end"),entry7.delete(0, "end"),entry8.delete(0, "end")
            tkinter.messagebox.showinfo(title="信息", message="数据已清空，请继续添加！")

        tk.Button(add_vacc_info, text="添加", bg='white', font=("Arial,9"), width=9, height=0, command=add).place(x=400, y=360)
        tk.Button(add_vacc_info, text="清空", bg='white', font=("Arial,9"), width=9, height=0, command=clear).place(x=160, y=360)

    def addVaccineDistrInfo(self):
        pass

    def addVaccineMaintenanceInfo(self):
        pass

    def addVcinationPersonInfo(self):
        pass

    def vaccineDistrInfoQuery(self):
        query = tk.Toplevel(app)
        query.title('信息查询')
        query.geometry("600x400")
        entry = tk.Entry(query, width=30)
        entry.pack()
        entry.place(x=200, y=80)
        tk.Label(query, text="请输入疫苗分配单号：", font=("Arial", 9)).place(x=50, y=80)
        tk.Label(query, text='查询结果：', font=('Arial', 9)).place(x=50, y=120)
        text1 = tk.Text(query, width=50, height=20)
        text1.pack()
        text1.place(x=150, y=120)

        def base_query():
            vaccine_distr_num = entry.get()
            print(vaccine_distr_num)
            content = "SELECT * FROM vaccine_distr_info WHERE vaccine_distr_num = %s;" % vaccine_distr_num
            data = connect_DB(database="vaccine-test", content=content)
            text1.delete(1.0, "end")
            text1.insert(chars="{}".format(data), index="insert")

        tk.Button(query, text='查询', bg='white', font=("Arial,12"), width=9, height=0, command=base_query).place(x=450,y=75)

    def vaccinationMaintenanceInfoQuery(self):
        query = tk.Toplevel(app)
        query.title('疫苗养护信息查询')
        query.geometry("600x400")
        entry = tk.Entry(query, width=30)
        entry.pack()
        entry.place(x=200, y=80)
        tk.Label(query, text="请输入疫苗养护批号：", font=("Arial", 9)).place(x=50, y=80)
        tk.Label(query, text='查询结果：', font=('Arial', 9)).place(x=50, y=120)
        text1 = tk.Text(query, width=50, height=20)
        text1.pack()
        text1.place(x=150, y=120)

        def base_query():
            vaccine_maintenance_num = entry.get()
            print(vaccine_maintenance_num)
            content = "SELECT * FROM vaccine_maintenance_info WHERE vaccine_maintenance_num = %s;" % vaccine_maintenance_num
            data = self.connect_DBS(database="vaccine_info", content=content)
            text1.delete(1.0, "end")
            text1.insert(chars="{}".format(data), index="insert")

        tk.Button(query, text='查询', bg='white', font=("Arial,12"), width=9, height=0, command=base_query).place(x=450,y=75)

    def vaccinationPersonInfoQuery(self):
        pass

    def vaccineInfoQuery(self):
        pass

    def modifyVaccineInfo(self):
        pass

    def delVaccineInfo(self):
        pass
