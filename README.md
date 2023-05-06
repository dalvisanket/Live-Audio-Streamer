# Live-Audio-Streamer
Concurrent Audio streamer to multiple clients using socket programming.

## About Project
This project is developed as a part of our Design of Internet Services course under the guidance of Prof. Srinivas Narayana.

The objective of this project is to design and implement an audio streaming system using socket programming. The system enables a sender to stream audio data to multiple receivers simultaneously using a single port. This is achieved through the use of multicast sockets, which allow the sender to transmit data to multiple receivers with a single send operation

## Contributors

Sanket Dalvi (sd1482) [GitHub](https://github.com/dalvisanket) [LinkedIn](https://www.linkedin.com/in/-sanketdalvi-/)
<br>
Swapnil Verlekar (sv725) [GitHub](https://github.com/swapnilverlekar) [LinkedIn](https://www.linkedin.com/in/swapnilverlekar/) <br>

## Basic setup requirements
- Python 3.x
- PyAudio <br>
To install the required dependency, run the following command: ```pip install pyaudio```

## Usage - Running the project on Local machine

- Clone the repository using ```git clone https://github.com/dalvisanket/Live-Audio-Streamer.git```

- Navigate to the project directory with ```cd Live-Audio-Streamer``` 

- To run the server, from the directory containing the main server script (server.py) run the following command:
```python server.py```

- To run the client, from the directory containing the client script run the following command on a new window:
```python client.py```

- Multiple clients can be run simultaneously by opening multiple terminal windows and running the above client command in each window.

- To pause or play the music on the server, enter ```PAUSE``` or ```PLAY``` at the command prompt where server.

## Testing

### Latency and Jitter
To test the latency and jitter of the program, a separate version of the server and client has been created with minor code changes. These changes track the time using the ```time()``` function and have all the code to perform all the necessary measurements.

1. Within the ```latency_jitter_testing``` directory, there are two scripts: ```latency_jitter_server.py``` and ```latency_jitter_client.py```.
2. First, run the server script by executing the command ```python latency_jitter_server.py``` in the command prompt.
3. In a new command prompt window, run ```python latency_jitter_client.py```.
4. This script contains code changes to measure the latency and jitter of the program. All functionality, including ```PLAY``` and ```PAUSE```, functions.
5. The latency and jitter measurements will be displayed on the client terminal.

### Throughput
In order the test the throughput of the application, the files we are concerned with are ```server.py``` which is the server code of this application, inside the ```throughput_testing``` folder, there are two files ```throughput_client.py``` and ```throughput_test.bat```. ```throughput_client.py``` contains the code to connect to the server and measure the throughput in bytes/sec and  ```throughput_test.bat``` contains the script to connect 1, 5, 10, 20, 35, 50 and 100 clients at the same instance
1. First run the server file with ```python server.py``` on cmd. 
2. Open a new cmd window and run ```throughput_test.bat``` using  the command ```throughput_test.bat```.
3. This will run the ```throughput_client.py``` file and measure the throughput for 20 seconds for each connected client and print on cmd.

## Results Overview

### Latency
<img width="400" alt="Latency graph" src="https://user-images.githubusercontent.com/48671736/236635594-46556260-1236-4590-a238-9b85d4b27704.png">

The recorded data indicates that the system performs well overall, with low latency and jitter values for most measurements.

### Jitter 
<img width="800" alt="Jitter graph" src="https://user-images.githubusercontent.com/48671736/236635338-39a4c721-84c1-4e1d-aa9c-9dcc3b782455.jpeg">

Low jitter values indicate stable network conditions and consistent delivery of audio data, while an increase in jitter values suggests the presence of network congestion or other factors contributing to increased variability in latency.

### Throughput
<img width="400" alt="Throughput graph" src="https://user-images.githubusercontent.com/48671736/236635535-c076f3cc-069f-45cc-b5e4-6648288c86f8.jpeg">

The code measures the throughput of music data received from a server over a duration of 20 seconds by creating a socket object, configuring multicast settings, and calculating the average number of bytes received per second. The graph provided shows that the server can handle up to 20 clients without any significant decrease in performance, but as more clients are added beyond this point, the server’s ability to transmit data efficiently begins to decline.

## Demo screenshots
On left : Server program running and music being streamed on 224.0.0.2:9999. Server provides an option to pause the music or continue playing.

On right : A single client connected to the server and listening to music

<img width="1000" alt="ss1_audio_streamer" src="https://user-images.githubusercontent.com/48671736/236636802-9b545cfa-1d07-426b-b3e7-8e16ea4fe117.jpeg">

Same setup as the above one but with multiple clients connected to the server and listening simultaneously.
<img width="1000" alt="ss2_audio_streamer" src="https://user-images.githubusercontent.com/48671736/236636850-df03b833-f144-4a2b-a019-431439a73999.jpeg">



### References

https://docs.github.com/en <br>
https://app.diagrams.net/ <br>
https://www.atatus.com/blog/jitter-vs-latency/ <br>
https://www.geeksforgeeks.org/socket-programming-python/ <br>
https://pymotw.com/2/socket/multicast.html <br>
https://www.geeksforgeeks.org/differences-between-tcp-and-udp/ <br>
https://www.baeldung.com/cs/bandwidth-packet-loss-latency-jitter <br>
