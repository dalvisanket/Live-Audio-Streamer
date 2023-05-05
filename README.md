# Live-Audio-Streamer
Concurrent Audio streamer to multiple clients using socket programming.

## About Project
This project is developed as a part of our Design of Internet Services course under the guidance of Prof. Srinivas Narayana.

The objective of this project is to design and implement an audio streaming system using socket programming. The system enables a sender to stream audio data to multiple receivers simultaneously using a single port. This is achieved through the use of multicast sockets, which allow the sender to transmit data to multiple receivers with a single send operation

## Basic setup requirements
- Python 3.x
- PyAudio <br>
To install the required dependency, run the following command: ```pip install pyaudio```

## Usage
To run the server, navigate to the directory containing the main server script (main.py) and run the following command:
```python main.py```

To run the client, navigate to the directory containing the client script and run the following command:
```python client.py```

Multiple clients can be run simultaneously by opening multiple terminal windows and running the above client command in each window.

To pause or play the music on the server, enter ```PAUSE``` or ```PLAY``` at the command prompt.
