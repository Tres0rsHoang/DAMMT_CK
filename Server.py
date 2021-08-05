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
        #Command cho server:
        while True:
            data = client.recv(1024).decode("utf8")
            client.sendall(bytes("Da Nhan","utf8"))
            print(data)

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