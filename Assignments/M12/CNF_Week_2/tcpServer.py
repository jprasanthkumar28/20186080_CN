import socket
import time

def main():
    host = '10.10.9.48'
    # lst = [rollnumber, question, pound, answer]
    port = 10020
    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    c, address = s.accept()
    print('connection from ' + str(address))
    while True:
        data = c.recv(1024)
        data = str(data.decode()).split()
        if data[1] == 'rollnumber':
            result = float(rollnumber.get(data[4]) * int(data[2]))
        elif data[1] == 'question':
            result = float(question.get(data[4]) * int(data[2]))
        elif data[1] == 'answer':
            result = float(answer.get(data[4]) * int(data[2]))
        c.send(str(result).encode())
    c.close()

if __name__ == '__main__':
    main()