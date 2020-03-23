import socket
import time

Nelson = 'gaylord'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDP_IP = '10.0.0.4'
UDP_PORT = 1337

while 'gay' in Nelson:
	sock.sendto(bytes('Zmly','utf-8'), (UDP_IP, UDP_PORT))
	time.sleep(1)
	sock.sendto(bytes('c3RwY','utf-8'), (UDP_IP, UDP_PORT))
	time.sleep(1)
	sock.sendto(bytes('XJ0Cg==','utf-8'), (UDP_IP, UDP_PORT))
	time.sleep(15)


