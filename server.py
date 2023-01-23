import socket

def server_connection():
    hostname=socket.gethostname()
    host=socket.gethostbyname(hostname)
    port=6000
    serer_socket=socket.socket()
    serer_socket.bind((host,port))
    serer_socket.listen(2)
    print("Listning connetction from ",host+"/ ",port)
    conn,addr=serer_socket.accept()
    print("Connetion from:",addr)

    while True:
        data=conn.recv(1024).decode()
        if data=="Bye":
            end_msg="Ok ! Thankyou !"
            conn.send(end_msg.encode())
            conn.close()

        else:
            data=input(">>>")
            conn.send(data.encode())



if __name__=='__main__':
    server_connection()
