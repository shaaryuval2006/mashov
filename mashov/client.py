import socket
import eel

global sock
sock = socket.socket()

def start():
    port = 8080
    print(f"requested port = {8080}, free port found = {port}")
    eel.start("entry_page.html", port=port)

@eel.expose
def move_id(p_id):
    global sock
    print(str(p_id))
    req = post("move_id_to_server", str(p_id))
    sock.sendall(req.encode())
    x = recv_http()
    parts = x.split("\r\n\r\n")
    body = parts[1]
    is_user = (body.strip()=="True")
    print("hello", is_user)
    return is_user


def get(resource: str) -> str:
    print("getting rec", resource)
    return f"GET /{resource} HTTP/1.1\r\n\r\n"


def post(resource: str, data: str = "") -> str:
    return f"POST /{resource} HTTP/1.1\r\nContent-Length: {len(data)}\r\n\r\n{data}"



def recv_http():
    global sock
    msg = b''
    while True:
        data = sock.recv(1)

        msg += data

        if len(data) == 0:
            return False, ""

        if b'\r\n\r\n' in msg:
            break
    if b"Content-Length: " in msg:
        x = int(msg[msg.index(b"Content-Length: ") + 16:].split(b'\r\n')[0])
        data = b""
        while len(data) < x:
            data += sock.recv(x - len(data))
        msg += data
    return msg.decode()


def main():
    global sock
    eel.init(".\\")
    sock.connect(('127.0.0.1', 8080))
    start()


if __name__ == '__main__':
    main()










