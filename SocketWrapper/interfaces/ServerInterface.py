'''
Import Socket interface that the Server class is a child of
'''
from SocketInterface import SocketInterface

##############################
class ServerInterface(SocketInterface):
    '''
    Server Interface, contains methods that a server would need regardless of implementation, such as binding, and tracking the connection socket.
    '''

    def __init__(self) -> None:
        super().__init__()
    
    def _bind_socket(self) -> bool:
        '''
        Binds using the ip and port number. Should catch and OS error, and display the error, and 
        should return false.

        An input state must be flipped to true, to indicate that on a class level, that this object has recieved valid input
        '''
        try:
            super().bind((self.ip, self.port_num))
            
        except OSError as e:
            raise(e)

        self.input_state = True
        return True
    
    #TODO Find a better way to make this connection happen, should make an "accept" method?
    def connect_to_client(self) -> None:
        '''
        Accepts a connection, saving the connection socket. Address returned from accept() is ignored.
        '''
        self.connectionSocket, _ = self.accept()