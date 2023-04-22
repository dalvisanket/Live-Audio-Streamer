import socket
import random
import threading
import math
import struct

def generate_music():
    # function to generate random sine wave
    frequency = random.randint(100, 1000) # random frequency between 100 and 1000 Hz
    sample_rate = 44100
    duration = 1 # 1 second duration
    num_samples = sample_rate * duration

    # generate sine wave
    data = []
    for i in range(num_samples):
        sample = math.sin(2 * math.pi * frequency * i / sample_rate)
        data.append(struct.pack('<h', int(sample * 32767)))

    return b''.join(data)

def handle_client(client_socket, playback_state):
    try:
        while True:
            if playback_state['paused']:
                # playback is paused, don't send any music data
                continue

            music = generate_music()
            client_socket.send(music)
    except ConnectionResetError:
        # client has disconnected
        print("Client has disconnected")
    finally:
        # close the socket for this client
        client_socket.close()

def handle_commands(playback_state):
    while True:
        # accept PAUSE and PLAY commands from the command line
        command = input('Enter command (PAUSE/PLAY): ')
        if command == 'PAUSE':
            playback_state['paused'] = True
        elif command == 'PLAY':
            playback_state['paused'] = False

def start_server(ip, port):
    # create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = ip

    # bind the socket to a public host, and a well-known port
    server_socket.bind((host, port))

    # become a server socket
    server_socket.listen(5)

    # dictionary to keep track of playback state (paused or not)
    playback_state = {'paused': False}

    # create a new thread to handle accepting commands from the command line
    command_thread = threading.Thread(target=handle_commands, args=(playback_state,))
    command_thread.start()

    while True:
        # establish a connection
        client_socket, addr = server_socket.accept()

        print("Got a connection from %s" % str(addr))

        # create a new thread to handle this client connection
        client_thread = threading.Thread(target=handle_client, args=(client_socket, playback_state))
        client_thread.start()

if __name__ == '__main__':
    start_server('127.0.0.1', 9999)