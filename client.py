import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socked created!")

host = "127.0.0.1"
port = 12397

remote_ip = socket.gethostbyname(host)

print("IP Address of " + host + " is " + remote_ip)

s.connect((remote_ip, port))

print("Socket connected to " + host + " on ip " + remote_ip)

message = b"GET / HTTP/1.1\r\n\r\n"
s.sendall(message)

reply = s.recv(4096)

print(reply)
