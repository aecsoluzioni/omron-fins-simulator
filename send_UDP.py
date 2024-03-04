import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 9600
# MESSAGE = "Hello, World!"
MESSAGE = bytearray([0x80,0x00,0x02,0x00,0x00,0x00,0x00,0x05,0x00,0x01,0x01,0x01,0x82,0x00,0x00,0x00,0x00,0x2C])

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
# sock.recvfrom(1024)
# print(sock.recvfrom(1024))


data, addr = sock.recv(1024) 
print ("received message:", data,addr)