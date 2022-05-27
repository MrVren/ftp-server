import os, socket

from pyftpdlib.authorizers import DummyAuthorizer, AuthenticationFailed
from pyftpdlib.servers import FTPServer
from pyftpdlib.handlers import FTPHandler

from plyer import notification 



def main():
    PATH = 'D:\\WhatFTP_Storage'
    os.chdir(PATH)
    ip = socket.gethostbyname(socket.gethostname())
    addr = (ip, 21)


    authorizer = DummyAuthorizer()
    authorizer.add_user('vren', 
                        '0000', 
                        './vren', 
                        perm = 'elradfmwM', 
                        msg_login = 'Welcome, MrVren', 
                        msg_quit = 'May the Force be with you')

    authorizer.add_user('what', 
                        '1111', 
                        './what', 
                        perm = 'erladfmwM', 
                        msg_login = 'ohayo', 
                        msg_quit = 'alive?')

    authorizer.add_anonymous('./anon')
    handler = Events
    handler.banner = '\nServer ready'
    handler.authorizer = authorizer

    server = FTPServer(addr, handler)
    server.max_cons = 10
    server.max_cons_per_ip = 5

    show_notify('FTP Server', 'Server started')

    server.serve_forever()


def show_notify(title, message):
    notification.notify(title = title, 
                        message = message, 
                        timeout = 5)



class Events(FTPHandler):
    
    def on_connect(self):
        show_notify('FTP Server', 'user connected')
    
    def on_disconnect(self):
        show_notify('FTP Server', 'user disconnected')

    def on_login(self, username):
        show_notify('FTP Server', 'user ' + username + ' log in')
        
    def on_login_failed(self, username, password):
        show_notify('FTP Server', 'Log in failed\nname: ' + 
                    username + '\npassword: ' + password) 

    def on_logout(self, username):
        show_notify('FTP Server', 'user log out')

    def on_file_sent(self, file):
        show_notify('FTP Server', file+' was sent')

    def on_file_received(self, file):
        show_notify('FTP Server', file+' was recieved')

    def on_incomplete_file_sent(self, file):
        show_notify('FTP Server', file+' is not sent')

    def on_incomplete_file_received(self, file):
        show_notify('FTP Server', file+' is not recieved')
        import os
        os.remove(file)



if __name__ == '__main__':
    main() 