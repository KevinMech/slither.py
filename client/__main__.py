# import system
import curses
import graphics

# Initialize Screen
window = curses.initscr()
window.keypad(1)
selectMenu = 0
key = None

while True:
    graphics.drawMenu(window, selectMenu)
    key = window.getch()
    if key == curses.KEY_UP and selectMenu > 0:
        selectMenu -= 1
    elif key == curses.KEY_DOWN and selectMenu < 2:
        selectMenu += 1
