import os, socket

from pyftpdlib.authorizers import DummyAuthorizer, AuthenticationFailed
from pyftpdlib.servers import FTPServer
from pyftpdlib.handlers import FTPHandler



def main():
    PATH = '.'
    os.chdir(PATH)
    ip = socket.gethostbyname(socket.gethostname())
    addr = (ip, 21)


    authorizer = DummyAuthorizer()
    authorizer.add_user('vren', 
                        '0000', 
                        '.', 
                        perm = 'elradfmwMT', 
                        msg_login = 'Welcome, MrVren', 
                        msg_quit = 'May the Force be with you')

    authorizer.add_user('what', 
                        '1111', 
                        '.', 
                        perm = 'erladfmwMT', 
                        msg_login = 'ohayo', 
                        msg_quit = 'alive?')

    authorizer.add_anonymous('.')
    handler = Events
    handler.banner = '\nServer ready'
    handler.authorizer = authorizer

    server = FTPServer(addr, handler)
    server.max_cons = 10
    server.max_cons_per_ip = 5


    server.serve_forever()



class Events(FTPHandler):

    def on_incomplete_file_received(self, file):
        import os
        os.remove(file)

    



if __name__ == '__main__':
    main() 