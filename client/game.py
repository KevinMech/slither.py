import socket
import graphics


def start(window):
    window.clear()
    window.refresh()
    connection = _connectServer(window)
    window.getch()

def _connectServer(window):
    '''Used to connect the client to the server'''
    center = graphics.findCenter(window)
    # Attempt to create a socket
    window.addstr(center[0] - 2, center[1] - 16, 'Creating Socket Connection...')
    try:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as e:
        window.clear()
        window.refresh()
        window.addstr(center[0] - 2, center[1] - 16, 'Failed to create socket connection :(')
        window.addstr(center[0], center[1] - 16, str(e))
        window.getch()
        window.clear()
    # Attempt to connect to server
    window.addstr(center[0] - 2, center[1] - 16, 'Connecting to server...')
    try:
        window.clear()
        window.refresh()
        clientSocket.connect(('127.0.0.1', 35246))
    except Exception as e:
        window.clear()
        window.refresh()
        window.addstr(center[0] - 2, center[1] - 16, 'Failed to connect to server :(')
        window.addstr(center[0], center[1] - 16, str(e))
        window.getch()
        window.clear()
    clientSocket.settimeout(10)
    connection = clientSocket.recv(1024)
    if connection == b'connected':
        window.addstr(center[0] - 2, center[1] - 16, 'Found server! Now loading Map...')
    else:
        window.addstr(center[0] - 2, center[1] - 16, connection)
    return connection
    window.getch()
