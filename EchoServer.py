import socket
import threading
from signal import signal, SIGTERM
import sys
import time

def echo(s):
    try:
        while (True):
            statement = s.recv(255)
            if statement == '': 
                break
            s.send(statement + '\n')
            if statement == "quit":  # user quit
                break
    except socket.error:
        print "Socket closed"
    finally:
        s.close()


def startSession(s):        # function starts a session / create a thread
    t = threading.Thread(target=echo, args=(s,))
    t.daemon = True  # Okay to exit if main goes away
    t.start()

def handle_exit(_signum, _frame):
    # Wait until we have no child threads
    print "Waiting for it to be safe to exit"
    while True:
        num = len(threading.enumerate())
        if num == 1:  # just main is running, can exit cleanly
            sys.exit(0)
        time.sleep(.1)

def main():
    signal(SIGTERM, handle_exit)  # insert a signal handler to ensure gracious termination

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP socket
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Resume the port for this socket
    s.bind(('', 9000))  # you may need to change the address and the port if you like
    s.listen(2)  # example here allows 2 connections in the queue. It is customizable. 
    while True:
        (client, address) = s.accept()  # when connection is fully.
        print "accepted: ", address
        client.settimeout(60)
        startSession(client)

if __name__ == "__main__":
    main()
