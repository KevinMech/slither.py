import system
import curses

# Initialize Screen
window = curses.initscr()

# Draw Main Menu
size = window.getmaxyx()
window.addstr(round(size[0] / 2) - 3, round(size[1] / 2) - 7, "Single Player")
window.addstr(round(size[0] / 2) - 1, round(size[1] / 2) - 6, "MultiPlayer")
window.addstr(round(size[0] / 2) + 1, round(size[1] / 2) - 4, "Options")
window.refresh()
window.getch()
curses.endwin()
