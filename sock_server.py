import socketserver
import json

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        mydata = json.dumps(str(self.data))
        if 'multidispensing' in mydata:
            self.request.sendall(bytes('{"result":"SUCESS"}',encoding = 'utf-8'))
        else:
            self.request.sendall(bytes('{"result":"ERROR"}',encoding = 'utf-8'))
              
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
