import socket
import stun

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 0))

def get_local_info():
    

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

def send_message():
    message = str(input("Введите сообщение: "))
    IP = str(input("Введите IP адрес того, кому вы хотите отправить сообщение"))
    PORT = str(input("Введите порт того, кому вы хотите отправить сообщение: "))
    sock.sendto(bytes(message, "utf-8"), (IP, PORT))
    
def receive_message():
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"Сообщение с {addr}: {data.decode()}")
    
get_external_info()
send_message()