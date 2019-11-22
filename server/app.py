import time
import zmq

context = zmq.Context()

socket = context.socket(zmq.REP)

socket.bind("tcp://0.0.0.0:5555")
print("socket on")
while True:
    message = socket.recv()
    print("Received request: %s" % message)

    time.sleep(1)

    socket.send(b"World")