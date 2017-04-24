import socket
import graphics


def start(window):
    window.clear()
    window.refresh()
    connection = _connectServer(window)
    window.getch()
    window.clear()


def _connectServer(window):
    '''Attempts to create a socket and connects the client to the server'''
    center = graphics.findCenter(window)
    window.clear()
    window.addstr(center[0] - 2, center[1] - 16, 'Connecting to server...')
    window.refresh()
    connection = ""
    try:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.settimeout(10)
        clientSocket.connect(('127.0.0.1', 35246))
        connection = clientSocket.recv(1024)
    except Exception as e:
        window.clear()
        window.addstr(center[0] - 2, center[1] - 16, 'Failed to connect to server :(')
        window.addstr(center[0], center[1] - 16, str(e))
        window.refresh()
    if connection == b'connected':
        window.addstr(center[0] - 2, center[1] - 16, 'Found server! Now loading Map...')
    return connection
