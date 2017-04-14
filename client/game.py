import socket
import graphics


def start(window):
    window.clear()
    window.refresh()
    _connectServer(window)
    window.getch()


def _connectServer(window):
    '''Used to connect the client to the server'''
    center = graphics.findCenter(window)
    # Attempt to create a socket
    window.addstr(center[0], center[1], 'Creating Socket Connection...')
    try:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as e:
        window.addstr(center[0], center[1], 'Failed to create socket connection :(')
        window.addstr(center[0] + 1, center[1], str(e))
    # Attempt to connect to server
    window.addstr(center[0], center[1], 'Connecting to server...')
    try:
        clientSocket.connect(('127.0.0.1', 35246))
    except Exception as e:
        window.addstr(center[0] - 2, center[1] - 1, 'Failed to connect to server :(')
        window.addstr(center[0] + 1, center[1] - 1, str(e))
