import socket
def se():
    TCP_IP = '192.168.1.209'
    TCP_PORT = 5005
    BUFFER_SIZE = 20  # Normally 1024, but we want fast response
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(2)
    conn, addr = s.accept()
    print ('Connection address:', addr)
    data=""
    data = conn.recv(BUFFER_SIZE)
    a=str(data.decode())
    l=a.split()
    print(l)
    #print("received data:", a)
    msg="yes".encode()
    conn.send(bytearray(msg))  # echo
    conn.close()
while 1:
    se()