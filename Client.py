import socket
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import *

def Show():
	newwin = Tk()
	newwin.title("Tra Cứu")
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
	SelectDay = Label(
	   newwin, 
	   text="Ngày tra cứu",
	   ).grid(row=0, column=0, pady = 5)
	cal = Calendar(newwin, selectmode = "day", year = 2021, month = 8, day = 5)
	cal.grid(row=1, column = 0)
	SelectUnit = Label(
	   newwin, 
	   text="Loại tiền tệ",
	   ).grid(row=2, column=0, pady = 5)
	Unit = ttk.Combobox(
	    newwin,
	    width = 22,
	    values = option
	    )
	Unit.insert(0, "Chọn loại tiền tệ")
	Unit.grid(row=3,column=0)
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
			messagebox.showinfo("Thông báo", "Sai ngày xem, vui lòng nhập lại")
			return
		if display_exist == True:
			display.grid_forget()
		display_exist = True
		display = Frame(newwin)
		display.grid(row=1, column=2)
		LoaiTien = Label(
			display,
			text="Loại Tiền"
			).grid(row=0,column=0,sticky="W")
		Tien = Label(
			display,
			text= Money
			).grid(row=0,column=1)

		NgayTraCuu = Label(
			display,
			text="Ngày Tra Cứu"
			).grid(row=1,column=0,sticky="W")
		Ngay = Label(
			display,
			text= Date
			).grid(row=1,column=1)

		GiaMuaTienMat = Label(
			display,
			text="Giá mua bằng tiền mặt"
			).grid(row=2,column=0,sticky="W")
		Mua1 = Label(
			display,
			text= MuaTienMat
			).grid(row=2,column=1)

		GiaMuaChuyenKhoan = Label(
			display,
			text="Giá mua bằng chuyển khoản"
			).grid(row=3,column=0,sticky="W")
		Mua2 = Label(
			display,
			text= MuaChuyenKhoan
			).grid(row=3,column=1)

		GiaBan = Label(
			display,
			text="Giá bán"
			).grid(row=4,column=0,sticky="W")
		Ban = Label(
			display,
			text= MuaChuyenKhoan
			).grid(row=4,column=1)
	ConfirmButton = Button(
	   newwin,
	   text="Tra Cứu",
	   height = 10,
	   width = 10,
	   command = Confirm
	   ).grid(row=1, column=1)
def Connected():
	newwin = Tk()
	newwin.title("Đăng Nhập")

	TextUsername = Label(
	   newwin,
	   text = "Username"
	   ).grid(row=0,column=0,sticky=W)
	Username_Entry = Entry(
	   newwin,
	   width = 60,
	   )
	Username_Entry.insert(END, "Nhập tên đăng nhập")
	Username_Entry.grid(row=1,column=0, padx = 20)

	TextPassword = Label(
	   newwin,
	   text = "Password"
	   ).grid(row=2,column=0,sticky=W)
	Passwords_Entry = Entry(
	   newwin,
	   show = '*',
	   width = 60,
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
	   command = DN
	   )
	LogIn.grid(row=4,column=0,pady = 10)

	def DK():
		newwin2 = Tk()
		newwin2.title("Đăng Kí")

		TextUsername = Label(
		   newwin2,
		   text = "Username"
		   ).grid(row=0,column=0,sticky=W)
		Username_Entry = Entry(
		   newwin2,
		   width = 60,
		   )
		Username_Entry.insert(END, "Tên đăng nhập")
		Username_Entry.grid(row=1,column=0, padx = 20)

		TextPassword = Label(
		   newwin2,
		   text = "Password"
		   ).grid(row=2,column=0,sticky=W)
		Passwords_Entry = Entry(
		   newwin2,
		   show = '*',
		   width = 60,
		   )
		Passwords_Entry.insert(END, "Password")
		Passwords_Entry.grid(row=3,column=0)

		TextConfirmPassword = Label(
		   newwin2,
		   text = "Confirm Password"
		   ).grid(row=4,column=0,sticky=W)
		ConfirmPasswords_Entry = Entry(
		   newwin2,
		   show = '*',
		   width = 60,
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
		   command = SendDK
		   )
		SignUp.grid(row=6,column=0,pady = 10)

	TextRegis = Label(
	   newwin,
	   text = "Nếu chưa có tài khoản, vui lòng ấn đăng ký"
	   ).grid(row=5,column=0)
	Regis = Button(
	   newwin,
	   width = 10,
	   text = "Đăng kí",
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
mainwin.title("CLIENT")

IP = Entry(
	mainwin,
	width = 60,
	)
IP.insert(END, "Nhập IP")
IP.grid(row = 1, column = 0, padx = 15)

Text = Label(text="Xem tỉ Giá Tiền Tệ")
Text.config(font=('',15))
Text.grid(row=0, columnspan = 2)

Connect_Button = Button(
	mainwin,
	text = "Kết nối",
	padx = 15, 
    pady = 15, 
    borderwidth=5,
    command = Connect
	).grid(row = 1, column = 1)

mainwin.mainloop()