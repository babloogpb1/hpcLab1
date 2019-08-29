import threading 
import socket
import time
port = 8080
s = socket.socket()
s.bind(('',port))
s.listen(4)
def fn(c):
  f = open('file1.txt','r')
  t1 = time.time()
  for i in range(400):
    d = f.read()
    f.seek(0,0)
    c.send(d.encode('utf-8'))
  print("Time taken: ",time.time()-t1)

  c.send(b'end')
  print("hi")
  a = c.recv(1024)
  print(a)
  f.close()
while True:
  c,addr = s.accept()
  if c:
    print(c)
    t = threading.Thread(target=fn, args=(c,))
    t.start()
    t.join()
  c.close()

