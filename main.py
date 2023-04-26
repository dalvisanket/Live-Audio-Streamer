import socket
import random
import threading
import math
import struct

def generate_music():
    # function to generate random sine wave
    frequency = random.randint(100, 1000) # random frequency between 100 and 1000 Hz
    sample_rate = 44100
    duration = 0.5
    num_samples = int(sample_rate * duration)

    # generate sine wave
    data = []
    for i in range(num_samples):
        sample = math.sin(2 * math.pi * frequency * i / sample_rate)
        data.append(struct.pack('<h', int(sample * 32767)))

    return b''.join(data)

def send_music(multicast_socket, multicast_group, playback_state):
    try:
        while True:
            if playback_state['paused']:
                # playback is paused, don't send any music data
                continue

            music = generate_music()
            multicast_socket.sendto(music, multicast_group)
    finally:
        multicast_socket.close()

def handle_commands(playback_state):
    while True:
        # accept PAUSE and PLAY commands from the command line
        command = input('Enter command (PAUSE/PLAY): ')
        if command == 'PAUSE':
            playback_state['paused'] = True
        elif command == 'PLAY':
            playback_state['paused'] = False

def start_multicast_server(ip, port):
    # create a socket object
    multicast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # configure multicast settings
    multicast_group = (ip, port)
    multicast_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)

    # dictionary to keep track of playback state (paused or not)
    playback_state = {'paused': False}

    # create a new thread to handle accepting commands from the command line
    command_thread = threading.Thread(target=handle_commands, args=(playback_state,))
    command_thread.start()

    # start sending music
    send_music(multicast_socket, multicast_group, playback_state)

if __name__ == '__main__':
    start_multicast_server('224.0.0.1', 9999)