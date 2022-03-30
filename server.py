import socket
import threading
from socket import*

serverSocket = socket(AF_INET,SOCK_STREAM)                                      
serverSocket.bind(('140.115.213.23',12000))                                     
serverSocket.listen(5)                                        
p1 = ""
p2 = ""
flag = False
readynumber = 0
socket_list = []
def handle(client,addr,a):
    global socket_list,p1,p2,flag,readynumber
    a = str(a)
    client.send(str.encode(a))
    while True:
        try:
            text = client.recv(1024).decode()
            spacesplit = text.split()
            if(text == "bye"):
                break
            if(spacesplit[0] == "ready"):
                if(a == "1"):
                    p1 = spacesplit[1]
                elif(a == "0"):
                    p2 = spacesplit[1]
                readynumber += 1
                if(readynumber == 2):
                    temp = p1+" "+p2+" "+"1"+" "+"1"+" "
                    socket_list[0].send(temp.encode())
                    socket_list[1].send(temp.encode())
                    flag  = True
            if(a=="1"):
                if(flag==True):
                    socket_list[1].send(text.encode())
            elif(a=="0"):
                if(flag==True):
                    socket_list[0].send(text.encode())
        except:
            break
    print(addr[0],addr[1],'>>say goodby')
    socket_list = []
    flag = False
    readynumber = 0
    client.close()






a = 0
while (True):
    client,addr=serverSocket.accept()
    socket_list.append(client)
    a = a+1                                                                    #4、接受客戶端連線
    if a % 2 == 1:
        thread1=threading.Thread(target=handle,args = (client,addr,a % 2))
        print(a % 2)
        thread1.start()
    elif a % 2 == 0:
        thread2=threading.Thread(target=handle,args = (client,addr,a % 2))
        print(a % 2)
        thread2.start()


