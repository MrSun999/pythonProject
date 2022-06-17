# -- ** -- UTF-8
import tkinter as tk
import tkinter.messagebox
from db.connectDB import connect_DB

app = tkinter.Tk()


class GUI():

    def mainInterface(self):  # 主界面
        loginbutten = tk.Button(app, text='登录', bg='white', font=("Arial,12"), width=12, height=1, command=self.login)
        registerbutten = tk.Button(app, text='注册', bg='white', font=("Arial,12"), width=12, height=1,command=self.register)
        quitmainloopbutten = tk.Button(app, text='退出', bg='white', font=("Arial,12"), width=12, height=1,command=self.quit_mainloop)
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
        entry1.pack(),entry2.pack()
        entry1.place(x=180, y=120, width=350, height=25),entry2.place(x=180, y=150, width=350, height=25)

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

        tk.Button(login, text="登录", bg='white', font=("Arial,9"), width=12, height=0, command=user_check).place(x=250,y=250)

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

        tk.Button(register, text="注册", bg='white', font=("Arial,9"), width=12, height=0, command=user_register).place(x=250, y=250)

    def quit_mainloop(self):
        app.destroy()

    def options(self):  # 功能区主界面
        options = tk.Toplevel(app)
        options.title('功能选项')
        options.geometry("600x500")
        tk.Label(options, text="欢迎使用！", font=("KaiTi", 40)).place(x=180, y=15)
        tk.Button(options, text='新建疫苗信息', bg='white', font=("Arial,12"), width=20, height=2,command=self.addVaccInfo).place(x=100, y=100)
        tk.Button(options, text='新建疫苗分配信息', bg='white', font=("Arial,12"), width=20, height=2,command=self.addVaccineDistrInfo).place(x=100, y=160)
        tk.Button(options, text='新建疫苗养护信息', bg='white', font=("Arial,12"), width=20, height=2,command=self.addVaccineMaintenanceInfo).place(x=100, y=220)
        tk.Button(options, text='新建接种人员信息', bg='white', font=("Arial,12"), width=20, height=2,command=self.addVcinationPersonInfo).place(x=100, y=280)
        tk.Button(options, text='查询疫苗分配信息', bg='white', font=("Arial,12"), width=20, height=2,command=self.vaccineDistrInfoQuery).place(x=100, y=340)
        tk.Button(options, text='查询疫苗养护信息', bg='white', font=("Arial,12"), width=20, height=2,command=self.vaccinationMaintenanceInfoQuery).place(x=320, y=100)
        tk.Button(options, text='查询接种人员信息', bg='white', font=("Arial,12"), width=20, height=2,command=self.vaccinationPersonInfoQuery).place(x=320, y=160)
        tk.Button(options, text='查询疫苗信息', bg='white', font=("Arial,12"), width=20, height=2,command=self.vaccineInfoQuery).place(x=320, y=220)
        tk.Button(options, text='修改疫苗信息', bg='white', font=("Arial,12"), width=20, height=2,command=self.modifyVaccineInfo).place(x=320, y=280)
        tk.Button(options, text='删除疫苗信息', bg='white', font=("Arial,12"), width=20, height=2,command=self.delVaccineInfo).place(x=320, y=340)

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
        entry1.place(x=180, y=60, width=350), entry2.place(x=180, y=90, width=350), entry3.place(x=180, y=120,width=350),
        entry4.place(x=180, y=150, width=350), entry5.place(x=180, y=180, width=350), entry6.place(x=180, y=210,width=350),
        entry7.place(x=180, y=240, width=350), entry8.place(x=180, y=270, width=350), entry9.place(x=180, y=300,width=350)

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
        add_vaccine_distr_info = tk.Toplevel(app)
        add_vaccine_distr_info.title('添加疫苗分配信息')
        add_vaccine_distr_info.geometry("600x400")
        tk.Label(add_vaccine_distr_info, text='疫苗分配单号：', font=("Arial", 9)).place(x=80, y=60)
        tk.Label(add_vaccine_distr_info, text='       日期：', font=('Arial', 9)).place(x=80, y=90)
        tk.Label(add_vaccine_distr_info, text='   疫苗批号：', font=('Arial', 9)).place(x=80, y=120)
        tk.Label(add_vaccine_distr_info, text='   疫苗名称：', font=('Arial', 9)).place(x=80, y=150)
        tk.Label(add_vaccine_distr_info, text='   企业编号：', font=('Arial', 9)).place(x=80, y=180)
        tk.Label(add_vaccine_distr_info, text=' 质检员编号：', font=('Arial', 9)).place(x=80, y=210)
        tk.Label(add_vaccine_distr_info, text='      数量：', font=('Arial', 9)).place(x=80, y=240)
        entry1 = tk.Entry(add_vaccine_distr_info, font=("Arial, 9"), width=46)
        entry2 = tk.Entry(add_vaccine_distr_info, font=("Arial, 9"), width=46)
        entry3 = tk.Entry(add_vaccine_distr_info, font=("Arial, 9"), width=46)
        entry4 = tk.Entry(add_vaccine_distr_info, font=("Arial, 9"), width=46)
        entry5 = tk.Entry(add_vaccine_distr_info, font=("Arial, 9"), width=46)
        entry6 = tk.Entry(add_vaccine_distr_info, font=("Arial, 9"), width=46)
        entry7 = tk.Entry(add_vaccine_distr_info, font=("Arial, 9"), width=46)
        entry1.pack(),entry2.pack(),entry3.pack(),entry4.pack()
        entry5.pack(),entry6.pack(),entry7.pack()
        entry1.place(x=180, y=60, width=350),entry2.place(x=180, y=90, width=350),entry3.place(x=180, y=120, width=350)
        entry4.place(x=180, y=150, width=350),entry5.place(x=180, y=180, width=350),entry6.place(x=180, y=210, width=350)
        entry7.place(x=180, y=240, width=350)

        def add():
            text1 = entry1.get()
            text2 = entry2.get()
            text3 = entry3.get()
            text4 = entry4.get()
            text5 = entry5.get()
            text6 = entry6.get()
            text7 = entry7.get()
            content = "INSERT INTO vaccine_distr_info (" \
                      "vaccine_distr_num, date, vaccine_num, vaccine_name, company_num, operator_num, num" \
                      ")" \
                      " VALUES (%s, '%s', '%s', '%s', '%s', '%s', '%s');" % (
                          text1, text2, text3, text4, text5, text6, text7)
            connect_DB(database="vaccine-test", content=content)
            tkinter.messagebox.showinfo(title="信息", message="数据添加成功！")

        def clear():
            entry1.delete(0, "end")
            entry2.delete(0, "end")
            entry3.delete(0, "end")
            entry4.delete(0, "end")
            entry5.delete(0, "end")
            entry6.delete(0, "end")
            entry7.delete(0, "end")
            tkinter.messagebox.showinfo(title="信息", message="数据已清空，请继续添加！")

        tk.Button(add_vaccine_distr_info, text="添加", bg='white', font=("Arial,9"), width=9, height=0, command=add).place(x=400,y=360)
        tk.Button(add_vaccine_distr_info, text="清空", bg='white', font=("Arial,9"), width=9, height=0, command=clear).place( x=160,y=360)

    def addVaccineMaintenanceInfo(self):
        vaccine_maintenance_info = tk.Toplevel(app)
        vaccine_maintenance_info.title('添加疫苗养护信息')
        vaccine_maintenance_info.geometry("600x400")
        tk.Label(vaccine_maintenance_info, text='养护疫苗批号：', font=("Arial", 9)).place(x=80, y=60)
        tk.Label(vaccine_maintenance_info, text='养护疫苗名称：', font=('Arial', 9)).place(x=80, y=90)
        tk.Label(vaccine_maintenance_info, text=' 管理员编号：', font=('Arial', 9)).place(x=80, y=120)
        tk.Label(vaccine_maintenance_info, text=' 管理员姓名：', font=('Arial', 9)).place(x=80, y=150)
        tk.Label(vaccine_maintenance_info, text='   养护时间：', font=('Arial', 9)).place(x=80, y=180)
        tk.Label(vaccine_maintenance_info, text=' 冷藏室温度：', font=('Arial', 9)).place(x=80, y=210)
        tk.Label(vaccine_maintenance_info, text=' 冷冻室温度：', font=('Arial', 9)).place(x=80, y=240)
        tk.Label(vaccine_maintenance_info, text='设备运转情况：', font=('Arial', 9)).place(x=80, y=270)
        tk.Label(vaccine_maintenance_info, text='    是否报警：', font=('Arial', 9)).place(x=80, y=300)
        entry1 = tk.Entry(vaccine_maintenance_info, font=("Arial, 9"), width=46)
        entry2 = tk.Entry(vaccine_maintenance_info, font=("Arial, 9"), width=46)
        entry3 = tk.Entry(vaccine_maintenance_info, font=("Arial, 9"), width=46)
        entry4 = tk.Entry(vaccine_maintenance_info, font=("Arial, 9"), width=46)
        entry5 = tk.Entry(vaccine_maintenance_info, font=("Arial, 9"), width=46)
        entry6 = tk.Entry(vaccine_maintenance_info, font=("Arial, 9"), width=46)
        entry7 = tk.Entry(vaccine_maintenance_info, font=("Arial, 9"), width=46)
        entry8 = tk.Entry(vaccine_maintenance_info, font=("Arial, 9"), width=46)
        entry9 = tk.Entry(vaccine_maintenance_info, font=("Arial, 9"), width=46)
        entry1.pack(),entry2.pack(),entry3.pack(),entry4.pack(),entry5.pack(),entry6.pack()
        entry7.pack(),entry8.pack(),entry9.pack()
        entry1.place(x=180, y=60, width=350),entry2.place(x=180, y=90, width=350),entry3.place(x=180, y=120, width=350)
        entry4.place(x=180, y=150, width=350),entry5.place(x=180, y=180, width=350),entry6.place(x=180, y=210, width=350)
        entry7.place(x=180, y=240, width=350),entry8.place(x=180, y=270, width=350),entry9.place(x=180, y=300, width=350)

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
            content = "INSERT INTO vaccine_maintenance_info (" \
                      "vaccine_maintenance_num, vaccine_maintenance_name, admin_num, admin_name, maintenance_time, cold_storage_temp, freezer_temp, equipment_operation, alter_info" \
                      ")" \
                      " VALUES (%s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (
                          text1, text2, text3, text4, text5, text6, text7, text8, text9)
            connect_DB(database="vaccine-test", content=content)
            tkinter.messagebox.showinfo(title="信息", message="数据添加成功！")


        def clear():
            entry1.delete(0, "end")
            entry2.delete(0, "end")
            entry3.delete(0, "end")
            entry4.delete(0, "end")
            entry5.delete(0, "end")
            entry6.delete(0, "end")
            entry7.delete(0, "end")
            entry8.delete(0, "end")
            entry9.delete(0, "end")
            tkinter.messagebox.showinfo(title="信息", message="数据已清空，请继续添加！")


        tk.Button(vaccine_maintenance_info, text="添加", bg='white', font=("Arial,9"), width=9, height=0, command=add).place(x=400, y=360)
        tk.Button(vaccine_maintenance_info, text="清空", bg='white', font=("Arial,9"), width=9, height=0, command=clear).place(x=160, y=360)

    def addVcinationPersonInfo(self):
        add_vaccination_person_info = tk.Toplevel(app)
        add_vaccination_person_info.title('添加接种人员信息')
        add_vaccination_person_info.geometry("600x400")
        tk.Label(add_vaccination_person_info, text='姓名：', font=("Arial", 9)).place(x=80, y=60)
        tk.Label(add_vaccination_person_info, text='性别：', font=('Arial', 9)).place(x=80, y=90)
        tk.Label(add_vaccination_person_info, text='年龄：', font=('Arial', 9)).place(x=80, y=120)
        tk.Label(add_vaccination_person_info, text='身份证号：', font=('Arial', 9)).place(x=80, y=150)
        tk.Label(add_vaccination_person_info, text='家庭住址：', font=('Arial', 9)).place(x=80, y=180)
        tk.Label(add_vaccination_person_info, text='是否过敏：', font=('Arial', 9)).place(x=80, y=210)
        tk.Label(add_vaccination_person_info, text='接种时间：', font=('Arial', 9)).place(x=80, y=240)
        entry1 = tk.Entry(add_vaccination_person_info, font=("Arial, 9"), width=46)
        entry2 = tk.Entry(add_vaccination_person_info, font=("Arial, 9"), width=46)
        entry3 = tk.Entry(add_vaccination_person_info, font=("Arial, 9"), width=46)
        entry4 = tk.Entry(add_vaccination_person_info, font=("Arial, 9"), width=46)
        entry5 = tk.Entry(add_vaccination_person_info, font=("Arial, 9"), width=46)
        entry6 = tk.Entry(add_vaccination_person_info, font=("Arial, 9"), width=46)
        entry7 = tk.Entry(add_vaccination_person_info, font=("Arial, 9"), width=46)
        entry1.pack(),entry2.pack(),entry3.pack(),entry4.pack(),entry5.pack()
        entry6.pack(),entry7.pack()
        entry1.place(x=180, y=60, width=350),entry2.place(x=180, y=90, width=350)
        entry3.place(x=180, y=120, width=350),entry4.place(x=180, y=150, width=350),
        entry5.place(x=180, y=180, width=350),entry6.place(x=180, y=210, width=350),
        entry7.place(x=180, y=240, width=350)

        def add():
            text1 = entry1.get()
            text2 = entry2.get()
            text3 = entry3.get()
            text4 = entry4.get()
            text5 = entry5.get()
            text6 = entry6.get()
            text7 = entry7.get()
            content = "INSERT INTO vaccination_person_info (" \
                      "name, sexy, age, ID_num, address, allergy, date" \
                      ")" \
                      " VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (
                          text1, text2, text3, text4, text5, text6, text7)
            connect_DB(database="vaccine-test", content=content)
            tkinter.messagebox.showinfo(title="信息", message="数据添加成功！")

        def clear():
            entry1.delete(0, "end")
            entry2.delete(0, "end")
            entry3.delete(0, "end")
            entry4.delete(0, "end")
            entry5.delete(0, "end")
            entry6.delete(0, "end")
            entry7.delete(0, "end")
            tkinter.messagebox.showinfo(title="信息", message="数据已清空，请继续添加！")

        tk.Button(add_vaccination_person_info, text="添加", bg='white', font=("Arial,9"), width=9, height=0,command=add).place(x=400, y=360)
        tk.Button(add_vaccination_person_info, text="清空", bg='white', font=("Arial,9"), width=9, height=0,command=clear).place(x=160, y=360)

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
            data = connect_DB(database="vaccine-test", content=content)
            text1.delete(1.0, "end")
            text1.insert(chars="{}".format(data), index="insert")

        tk.Button(query, text='查询', bg='white', font=("Arial,12"), width=9, height=0, command=base_query).place(x=450,y=75)

    def vaccinationPersonInfoQuery(self):
        query = tk.Toplevel(app)
        query.title('接种人员信息查询')
        query.geometry("600x400")
        entry = tk.Entry(query, width=30)
        entry.pack()
        entry.place(x=200, y=80)
        tk.Label(query, text="请输入接种人员身份证号：", font=("Arial", 9)).place(x=50, y=80)
        tk.Label(query, text='查询结果：', font=('Arial', 9)).place(x=50, y=120)
        text1 = tk.Text(query, width=50, height=20)
        text1.pack()
        text1.place(x=150, y=120)
        def base_query():
            ID_num = entry.get()
            content = "SELECT * FROM vaccination_person_info WHERE ID_num = %s;" % ID_num
            data = connect_DB(database="vaccine-test", content=content)
            text1.delete(1.0, "end")
            text1.insert(chars="{}".format(data), index="insert")

        tk.Button(query, text='查询', bg='white', font=("Arial,12"), width=9, height=0, command=base_query).place(x=450, y=75)

    def vaccineInfoQuery(self):
        query = tk.Toplevel(app)
        query.title('疫苗信息查询')
        query.geometry("600x400")
        entry = tk.Entry(query, width=30)
        entry.pack()
        entry.place(x=200, y=80)
        tk.Label(query, text="请输入疫苗批号：", font=("Arial", 9)).place(x=50, y=80)
        tk.Label(query, text='查询结果：', font=('Arial', 9)).place(x=50, y=120)
        text1 = tk.Text(query, width=50, height=20)
        text1.pack()
        text1.place(x=150, y=120)
        def base_query():
            vaccine_num = entry.get()
            content = "SELECT * FROM vaccine_info WHERE vaccine_num = %s;" % vaccine_num
            data = connect_DB(database="vaccine-test", content=content)
            text1.delete(1.0, "end")
            text1.insert(chars="{}".format(data), index="insert")

        tk.Button(query, text='查询', bg='white', font=("Arial,12"), width=9, height=0, command=base_query).place(x=450, y=75)

    def modifyVaccineInfo(self):
        modify_info = tk.Toplevel(app)
        modify_info.title('疫苗信息修改')
        modify_info.geometry("600x400")
        entry = tk.Entry(modify_info, width=30)
        entry.pack()
        entry.place(x=200, y=60)
        tk.Label(modify_info, text="请输入疫苗分配单号：", font=("Arial", 9)).place(x=50, y=60)
        tk.Label(modify_info, text='疫苗批号：', font=("Arial", 9)).place(x=80, y=100)
        tk.Label(modify_info, text='疫苗名称：', font=('Arial', 9)).place(x=80, y=130)
        tk.Label(modify_info, text='企业名称：', font=('Arial', 9)).place(x=80, y=160)
        tk.Label(modify_info, text='企业编号：', font=('Arial', 9)).place(x=80, y=190)
        tk.Label(modify_info, text='    规格：', font=('Arial', 9)).place(x=80, y=220)
        tk.Label(modify_info, text='    进价：', font=('Arial', 9)).place(x=80, y=250)
        tk.Label(modify_info, text='  预售价：', font=('Arial', 9)).place(x=80, y=280)
        tk.Label(modify_info, text='企业上限：', font=('Arial', 9)).place(x=80, y=310)
        tk.Label(modify_info, text='企业下限：', font=('Arial', 9)).place(x=80, y=340)
        text1 = tk.Text(modify_info, width=50, height=1)
        text2 = tk.Text(modify_info, width=50, height=1)
        text3 = tk.Text(modify_info, width=50, height=1)
        text4 = tk.Text(modify_info, width=50, height=1)
        text5 = tk.Text(modify_info, width=50, height=1)
        text6 = tk.Text(modify_info, width=50, height=1)
        text7 = tk.Text(modify_info, width=50, height=1)
        text8 = tk.Text(modify_info, width=50, height=1)
        text9 = tk.Text(modify_info, width=50, height=1)
        text1.pack(),text2.pack(),text3.pack(),text4.pack(),text5.pack(),
        text6.pack(),text7.pack(),text8.pack(),text9.pack()
        text1.place(x=150, y=100),text2.place(x=150, y=130),text3.place(x=150, y=160),
        text4.place(x=150, y=190),text5.place(x=150, y=220),text6.place(x=150, y=250),
        text7.place(x=150, y=280),text8.place(x=150, y=310),text9.place(x=150, y=340)

        def base_query():
            vaccine_modify_num = entry.get()
            content = "SELECT * FROM vaccine_info WHERE vaccine_num = %s;" % vaccine_modify_num

            data = connect_DB(database="vaccine-test", content=content)
            text1.delete(1.0, "end"),text2.delete(1.0, "end"),text3.delete(1.0, "end"),text4.delete(1.0, "end"),
            text5.delete(1.0, "end"),text6.delete(1.0, "end"),text7.delete(1.0, "end"),text8.delete(1.0, "end"),
            text9.delete(1.0, "end")
            text1.insert(chars="{}".format(data[0]), index="insert"),text2.insert(chars="{}".format(data[1]), index="insert"),
            text3.insert(chars="{}".format(data[2]), index="insert"),text4.insert(chars="{}".format(data[3]), index="insert"),
            text5.insert(chars="{}".format(data[4]), index="insert"),text6.insert(chars="{}".format(data[5]), index="insert"),
            text7.insert(chars="{}".format(data[6]), index="insert"),text8.insert(chars="{}".format(data[7]), index="insert"),
            text9.insert(chars="{}".format(data[8]), index="insert")
        def update_info():
            vaccine_del_num = entry.get()
            str_ls = [text1.get("1.0", "end")[0:-1], text2.get("1.0", "end")[0:-1], text3.get("1.0", "end")[0:-1],
                      text4.get("1.0", "end")[0:-1], text5.get("1.0", "end")[0:-1], text6.get("1.0", "end")[0:-1],
                      text7.get("1.0", "end")[0:-1], text8.get("1.0", "end")[0:-1], text9.get("1.0", "end")[0:-1]]
            str_ls = [str(i) for i in str_ls]
            content = "UPDATE vaccine_info  SET vaccine_num='%s', vaccine_name='%s', company_name='%s', vaccine_num='%s'" \
                      ", size='%s', buy_price='%s', pre_sale_price='%s', limit_up='%s', limit_down='%s' WHERE " \
                      "vaccine_num = '%s';" % (
                          str_ls[0], str_ls[1], str_ls[2], str_ls[3], str_ls[4], str_ls[5], str_ls[6], str_ls[7], str_ls[8],
                          vaccine_del_num)
            connect_DB(database="vaccine-test", content=content)
            tkinter.messagebox.showinfo(title="信息", message="疫苗分配单号：{}数据修改成功！".format(vaccine_del_num))
            return None

        tk.Button(modify_info, text='查询', bg='white', font=("Arial,12"), width=9, height=0, command=base_query).place(x=450,y=55)
        tk.Button(modify_info, text='修改', bg='white', font=("Arial,12"), width=9, height=0, command=update_info).place(x=260,y=370)

    def delVaccineInfo(self):
        del_info = tk.Toplevel(app)
        del_info.title('疫苗信息删除')
        del_info.geometry("600x500")
        entry = tk.Entry(del_info, width=30)
        entry.pack()
        entry.place(x=200, y=80)
        tk.Label(del_info, text="请输入疫苗批号：", font=("Arial", 9)).place(x=50, y=80)
        tk.Label(del_info, text='查询结果：', font=('Arial', 9)).place(x=50, y=120)
        text1 = tk.Text(del_info, width=50, height=20)
        text1.pack()
        text1.place(x=150, y=120)

        def base_query():
            vaccine_del_num = entry.get()
            print(vaccine_del_num)
            content = "SELECT * FROM vaccine_info WHERE vaccine_num = %s;" % vaccine_del_num
            data = connect_DB(database="vaccine-test", content=content)
            text1.delete(1.0, "end")
            text1.insert(chars="{}".format(data), index="insert")

        def del_infor():
            vaccine_del_num = entry.get()
            print(vaccine_del_num)
            content = "DELETE FROM vaccine_info  WHERE vaccine_num = %s;" % vaccine_del_num
            data = connect_DB(database="vaccine-test", content=content)
            tkinter.messagebox.showinfo(title="信息", message="疫苗批号：{}数据已删除！".format(vaccine_del_num))
            return None

        tk.Button(del_info, text='查询', bg='white', font=("Arial,12"), width=9, height=0, command=base_query).place(x=450,y=75)
        tk.Button(del_info, text='删除', bg='white', font=("Arial,12"), width=9, height=0, command=del_infor).place(x=280,y=400)
