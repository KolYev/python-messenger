import socket
import stun

def get_local_info():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 0))

    local_address, local_port = sock.getsockname()
    
    print(f"Ваш локальный UDP IP: {local_address}")
    print(f"Ваш локальный UDP порт: {local_port}")
    
def get_external_info():
    nat_type, external_ip, external_port = stun.get_ip_info(
        stun_host='stun.l.google.com', 
        stun_port=19302
    )

    
    print(f"Ваш публичный IP адрес: {external_ip}")
    print(f"Ваш публичный UDP порт: {external_port}")
    print(f"Ваш тип NAT: {nat_type}")
    
get_external_info()