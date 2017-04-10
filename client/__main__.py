import system
import curses

# Initialize Screen
window = curses.initscr()

# Draw Main Menu
size = window.getmaxyx()
window.addstr("curses init")
window.refresh()
window.getch()
curses.endwin()
