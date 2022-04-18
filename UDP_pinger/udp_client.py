import socket
from socket import AF_INET, SOCK_DGRAM
import time

o=0
maxRTT=0
minRTT=0
sum=0

print("Running...")


serverName = '127.0.0.1'
clientSocket = socket.socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
sequence_number = 1

while sequence_number<=10:
    message = 'Ping'
    start= time.time()
    clientSocket.sendto(b'message', (serverName, 1024))

    try:
        context = (f'ping, sequence {sequence_number:d} {sequence_number}')
        [message, address] = clientSocket.recvfrom(1024)
        elapsed = (time.time() - start)
        start_time = time.time()*1000
        end_time = time.time()*1000
        RTT = (time.time() - start)
        print(sequence_number)
        print("RTT is: " +  str(elapsed) + "seconds")
        sum = sum + RTT
        if RTT > maxRTT:
            maxRTT = RTT
        if RTT < RTT:
            minRTT = RTT
        modifiedMessage = message.decode()
        print("sequnece %s %s replay from %s RTT=%fms" % (sequence_number, modifiedMessage, serverName, RTT))

    except socket.timeout:

        print(sequence_number)
        print("Request timed out")
        o=o+1
    sequence_number+=1
    if sequence_number > 10:
        clientSocket.close()

if __name__ == '__main__':
    print("")
    print("Successfully received %d" %(10-o))
    print("The number of the packet loss %d" %(o))
    lost=o/10
    averageRTT = sum / (10-o)
    print(f'Packet loss rate is={lost*100}')
    print(f'MinRTT={minRTT:f}ms')
    print(f'MaxRTT={maxRTT:f}ms')
    print(f'AverageRTT={averageRTT:f}ms')
    print("Request time equals %s" %sum)




