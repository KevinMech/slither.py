import curses


def findCenter(window):
    '''Find half the screen size for both width and height'''
    size = window.getmaxyx()
    halfheight = round(size[0] / 2)
    halfwidth = round(size[1] / 2)
    center = (halfheight, halfwidth)
    return center


def drawMenu(window, selectMenu):
    '''Draw menu to the terminal screen'''
    options = ['Single Player', 'Multiplayer', 'Options']
    selection = [curses.A_REVERSE, curses.A_NORMAL, curses.A_NORMAL]
    halfheight = findCenter(window)[0]
    halfwidth = findCenter(window)[1]

    # Menu Selection
    if selectMenu == 1:
        selection = [curses.A_NORMAL, curses.A_REVERSE, curses.A_NORMAL]
    elif selectMenu == 2:
        selection = [curses.A_NORMAL, curses.A_NORMAL, curses.A_REVERSE]

    # Draw menu to screen
    window.addstr(halfheight - 3, halfwidth - 7, options[0], selection[0])
    window.addstr(halfheight - 1, halfwidth - 6, options[1], selection[1])
    window.addstr(halfheight + 1, halfwidth - 4, options[2], selection[2])
    window.refresh()

    # Old code saved as reference; will be phased out
    # if selectMenu == 0:
    #     window.addstr(round(size[0] / 2) - 3, round(size[1] / 2) - 7, "Single Player", curses.A_REVERSE)
    #     window.addstr(round(size[0] / 2) - 1, round(size[1] / 2) - 6, "MultiPlayer")
    #     window.addstr(round(size[0] / 2) + 1, round(size[1] / 2) - 4, "Options")
    # elif selectMenu == 1:
    #     window.addstr(round(size[0] / 2) - 3, round(size[1] / 2) - 7, "Single Player")
    #     window.addstr(round(size[0] / 2) - 1, round(size[1] / 2) - 6, "MultiPlayer", curses.A_REVERSE)
    #     window.addstr(round(size[0] / 2) + 1, round(size[1] / 2) - 4, "Options")
    # else:
    #     window.addstr(round(size[0] / 2) - 3, round(size[1] / 2) - 7, "Single Player")
    #     window.addstr(round(size[0] / 2) - 1, round(size[1] / 2) - 6, "MultiPlayer")
    #     window.addstr(round(size[0] / 2) + 1, round(size[1] / 2) - 4, "Options", curses.A_REVERSE)
