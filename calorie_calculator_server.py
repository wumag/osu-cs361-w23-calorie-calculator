import zmq
import time
import os

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:6666")

history = [
    "User gender: f",
    "User weight(kgs): 55.0",
    "User height(cm): 166.0",
    "User age: 23",
    "User activity level: active",
    "You need to eat 2547.8250000000003 calories a day to maintain your current weight"
]

clear = lambda: os.system('clear')

print("Connecting to Calorie Calculator...")
time.sleep(5)
clear()

def main():
    while True:
        msg = socket.recv()
        print("Waiting for request from client...")
        print(f"Request received: {msg}")

        msg = msg.decode('UTF-8')
        params = msg.split(' ')
        variable = str(params[1])

        if variable == 'gender':
            i = 0
        
        if variable == 'weight':
            i = 1

        if variable == 'height':
            i = 2

        if variable == 'age':
            i = 3  

        if variable == 'activity':
            i = 4

        if variable == 'calories':
            i = 5

        socket.send_string(history[i])
        print("Response sent to client!")
        print("--------------------------------")

if __name__ == '__main__':
    main()