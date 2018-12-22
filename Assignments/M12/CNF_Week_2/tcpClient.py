import csv
import socket


def main():
    host = '10.10.9.48'
    port = 10020
    s = socket.socket()
    s.connect((host, port))
    with open('data.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            print(row)
        csvFile.close()
        reader = input('--> ')
        while reader != 'q':
            s.send(reader.encode())
            data = s.recv(1024)
            print('received from server ' + str(data.decode()))
            reader = input("--> ")
        s.close()


if __name__ == '__main__':
    main()

