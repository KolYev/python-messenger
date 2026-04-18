import socket
from requests import get

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('', 0))

local_address, local_port = sock.getsockname()

ip = get('https://api.ipify.org').content.decode('utf8')


print(f"Ваш локальный UDP IP: {local_address}")
print(f"Ваш локальный UDP порт: {local_port}")
print('Ваш публичный IP адрес: {}'.format(ip))