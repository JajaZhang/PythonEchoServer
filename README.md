# PythonEchoServer
This is an example for how to write a thread-based Python TCP echo server. It uses socket programming and establishes a session in a thread to talk to specific host.

The project also equips with Dockerfile for docker container usage.

# Language:
Python 2.7

# Key feature:

1. The server creates a main TCP socket for listening to incoming connections.
2. Each incoming connection is put into a threaded session.
3. The server will be shut down graciously at Termination Signal.

# Motivation:

The project is an example for setting up a TCP echo server with threading and socket programming mainly. It is a good demonstration for the basic socket and serve programming.
It shows how easy you can set up a server in Python!

# Instruction:

Type "Python EchoServer.py" to run the program.


