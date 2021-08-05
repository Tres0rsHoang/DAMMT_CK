import socket
from threading import Thread
import threading
from tkinter import *

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


        #Command cho server:
        while True:

            command = client.recv(1024).decode("utf8")
            client.sendall(bytes("Da Nhan","utf8"))
            print(command)
            
            if command == "DangKi": DangKi()
            elif command == "DangNhap": DangNhap()

    while True:
        client, addr = server.accept()
        print('Connected by', addr)
        t1 = threading.Thread(target = SendMess, args = (client,addr))
        t1.start()

mainWin = Tk()
mainWin.title("SERVER")
mainWin.geometry("200x200")
Start = Button(
        mainWin,
        text = "Khởi động server",
        width = 20,
        height = 10,
        command = Server_Running
    ).pack()

mainWin.mainloop()
server.close()