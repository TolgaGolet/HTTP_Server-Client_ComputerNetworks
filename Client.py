#GET file.html
import http.client
import sys

http_server = sys.argv[1]
conn = http.client.HTTPConnection(http_server)

while 1:
    cmd = input('input command (ex. GET testfile.html): ')
    cmd = cmd.split()

    if cmd[0] == 'exit':
        break

    conn.request(cmd[0], cmd[1])

    rsp = conn.getresponse()

    print('\nResponse status:', rsp.status, 'Response reason', rsp.reason)
    data_received = rsp.read()
    print('Data received from server:', data_received, '\n')

conn.close()
