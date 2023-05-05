import socket
import struct
import pyaudio
import time

def start_client(ip, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    multicast_group = (ip, port)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client_socket.bind(('', port))
    group = socket.inet_aton(ip)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(2), channels=1, rate=44100, output=True)

    print("Client started and joined multicast group")

    prev_latency = None
    while True:
        try:
            music = client_socket.recv(65507)
            timestamp, music = struct.unpack('<d', music[:8])[0], music[8:]
            latency = time.time() - timestamp

            if prev_latency is not None:
                jitter = abs(latency - prev_latency)
                print(f'Jitter: {jitter:.6f} seconds')

            prev_latency = latency

            print(f'Latency: {latency:.6f} seconds')
            stream.write(music)
            print("Received and playing music data")
        except Exception as e:
            print(f"Error occurred: {e}")

if _name_ == '_main_':
    start_client('224.0.0.2', 9999)