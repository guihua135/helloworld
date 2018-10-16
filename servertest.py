import socket
import re

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 1234))
server.listen(5)

while 1:
    i, msg = 0, []
    connectSocket, addr = server.accept()
    while 1:
        msg.append(connectSocket.recv(1024).decode("utf-8"))
        matchObj = re.match(r'.*bye\b', str(msg[i]))
        if matchObj is not None:
            print(str(msg[i]), "连接地址：%s" % str(addr))
            break
        else:
            print(str(msg[i]), "连接地址：%s" % str(addr))
        i += 1

    '''while i<10:
        connectSocket.send("欢迎访问我的测试socket服务器".encode("utf-8"))
        time.sleep(1)
        i+=1
    '''
    connectSocket.close()
