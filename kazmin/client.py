import socket

IP = '127.0.0.1'
PORT = 1005
buffersize = 65535

s = socket.socket()
s.connect((IP, PORT))
print("���������� � �������� " + IP + ":" + str(PORT) + " �����������.\n")

while True:
    print("�������:")
    print("1 Log file ����������")
    if pckType == 1:
        data = input("������� ����: ")
        pckSend = chr(pckType) + data
        s.send(bytearray(pckSend, 'utf-8'))
        pckRecv = s.recv(buffersize).decode("utf-8")
s.close()
print("���������� �������.")