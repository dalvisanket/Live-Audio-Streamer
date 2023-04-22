import socket
import pyaudio

def start_client(ip, port):
    # create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = ip

    # connection to hostname on the port.
    client_socket.connect((host, port))

    # initialize pyaudio
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(2), channels=1, rate=44100, output=True)

    while True:
        music = client_socket.recv(1024)
        print(music)
        stream.write(music)

if __name__ == '__main__':
    start_client('127.0.0.1', 9999)