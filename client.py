import socket

def client():
    hostname=socket.gethostname()
    host=socket.gethostbyname(hostname)
    port=6000

    client_socket=socket.socket()
    client_socket.connect((host,port))

    while True:
        msg=input(">>>")
        client_socket.send(msg.encode())
        data=client_socket.recv(1024).decode()
        print(data)
        msg=input(">>>")

if __name__=='__main__':
    client()