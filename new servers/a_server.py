import socket
def getuser(username):
    TCP_IP = '192.168.43.177'
    TCP_PORT = 5006
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(bytearray(username.encode()))
    s.close()