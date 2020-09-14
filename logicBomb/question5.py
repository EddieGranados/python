from random import randint
import ctypes
import datetime

x = 0
counter = 0
now = datetime.datetime.now()
date = now.strftime("%d%m%Y")


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
    Mbox('Your title', 'Your text', 1)


def random_number(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


while 0 < 1:
    fuse = random_number(8)
    counter += 1
    if fuse == int(date):
        while x < 5:
            x += 1
            Mbox('Congragulations!', 'Today is: ' + date +
                 '\nThe counter is: ' + str(counter), 1)
    break
