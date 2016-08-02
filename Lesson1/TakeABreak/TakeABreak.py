from time import sleep, ctime
from webbrowser import open


def take_a_break():
    sleep(15)
    return open('https://www.youtube.com/watch?v=uf2-5uDEkS8')

count = 0
total_breaks = 3

print 'program started to run at {}'.format(ctime())

while count < total_breaks:
    take_a_break()
    count += 1
