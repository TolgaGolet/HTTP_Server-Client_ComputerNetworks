# HTTP_Server-Client_ComputerNetworks

# Introduction
Client-server network is basically a relationship in which one program (the client) requests a service or resource from another program (the server). 
This project aims to transmit a message from a server to a client with HTTP protocol. We created two programs act like a client and a server. Firstly, the client connects to the server with the server’s IP address and then makes a request with GET method (command). Then the server gets and processes the request and sends the requested encoded data to the client with headers. Finally, the transmitted message is displayed on the client’s program.

# Step-By-Step Message Tranmission Example:

--------------------Server--------------------

> python Server.py
> http server is starting...
> http server is running…

--------------------Client--------------------

> python Client.py 127.0.0.1
> input command (ex. GET testfile.html): GET testfile.html

--------------------Server--------------------

> Command given by the client is GET command
> Path requested by the client is C:/Users/MTG/Desktop/testfile.html
> 127.0.0.1 - - [11/Nov/2019 22:04:01] "GET testfile.html HTTP/1.1" 200 –

--------------------Client--------------------
 
> Response status: 200 Response reason OK
> Data received from server:
```html
b'<head>\n <title>Message</title>\n <style media="screen">\n   body{\n
> text-align: center;\n   }\n </style>\n</head>\n<body>\n <h1 style="color:red;">Computer Networks 
> Course</h1>\n <h3>This html page was transmitted via http protocol from server to client.</h3>\n</body>\n'
```

> input command (ex. GET testfile.html):
