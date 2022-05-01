import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
addr=('localhost', 9000)
sock.connect(addr)

msg=sock.recv(1024) #1 서버한테서의 메시지를 기다림
print(msg.decode()) #server에서 받은 msg인 Hello 127.0.0.1 출력

# msgName=sock.send(b'Nahee Kim')
msgName=sock.send('Nahee Kim'.encode('utf-8'))
#이름 보내기 성공

num=sock.recv(1024)
print(int.from_bytes(num,'big'))
#학번 받기 성공

sock.close()