import socket
from threading import Thread
from tkinter import messagebox
import threading
from tkinter import *
import requests
from bs4 import BeautifulSoup

HOST = ''  
PORT = 1233

def Server_Running():
    global HOST, PORT, server
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    HOST = str(ip_address)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(10)
    print(HOST+':'+str(PORT))

    def SendMess(client, adr):
        global StopServer
        #function cho server:

        def DangKi():
            Username = client.recv(1024).decode("utf8")
            client.sendall(bytes("Da nhan username", "utf8"))

            file = open("Database.txt", 'r')
            while True:
                line = file.readline()
                line = line.strip()
                if not line: break
                UP = line.split(" ", 2)
                if UP[0] == Username:
                    client.sendall(bytes("ExistUsername", "utf8"))
                    check = client.recv(1024).decode("utf8")
                    return
            client.sendall(bytes("ValidUsername", "utf8"))
            check = client.recv(1024).decode("utf8")
            file.close()

            Password = client.recv(1024).decode("utf8")
            client.sendall(bytes("Da nhan password","utf8"))

            file = open("Database.txt", 'a')
            file.write('\n')
            file.write(Username + ' ' + Password)
        def DangNhap():
            Username = client.recv(1024).decode("utf8")
            client.sendall(bytes("Da Nhan username", "utf8"))

            Password = client.recv(1024).decode("utf8")
            client.sendall(bytes("Da Nhan Password", "utf8"))

            file = open("Database.txt", 'r')
            while True:
                line = file.readline()
                line = line.strip()
                if not line: break
                UP = line.split(" ", 2)
                if UP[0] == Username and UP[1] != Password:
                    client.sendall(bytes("WrongPass", "utf8"))
                    check = client.recv(1024).decode("utf8")
                    return
                if UP[0] == Username and UP[1] == Password:
                    client.sendall(bytes("RightUser", "utf8"))
                    check = client.recv(1024).decode("utf8")
                    return
            client.sendall(bytes("WrongUser", "utf8"))
            check = client.recv(1024).decode("utf8")
            file.close()
        def TraCuu():
            def search(date,money):
               url="https://portal.vietcombank.com.vn/UserControls/TVPortal.TyGia/pListTyGia.aspx?txttungay="+ date +"&BacrhID=1&isEn=False&fbclid=IwAR3m3AhOyRSUd0hJfE8nLaExcTp6gUgjBqEQaO6liygeyfi0QsIKR5b454k"
               response = requests.get(url)
               soup = BeautifulSoup(response.content, "html.parser")
               file = open('tygia.txt','w',encoding='utf-8')
               file.write(str(soup))
               file.close()
               file = open('tygia.txt','r',encoding='utf-8')
               data = file.read()
               start = data.find(money)
               if start == -1: 
                  return '0', '0', '0'
               stop = data.find("</tr>",start,len(data))
               Total = data[start:stop]
               start = Total.find("<td>")
               for i in range(3):
                  stop = Total.find("</td>",stop)
               ThreeMoney = Total[start:stop]
               pos = ThreeMoney.find('\n')
               TienMat = ThreeMoney[4:pos-5]
               pos1 = ThreeMoney.find('\n',pos+1)
               ChuyenKhoan = ThreeMoney[pos+5: pos1-5]
               Ban = ThreeMoney[pos1+5:ThreeMoney.find('\n',pos1+1)-4]
               file.close()
               return TienMat, ChuyenKhoan, Ban

            Date = client.recv(1024).decode("utf8")
            client.sendall(bytes("Da Nhan Duoc Date","utf8"))

            Money = client.recv(1024).decode("utf8")
            client.sendall(bytes("Da Nhan Duoc Money","utf8"))

            MuaTienMat, MuaChuyenKhoan, Ban = search(Date, Money)

            client.sendall(bytes(MuaTienMat,"utf8"))
            check = client.recv(1024).decode("utf8")

            client.sendall(bytes(MuaChuyenKhoan,"utf8"))
            check = client.recv(1024).decode("utf8")

            client.sendall(bytes(Ban,"utf8"))
            check = client.recv(1024).decode("utf8")

        #Command cho server:
        while True:
            try:
                command = client.recv(1024).decode("utf8")
                print(1)
                client.sendall(bytes("Da Nhan","utf8"))
                print(command)
                if command == "DangKi": DangKi()
                elif command == "DangNhap": DangNhap()
                elif command == "TraCuu": TraCuu()
            except:
                print(addr, "Disconneted")
                return

    while True:
        try:
            client, addr = server.accept()
            print('Connected by', addr)
            t1 = threading.Thread(target = SendMess, args = (client,addr))
            t1.start()
        except:
            print("Disconneted")
            break

def StartServer():
    mainThread = threading.Thread(target = Server_Running)
    mainThread.daemon = True 
    mainThread.start()

def StopServer():
    check = messagebox.askyesno("Tắt Server", "Bạn có muốn ngưng Server?")
    if check == 1:
        server.close()
        exit()
    return
mainWin = Tk()
mainWin.title("SERVER")
mainWin.geometry("200x200")
Start = Button(
        mainWin,
        text = "Khởi động server",
        width = 20,
        height = 10,
        command = StartServer
    ).pack()
Stop = Button(
    mainWin,
    text = "Tắt server",
    width = 20,
    height = 10,
    command = StopServer
    ).pack()
mainWin.mainloop()
