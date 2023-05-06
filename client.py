import socket
import struct
import pyaudio

def start_client(ip, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client_socket.bind(('', port))
    group = socket.inet_aton(ip)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(2), channels=1, rate=44100, output=True)

    print("Client started and joined multicast group")

    while True:
        try:
            music = client_socket.recv(65507)
            stream.write(music)
        except Exception as e:
            print(f"Error occurred: {e}")

if __name__ == '__main__':
    start_client('224.0.0.2', 9999)