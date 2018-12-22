import socket

def main():
	host = '192.168.137.106'
	port = 1011

	s = socket.socket()
	s.connect((host,port))

	message = input("enter text: ")
	while message != 'q':
		s.send(message.encode())
		data = s.recv(1024)
		print("Received from server: " + str(data.decode()))
		print("Received")
		message = input("enter text: ")

	s.close()

if __name__ == '__main__':
	main()