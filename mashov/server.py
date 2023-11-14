import socket
import os.path
import threading

person_id = 0
check_id = False

class ClientHandler:
    def __init__(self, client_socket):
        self.s = client_socket

    def handler(self):
        is_ok = True
        while is_ok:
            is_ok, url = self.handle_request()
            self.send_response(url)


    def handle_request(self):
        global person_id
        try:
            is_ok = False
            msg = b''
            while True:
                data = self.s.recv(1)

                msg += data

                if len(data) == 0:
                    return False, ""

                if b'\r\n\r\n' in msg:
                    is_ok = True
                    break
            if b"Content-Length: " in msg: 
                x = int(msg.split(b"Content-Length: ")[-1].split(b"\r\n")[0])
                data = b""
                while len(data) < x:
                    data += self.s.recv(x-len(data))
                msg += data
            data = msg.decode()
            list_of_req = str(data).split()

            url = list_of_req[1]
            if data.startswith('POST'):
                if url == "/move_id_to_server":
                    person_id = data.split("\r\n\r\n")[-1]
            
            msg = msg.decode()
            return is_ok, url
        except(ConnectionError, socket.error):
            return False, ""

    def send_response(self, url):
        global person_id, check_id
        try: 
            print(url)
            if url == "/move_id_to_server":
                for teacher in Teachers.teachers_id:
                    print(teacher)
                    if person_id == str(teacher.t_id):
                        check_id = True
                        print(check_id)
                        break
                self.s.send(f"HTTP/1.1 200 ok\r\nContent-Type: application/json\r\nContent-Length: {len(str(check_id))}\r\nAccess-Control-Allow-Origin: *\r\n\r\n".encode() + str(check_id).encode())
                person_id = 0
                check_id = False
                return True

            print(url)
            url = url[1::]
            if not os.path.isfile(url):
                self.s.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
                return False

            file_type = url.split('.')[-1]
            file_data = ""
            with open(url, "rb") as file:
                file_data = file.read()

            if 'jpg' in file_type or 'jpeg' in file_type or 'ico' in file_type or 'gif' in file_type:
                file_type = f"image/{file_type}"
            else:
                file_type = f"text/{file_type}"

            header = f"HTTP/1.1 200 OK\r\nContent-Type: {file_type}; charset=utf-8\r\nContent-Length: {len(file_data)}"
            self.s.send((header + "\r\n\r\n").encode() + file_data)
            return True
        except(ConnectionError, socket.error):
            return False

    def check_http(self, req):
        print(req)
        if not req.endswith("\r\n\r\n"):
            return False, ""
        list_of_req = str(req).split()
        cmd_itself = list_of_req[0]
        url = list_of_req[1]
        protocol = list_of_req[:3]
        if not (cmd_itself == "GET" and list_of_req[2] == 'HTTP/1.1'):
            return False, ""

        if cmd_itself == "GET":
            return True, url


class Teacher:
    def __init__(self, name, t_id, subject):
        self.name = name
        self.t_id = t_id
        self.subject = subject
    def __repr__(self) -> str:
        return f"{self.name} {self.t_id} {self.subject}"  

class Teachers:
    teachers_id = [Teacher("Eli", 12345, "Computers"),Teacher("Shimon", 54321, "Math"),Teacher("Fima", 13524, "Computers"),Teacher("Orly", 69696, "Hebrew")]


class Student:
    def __init__(self, name, s_id, subject):
        self.name = name
        self.s_id = s_id
        self.subject = subject

class Students:
    students = [Student("Tomer", 67890, 0),Student("Yuval", 98760, 0),Student("Simhi", 89706, 0),Student("Menachem", 77777, 0)]


class Server:
    def __init__(self):
        self.server_socket = socket.socket()
        self.server_socket.bind(("0.0.0.0", 8080))
        self.amount_of_clients = 10
        self.client_sockets = []
        self.server_socket.listen(self.amount_of_clients)

    def main(self):
        client_socket, client_address = self.server_socket.accept()
        self.client_sockets.append(client_socket)
        ch = ClientHandler(client_socket)
        client_t = threading.Thread(target=ch.handler, daemon=True)

        client_t.start()

    def start(self):
        while True:
            self.main()


if __name__ == "__main__":
    s = Server()
    s.start()
