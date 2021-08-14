import socket
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import *

Background = '#08748C'
Highlight_font_color = '#EDE907'
Highlight_background_color = '#022340'
Font_color = '#0FF2F2'
Background_color = '#023E73'
Entry_color = '#011526'
Entry_background = '#0FF2F2'


def Show():
	newwin = Tk()
	newwin.geometry("465x550")
	newwin.configure(bg = Background)
	newwin.title("Look Up")
	option = [
	            "AUSTRALIAN DOLLAR",
	            "CANADIAN DOLLAR",
	            "SWISS FRANC",
	            "YUAN RENMINBI",
	            "DANISH KRONE",
	            "EURO",
	            "POUND STERLING",
	            "HONGKONG DOLLAR",
	            "INDIAN RUPEE",
	            "YEN",
	            "KOREAN WON",
	            "KUWAITI DINAR",
	            "MALAYSIAN RINGGIT",
	            "NORWEGIAN KRONER",
	            "RUSSIAN RUBLE",
	            "SAUDI RIAL",
	            "SWEDISH KRONA",
	            "SINGAPORE DOLLAR",
	            "THAILAND BAHT",
	            "US DOLLAR",
	        ]

	title = Label(
		newwin,
		text = "__TỶ GIÁ TIỀN TỆ__",
		fg = Highlight_font_color,
		bg = Background,
		)
	title.config(font=('Fira Sans ExtraBold',20))
	title.grid(row=0, column=0, padx = 10, pady = 10, columnspan = 2)
	kcach = Label(
		newwin,
		text = '',
		bg = Background,
    	fg = Highlight_font_color,
		).grid(row=1, column=0, columnspan = 2)
	SelectDay = Label(
	   newwin, 
	   text="Ngày tra cứu:",
	   bg = Background,
	   fg = Highlight_font_color,
	   ).grid(row=2, column=0, sticky=W, padx = 15, pady = 10)
	cal = Calendar(newwin, selectmode = "day", year = 2021, month = 8, day = 7)
	cal.grid(row=3, column = 0, padx = 15, pady = 10, rowspan = 2)
	SelectUnit = Label(
	   newwin, 
	   text="Loại tiền tệ:",
	   bg = Background,
	   fg = Highlight_font_color,
	   ).grid(row=2, column=1, sticky=W, padx = 15, pady = 10)
	Unit = ttk.Combobox(
	    newwin,
	    width = 22,
	    values = option
	    )
	Unit.insert(0, "Chọn loại tiền tệ")
	Unit.grid(row=3,column=1, padx = 15, pady = 10)
	display_exist = False
	display = Frame(newwin)
	display.grid(row=1, column=2)
	def Confirm():
		nonlocal display_exist, display
		Day = cal.get_date().split('/',3)
		MonthYear = cal.get_displayed_month()
		Money = Unit.get()
		Date = Day[1] + '/' + str(MonthYear[0]) + "/" + str(MonthYear[1])

		if Money == "Chọn loại tiền tệ":
			messagebox.showinfo("Thông báo", "Sai loại tiền tệ, vui lòng nhập lại")
			return
		try:
			client.sendall(bytes("TraCuu","utf8"))
			check = client.recv(1024).decode("utf8")
			client.sendall(bytes(Date,"utf8"))
			check =  client.recv(1024).decode("utf8")
			client.sendall(bytes(Money,"utf8"))
			check = client.recv(1024).decode("utf8")
			MuaTienMat = client.recv(1024).decode("utf8")
			client.sendall(bytes("Da Nhan Duoc MuaTienMat","utf8"))
			MuaChuyenKhoan = client.recv(1024).decode("utf8")
			client.sendall(bytes("Da Nhan Duoc MuaChuyenKhoan","utf8"))
			Ban = client.recv(1024).decode("utf8")
			client.sendall(bytes("Da Nhan Duoc Ban","utf8"))
		except:
			messagebox.showinfo("Thông báo", "Mất kết nối đến server")
			return

		if MuaTienMat == '0' and MuaChuyenKhoan == '0' and Ban == '0':
			messagebox.showinfo("Thông báo", "Không tìm thấy loại tiền vào ngày này, vui lòng nhập lại")
			return
		if display_exist == True:
			display.grid_forget()
		display_exist = True
		display = Frame(newwin, bg=Background)
		display.grid(row=5, column=0, columnspan = 2, padx =15, pady = 15)

		daugach = Label(
			display,
			text ="==================================================",
			bg = Background,
    		fg = Highlight_font_color,
			).grid(row=0,column=0, sticky='w', padx = 10, pady = 5, columnspan = 2)
		LoaiTien = Label(
			display,
			text="Loại Tiền:",
			bg = Background,
    		fg = Highlight_background_color,
			).grid(row=1,column=0, sticky='w', padx = 10, pady = 5)
		Tien = Label(
			display,
			text= Money,
			bg = Background,
    		fg = Highlight_font_color,
			).grid(row=1,column=1)

		NgayTraCuu = Label(
			display,
			text="Ngày Tra Cứu:",
			bg = Background,
    		fg = Highlight_background_color,
			).grid(row=2,column=0, sticky='w', padx = 10, pady = 5)
		Ngay = Label(
			display,
			text= Date,
			bg = Background,
    		fg = Highlight_font_color,
			).grid(row=2,column=1)

		GiaMuaTienMat = Label(
			display,
			text="Giá mua bằng tiền mặt:",
			bg = Background,
    		fg = Highlight_background_color,
			).grid(row=3,column=0, sticky='w', padx = 10, pady = 5)
		Mua1 = Label(
			display,
			text= MuaTienMat,
			bg = Background,
    		fg = Highlight_font_color,
			).grid(row=3,column=1)

		GiaMuaChuyenKhoan = Label(
			display,
			text="Giá mua bằng chuyển khoảng:",
			bg = Background,
    		fg = Highlight_background_color,
			).grid(row=4,column=0, sticky='w', padx = 10, pady = 5)
		Mua2 = Label(
			display,
			text= MuaChuyenKhoan,
			bg = Background,
    		fg = Highlight_font_color,
			).grid(row=4,column=1)

		GiaBan = Label(
			display,
			text="Giá bán:",
			bg = Background,
    		fg = Highlight_background_color,
			).grid(row=5,column=0, sticky='w', padx = 10, pady = 5)
		Ban = Label(
			display,
			text= MuaChuyenKhoan,
			bg = Background,
    		fg = Highlight_font_color,
			).grid(row=5,column=1)
	ConfirmButton = Button(
	   newwin,
	   text="Tra Cứu",
	   height = 7,
	   width = 15,
	   borderwidth=5,
	   fg = Highlight_font_color,
       bg = Highlight_background_color,
	   command = Confirm
	   ).grid(row=4, column=1)
def Connected():
	newwin = Tk()
	newwin.geometry("405x240")
	newwin.configure(bg = Background)
	newwin.title("Log In")

	TextUsername = Label(
	   newwin,
	   text = "Username",
	   bg = Background,
	   fg = Highlight_font_color,
	   ).grid(row=0,column=0,sticky=W, padx =10, pady = 10)
	Username_Entry = Entry(
	   newwin,
	   width = 60,
	   bg = Entry_background,
	   fg = Entry_color,
	   )
	Username_Entry.insert(END, "Nhập tên đăng nhập")
	Username_Entry.grid(row=1,column=0, padx = 20)

	TextPassword = Label(
	   newwin,
	   text = "Password",
	   bg = Background,
	   fg = Highlight_font_color,
	   ).grid(row=2,column=0,sticky=W, padx =10, pady = 10)
	Passwords_Entry = Entry(
	   newwin,
	   show = '*',
	   width = 60,
	   bg = Entry_background,
	   fg = Entry_color,
	   )
	Passwords_Entry.insert(END, "Password")
	Passwords_Entry.grid(row=3,column=0)


	def DN():
		try:
			client.sendall(bytes("DangNhap","utf8"))
			check = client.recv(1024).decode("utf8")

			Username = Username_Entry.get()
			Passwords = Passwords_Entry.get()

			client.sendall(bytes(Username,"utf8"))
			check = client.recv(1024).decode("utf8")

			client.sendall(bytes(Passwords,"utf8"))
			check = client.recv(1024).decode("utf8")


			Mess = client.recv(1024).decode("utf8")
			client.sendall(bytes("OK","utf8"))

			if Mess == "WrongPass":
				messagebox.showinfo("Thông báo", "Sai mật khẩu")
				return
			if Mess == "WrongUser":
				messagebox.showinfo("Thông báo", "Sai Username")
				return
			if Mess == "RightUser":
				messagebox.showinfo("Thông báo", "Đăng nhập thành công!!!")
				newwin.destroy()
				Show()
				return
		except:
			messagebox.showinfo("Thông báo", "Mất kết nối đến server")
			return

	LogIn = Button(
	   newwin,
	   width = 10,
	   text = "Đăng nhập",
	   borderwidth=5,
	   fg = Highlight_font_color,
	   bg = Highlight_background_color,
	   command = DN
	   )
	LogIn.grid(row=4,column=0,pady = 10)

	def DK():
		newwin2 = Tk()
		newwin2.configure(bg = Background)
		newwin2.title("Sign Up")

		TextUsername = Label(
		   newwin2,
		   text = "Username",
		   bg = Background,
	       fg = Highlight_font_color,
		   ).grid(row=0,column=0,sticky=W, padx = 10, pady = 10)
		Username_Entry = Entry(
		   newwin2,
		   width = 60,
		   bg = Entry_background,
		   fg = Entry_color,
		   )
		Username_Entry.insert(END, "Tên đăng nhập")
		Username_Entry.grid(row=1,column=0, padx = 20)

		TextPassword = Label(
		   newwin2,
		   bg = Background,
	       fg = Highlight_font_color,
		   text = "Password"
		   ).grid(row=2,column=0,sticky=W, padx =10, pady = 10)
		Passwords_Entry = Entry(
		   newwin2,
		   show = '*',
		   bg = Entry_background,
		   fg = Entry_color,
		   width = 60,
		   )
		Passwords_Entry.insert(END, "Password")
		Passwords_Entry.grid(row=3,column=0)

		TextConfirmPassword = Label(
		   newwin2,
		   text = "Confirm Password",
		   bg = Background,
	       fg = Highlight_font_color,
		   ).grid(row=4,column=0,sticky=W, padx =10, pady =10)
		ConfirmPasswords_Entry = Entry(
		   newwin2,
		   show = '*',
		   width = 60,
		   bg = Entry_background,
		   fg = Entry_color,
		   )
		ConfirmPasswords_Entry.insert(END, "Password")
		ConfirmPasswords_Entry.grid(row=5,column=0)
		def SendDK():
			try:
				ConfirmPasswords = ConfirmPasswords_Entry.get()
				Passwords = Passwords_Entry.get()
				Username = Username_Entry.get()
				if Username.find(" ") != -1: 
					messagebox.showinfo("Thông báo", "Không được để khoảng trắng trong USERNAME")
					return
				if ConfirmPasswords != Passwords:
					messagebox.showinfo("Thông báo", "Mật khẩu không trùng khớp")
					return

				client.sendall(bytes("DangKi","utf8"))
				check = client.recv(1024).decode("utf8")

				client.sendall(bytes(Username,"utf8"))
				check = client.recv(1024).decode("utf8")

				ExistUsername = client.recv(1024).decode("utf8")
				client.sendall(bytes("OK","utf8"))

				if ExistUsername == "ExistUsername":
					messagebox.showinfo("Thông báo", "Username đã tồn tại, vui lòng chọn username khác")
					return
				if ExistUsername == "ValidUsername":
					client.sendall(bytes(Passwords,"utf8"))
					check = client.recv(1024).decode("utf8")
					messagebox.showinfo("Thông báo", "Chúc mừng bạn đã đăng kí thành công!!!")
					newwin2.destroy()
					return
			except:
				messagebox.showinfo("Thông báo", "Mất kết nối đến server")
				exit()

		SignUp = Button(
		   newwin2,
		   width = 10,
		   text = "Đăng kí",
		   borderwidth=5,
	       fg = Highlight_font_color,
	       bg = Highlight_background_color,
		   command = SendDK
		   )
		SignUp.grid(row=6,column=0, pady = 10)

	TextRegis = Label(
	   newwin,
	   text = "Nếu chưa có tài khoản, vui lòng ấn đăng ký",
	   bg = Background,
	   fg = Entry_color,
	   ).grid(row=5,column=0, pady =5)
	Regis = Button(
	   newwin,
	   width = 10,
	   text = "Đăng kí",
	   borderwidth=5,
	   fg = Highlight_font_color,
	   bg = Highlight_background_color,
	   command = DK
	   )
	Regis.grid(row=6,column=0,pady = 3)
	newwin.mainloop()
def Connect():
	global client
	Host = IP.get()
	Port = 1233
	server_address = (Host,Port)
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
	    client.connect(server_address)
	    messagebox.showinfo("Kết nối", "Bạn đã kết nối thành công!!!")
	    mainwin.destroy()
	    Connected()
	except:
	    messagebox.showinfo("Kết nối", "Sai IP")

mainwin = Tk()
mainwin.configure(bg = Background)
mainwin.title("CLIENT")

IP = Entry(
	mainwin,
	width = 55,
	bg = Entry_background,
    fg = Entry_color,
	)
IP.insert(END, "Nhập IP server")
IP.grid(row = 1, column = 0, padx = 15)

Text = Label(
	mainwin, 
	text="TRA CỨU TỈ GIÁ TIỀN TỆ THẾ GIỚI",
	bg = Background,
    fg = Highlight_font_color,
	)
Text.config(font=('Fira Sans ExtraBold',20))
Text.grid(row=0, columnspan = 1, pady = 0)

Connect_Button = Button(
	mainwin,
	text = "Kết nối",
	padx = 15, 
    pady = 15, 
    borderwidth=5,
    fg = Highlight_font_color,
    bg = Highlight_background_color,
    command = Connect
	).grid(row = 1, column = 1, padx =15, pady = 2)

mainwin.mainloop()