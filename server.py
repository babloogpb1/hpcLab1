
import time
import os
import socket 
port = 8080
#addr = '127.0.0.1'
soc = socket.socket()
soc.bind(('',port))
soc.listen(4)
while True:
  c = 0
  print(c)
  c,addr = soc.accept()
  #print(c)
  if c != 0:
   print(c) 
   n = os.fork()
  if n <= 0:
  #c.send(b'Hello Client!')
    f = open('file1.txt', 'r')
    for i in range(400):
      data = f.read()
      f.seek(0, 0)
      #print()
      c.send(data.encode('utf-8'))
    print("here")
    c.send(b'end')
    print("hiii")
    a = c.recv(1024)
    print(a)
    f.close()
    #time.sleep(20)
