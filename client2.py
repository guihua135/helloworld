import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 1234))
i=0
while i<10:
    client.send("this is client 2".encode("utf-8"))
    time.sleep(0.1)
    i+=1
client.send("bye".encode("utf-8"))
client.close()