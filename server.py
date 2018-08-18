import socket
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print ("hurre")
host="127.0.0.1"
port = 12397
remote_ip = socket.gethostbyname(host)
print("IP Address of " + host + " is " + remote_ip)
print("Socket connected to " + host + " on ip " + remote_ip)
serversocket.bind((host, port))

serversocket.listen(5)
print ('cvam_server start')
while 1:
    (clientsocket, address) = serversocket.accept()
    print ("connection found!")
    data = clientsocket.recv(1024).decode()
    print (data)
    r='Recive'
    clientsocket.send(r.encode())
    
