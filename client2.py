import socket
soc = socket.socket()
port = 8080
addr = '127.0.0.1'
soc.connect((addr, port))
f = open("rec2.txt", "w")
while 1:
  data = soc.recv(1024)
  #print(data)
  z = data.decode('utf-8')
  if z[len(z)-1] == 'd':
    break
#data = soc.recv(10240)
  f.write(data.decode('utf-8'))
  data = 0
  #else:
    #break
f.close()
print("here")
soc.send(b'Hello Server...!!')
soc.close()
