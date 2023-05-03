import socket
import struct
import time

import pyaudio

def start_client(ip, port):
    # create a multicast socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # configure multicast settings
    multicast_group = (ip, port)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    client_socket.bind(('', port))
    group = socket.inet_aton(ip)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    # initialize pyaudio
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(2), channels=1, rate=44100, output=True)

    while True:
        data = client_socket.recv(65507)
        timestamp, music = struct.unpack('<d', data[:8])[0], data[
                                                             8:]  # extract timestamp and music data from received data
        latency = time.time() - timestamp  # calculate latency as difference between current time and timestamp
        print(f'Latency: {latency:.6f} seconds')  # print latency to terminal
        stream.write(music)

if __name__ == '__main__':
    start_client('224.0.0.1', 9999)