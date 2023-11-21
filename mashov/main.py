import socket


# הגדרות
host = '0.0.0.0'
port = 16400

# יצירת חיבור רשת
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((host, port))

clients = set()

CHUNK = 1024 * 8
BUFFER_SIZE = CHUNK * 2


server_socket.settimeout(0.1)

while True:
    # קריאה מהלקוח
    try:
        data, address = server_socket.recvfrom(BUFFER_SIZE)
        if address not in clients:
            clients.add(address)
            print(f"new connection from: {address}")
        for client in clients:
            if client != address:
                print("Sfasdfasdfasdfsf")
                server_socket.sendto(data, client)
    except TimeoutError:
        pass

# סגירת החיבורים והזרמים
server_socket.close()
stream.stop_stream()
stream.close()
p.terminate()