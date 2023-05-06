import socket
import random
import threading
import math
import struct

def generate_music():
    frequency = random.randint(100, 1000)
    sample_rate = 44100
    duration = 0.5
    num_samples = int(sample_rate * duration)
    data = []
    for i in range(num_samples):
        sample = math.sin(2 * math.pi * frequency * i / sample_rate)
        data.append(struct.pack('<h', int(sample * 32767)))

    return b''.join(data)

def send_music(multicast_socket, multicast_group, playback_state):
    try:
        while True:
            if playback_state['paused']:
                continue
            music = generate_music()
            multicast_socket.sendto(music, multicast_group)

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        multicast_socket.close()

def handle_commands(playback_state):
    while True:
        command = input('Enter command (PAUSE/PLAY): ')
        if command == 'PAUSE':
            playback_state['paused'] = True
        elif command == 'PLAY':
            playback_state['paused'] = False

def start_multicast_server(ip, port):
    multicast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    multicast_group = (ip, port)
    multicast_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
    playback_state = {'paused': False}
    command_thread = threading.Thread(target=handle_commands, args=(playback_state,))
    command_thread.start()
    print("Server started")
    send_music(multicast_socket, multicast_group, playback_state)

if __name__ == '__main__':
    start_multicast_server('224.0.0.2', 9999)