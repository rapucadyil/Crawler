import socket
from _thread import *
import sys

server = "192.168.1.115"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(4)
print("Waiting for connection, Server Started")

def threaded_client(conn):
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            if not data:
                print("disconnected...")
                break
            else:
                print("Recieved : ", reply)
                print("Sending : ", reply)
            conn.sendall(str.encode(reply))
        except:
            break 
while True:
    conn, addr = s.accept()
    print("Connection recieved to : ", addr)

    start_new_thread(threaded_client, (conn, ))