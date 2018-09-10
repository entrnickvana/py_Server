
import socket

hostname, sld, tld, port = 'www', 'theberrics', 'com', 80
target = '{}.{}.{}'.format(hostname, sld, tld)

# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
# client.connect((target, port))
client.connect(('127.0.0.1', 1256))

# ------------------- FOR WEB ADDRESSES  ----------------------------------------
# addr_str = 'GET /index.html HTTP/1.1\r\nHost: {}.{}\r\n\r\n'.format(sld, tld)
# encoded_str = addr_str.encode()

msg = 'My name is Jonas'

# send some data (in this case a HTTP GET request)
client.send(msg.encode())

# receive the response data (4096 is recommended buffer size)
response = client.recv(4096)

print(response)