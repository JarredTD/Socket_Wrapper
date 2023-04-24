'''
Imports the Socket interface that the Client interface is a child of
'''
from SocketInterface import SocketInterface

##############################

class ClientInterface(SocketInterface):
    '''
    Client Interface, contains methods that a client would need, regardless of implementation of the client
    such as connection to a socket.
    '''
    def __init__(self) -> None:
        super().__init__()

    def _connect_socket(self) -> bool:
        '''
        Connects using the ip and port number. Should catch and OS error, and display the error, and 
        should return false.
        '''
        try:
            self.connect((self.ip, self.port_num))
        except OSError as e:
            print(f"Error {e.errno}: {e.strerror}")
            return False

        self.input_state = True
        return True