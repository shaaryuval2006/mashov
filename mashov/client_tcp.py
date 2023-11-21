import socket
import time

import pyaudio

# Server
HOST = '109.186.154.12'
PORT = 16400
SERVER_ADDR = (HOST, PORT)
# הגדרות זמן וקצב דומציה
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024 * 8
BUFFER_SIZE = CHUNK * 2


def main():
    # יצירת חיבור רשת
    client_socket = socket.socket()
    client_socket.connect(SERVER_ADDR)

    # יצירת אובייקט PyAudio
    p = pyaudio.PyAudio()

    # יצירת קלט קולי
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    output=True,
                    frames_per_buffer=CHUNK)
    client_socket.settimeout(0.1)
    while True:
        data = stream.read(CHUNK)
        client_socket.send(data)
        try:
            data = client_socket.recv(BUFFER_SIZE)
            stream.write(data)
        except TimeoutError:
            pass
        time.sleep(0.02)

    # סגירת החיבורים והזרמים
    client_socket.close()
    stream.stop_stream()
    stream.close()
    p.terminate()


if __name__ == '__main__':
    main()