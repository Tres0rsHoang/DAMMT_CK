import socket
from tkinter import *
from tkinter import messagebox

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

	LogIn = Button(
	   newwin,
	   width = 10,
	   text = "Đăng nhập"
	   )
	LogIn.grid(row=4,column=0,pady = 10)

	TextRegis = Label(
	   newwin,
	   text = "Nếu chưa có tài khoản, vui lòng ấn đăng ký"
	   ).grid(row=5,column=0)

	Regis = Button(
	   newwin,
	   width = 10,
	   text = "Đăng kí"
	   )
	Regis.grid(row=6,column=0,pady = 3)





def Connect():
	global client
	Host = IP.get()
	Port = 1233
	server_address = (Host,Port)
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
	    client.connect(server_address)
	    messagebox.showinfo("Kết nối", "Bạn đã kết nối thành công!!!")
	    Connected()
	    mainwin.destroy()
	except:
	    messagebox.showinfo("Kết nối", "Sai IP")

def SendMess():
	client.sendall(bytes("Hi","utf8"))
	rep = client.recv(1024).decode("utf8")
	print(rep)


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