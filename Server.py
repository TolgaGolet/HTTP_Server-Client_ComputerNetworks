from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class customHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        rootdir = 'D:/MTG/Desktop'
        try:
            if self.path.endswith('.html'):
                print('Command given by the client is', self.command, 'command')
                dir = rootdir + self.path
                print('Path requested by the client is', dir)
                f = open(dir)

                self.send_response(200)

                self.send_header('Content-type', 'text-html')
                self.end_headers()


                self.wfile.write(f.read().encode())
                f.close()
                return

        except IOError:
            self.send_error(404, 'file not found')

def run():
    print('http server is starting...')

    server_address = ('0.0.0.0', 80)
    httpd = HTTPServer(server_address, customHTTPRequestHandler)
    print('http server is running...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
