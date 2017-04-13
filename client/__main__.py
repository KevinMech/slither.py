# import system
import curses
import graphics

# Initialize Screen
window = curses.initscr()
window.keypad(1)
selectMenu = 0

while True:
    graphics.drawMenu(window, selectMenu)
    key = window.getch()
    if key == curses.KEY_UP and selectMenu > 0:
        selectMenu -= 1
    elif key == curses.KEY_DOWN and selectMenu < 2:
        selectMenu += 1
    elif key == 10:
        size = window.getmaxyx()
        if selectMenu == 0:
            pass
        elif selectMenu == 1:
            window.addstr(size[0] - 1, 0, 'Multiplayer not supported yet!')
        else:
            window.clear()
            window.addstr(size[0] - 1, 0, 'Config not supported yet!')
