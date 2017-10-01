import socket


HOST = ''  
PORT = 8888


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error as msg:
    print('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print "Server is listening ..."
while 1:
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]

    if not data:
        break
#    reply = "Data Received : "+data
#    s.sendto(reply, addr)

    rev_data = ''

    print('Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip())
    #print ('Reverse Message ['+addr[0]+':'+str(addr[1])+'] - '),
    i = len(data)-1
    while i>=0:
        rev_data=rev_data+(data[i])
        i-=1
    #print rev_data
    s.sendto(rev_data,addr)

s.close()
