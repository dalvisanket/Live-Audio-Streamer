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
To run the server, navigate to the directory containing the main server script (server.py) and run the following command:
```python server.py```

To run the client, navigate to the directory containing the client script and run the following command:
```python client.py```

Multiple clients can be run simultaneously by opening multiple terminal windows and running the above client command in each window.

To pause or play the music on the server, enter ```PAUSE``` or ```PLAY``` at the command prompt where server.


## Testing
### Throughput
* In order the test the throughput of the application, the files we are concerned with are ```server.py``` which is the server code of this application, inside the ```throughput_testing``` folder, there are two files ```throughput_client.py``` and ```throughput_test.bat```. ```throughput_client.py``` contains the code to connect to the server and measure the throughput in bytes/sec and  ```throughput_test.bat``` contains the script to connect 1, 5, 10, 20, 35, 50 and 100 clients at the same instance
* First run the server file with ```python server.py``` on cmd. 
* Open a new cmd window and run ```throughput_test.bat``` using  the command ```throughput_test.bat```.
* This will run the ```throughput_client.py``` file and measure the throughput for 20 seconds for each connected client and print on cmd.