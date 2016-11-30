FROM python:2-onbuild
EXPOSE 9000
CMD [ "python", "./EchoServer.py" ]
