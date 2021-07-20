from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.blind((HOST,PORT))            #connect to server (block until accept)
s.send("Hello World")           #send same data
data = s.recv(1024)             #receive the response
print data                      #print the results
s.close()                       #close the connection 