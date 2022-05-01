from os import access
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',9000))
s.listen(2)

while True:
    client, addr=s.accept() #addr는 클라이언트에서 받아온거
    print('Connection from  ', addr)
    client.send(b'Hello '+addr[0].encode()) #1 클라이언트로 보내는 메시지
    #->Hello 127.0.0.1 보냄

    name=client.recv(1024) #이때까지 s.recv로 해서 안 됐던 거임!!!!!
    print(name.decode())
    #이름 받기 성공
    
    N=20181529
    num=N.to_bytes(4, 'big')
    client.send(num)
    #학번 보내기 성공

    client.close()