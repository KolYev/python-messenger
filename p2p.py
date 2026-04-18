import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('', 0))

local_address, local_port = sock.getsockname()

print(f"Ваш локальный UDP IP: {local_address}")
print(f"Ваш локальный UDP порт: {local_port}")