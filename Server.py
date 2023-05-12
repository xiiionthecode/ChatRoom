import socket

host = "localhost"
port = 8080

# socket.SOCK_DGRAM   UDP
# socket.SOCK_STREAM   TCP

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))

sock.listen(1)
conn,address = sock.accept()


message = "Hey there is somthing important for you"
conn.send(message.encode())

conn.close()

