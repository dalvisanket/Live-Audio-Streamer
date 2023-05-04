import time
import socket
import struct

def measure_throughput(server_ip, server_port, duration):
    # create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # configure multicast settings
    multicast_group = (server_ip, server_port)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client_socket.bind(('', server_port))
    group = socket.inet_aton(server_ip)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    start_time = time.time()
    end_time = start_time + duration
    bytes_received = 0

    while time.time() < end_time:
        music = client_socket.recv(65507)
        bytes_received += len(music)

    throughput = bytes_received / duration
    print(f"Throughput: {throughput} bytes/second")
    client_socket.close()

if __name__ == '__main__':
    measure_throughput('224.0.0.2', 9999, 20)
