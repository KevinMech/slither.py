import curses


def drawMenu(window, selectMenu):
    size = window.getmaxyx()
    if selectMenu == 0:
        window.addstr(round(size[0] / 2) - 3, round(size[1] / 2) - 7, "Single Player", curses.A_REVERSE)
        window.addstr(round(size[0] / 2) - 1, round(size[1] / 2) - 6, "MultiPlayer")
        window.addstr(round(size[0] / 2) + 1, round(size[1] / 2) - 4, "Options")
    elif selectMenu == 1:
        window.addstr(round(size[0] / 2) - 3, round(size[1] / 2) - 7, "Single Player")
        window.addstr(round(size[0] / 2) - 1, round(size[1] / 2) - 6, "MultiPlayer", curses.A_REVERSE)
        window.addstr(round(size[0] / 2) + 1, round(size[1] / 2) - 4, "Options")
    else:
        window.addstr(round(size[0] / 2) - 3, round(size[1] / 2) - 7, "Single Player")
        window.addstr(round(size[0] / 2) - 1, round(size[1] / 2) - 6, "MultiPlayer")
        window.addstr(round(size[0] / 2) + 1, round(size[1] / 2) - 4, "Options", curses.A_REVERSE)
    window.refresh()
