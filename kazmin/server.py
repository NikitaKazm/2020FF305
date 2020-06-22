import time
import socket
import threading
from  test_for_log import openning

IP = ''
PORT = 1005
backlog = 50
buffersize = 65535

s = socket.socket()
s.bind((IP, PORT))
s.listen(backlog)
print("���� " + str(PORT) + " ��������������...")


def new_connect(sock, addr):
    def send(pckData):
        sock.send(bytearray(pckData, 'utf-8'))

    last_message = chr(0)
    try:
        while True:
            data = sock.recv(buffersize).decode("utf-8")  # �������� ������
            if data == '': break

            pckType = ord(data[0])  # ������ ���� - ��� �������� ������

            if pckType == 1:  # 01 - ��������� ��� ��� ����
                a = data[1:]
                openning(a)
                print(addr[0] + " Log file ���������")
sock.close()
        print("���������� " + addr[0] + " �������")
while True:
    sock, addr = s.accept()
    print("����� ���������� �� " + addr[0])

    threading.Thread(target=new_connect, args=(sock, addr,)).start()  # ������� ����� �����