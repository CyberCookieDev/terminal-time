from pyfiglet import Figlet
import curses
from datetime import datetime
import os
import colorama
import time

def get_hour():
    date_time = datetime.now()
    time = datetime.strftime(date_time, "%H : %M : %S")
    return time
def get_date():
    return datetime.now().strftime("%Y-%m-%d")  # Get current date

def clocking(stdscr):
    curses.curs_set(0)
    f = Figlet(font='big')

    while True:
        height, width = stdscr.getmaxyx()

        time_text = f.renderText(get_hour())
        date_text = get_date()

        time_lines = time_text.splitlines()
        date_lines = date_text.splitlines()

        start_x = (width - max(len(line) for line in time_lines)) // 2
        start_y = (height - len(time_lines) - len(date_lines)) // 2

        stdscr.clear()
        for i, line in enumerate(time_lines):
            stdscr.addstr(start_y + i, start_x, line)

        for i, line in enumerate(date_lines):
            stdscr.addstr(start_y + len(time_lines) + i, start_x, line)

        stdscr.refresh()
        time.sleep(1)

curses.wrapper(clocking)

