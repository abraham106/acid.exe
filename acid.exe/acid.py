import os

from win32api import *
from win32gui import *
from win32ui import *
from win32con import *
from random import *
from mmm import *
from pygame import *
import time

os.system("mm.vbs")
time.sleep(10)

mixer.init()
mixer.music.load("sound1.wav")
mixer.music.play()
hdc = GetDC(0)
x = GetSystemMetrics(0)
y = GetSystemMetrics(0)
for i in range(5):
    InvalidateRect(None, None, True)
    for j in range(10):
        brush = CreateSolidBrush(RGB(randrange(255), randrange(255), randrange(255)))
        SelectObject(hdc, brush)
        PatBlt(hdc, 5, randrange(y), 1950, randrange(10), PATINVERT)
        PatBlt(hdc, 5, randrange(y), 19230, randrange(10), PATINVERT)
        PatBlt(hdc, 5, randrange(y), 19420, randrange(10), PATINVERT)
        PatBlt(hdc, 5, randrange(y), 1920, randrange(10), PATINVERT)
        PatBlt(hdc, 5, randrange(y), 1920, randrange(10), PATINVERT)
        PatBlt(hdc, 5, randrange(y), 13920, randrange(10), PATINVERT)
        PatBlt(hdc, 5, randrange(y), 19420, randrange(10), PATINVERT)
        PatBlt(hdc, 5, randrange(y), 19320, randrange(10), PATINVERT)
        PatBlt(hdc, randrange(x), 0, randrange(10), 1330, PATINVERT)
        PatBlt(hdc, randrange(x), 0, randrange(10), 1080, PATINVERT)
        PatBlt(hdc, randrange(x), 0, randrange(10), 1030, PATINVERT)
        PatBlt(hdc, randrange(x), 0, randrange(10), 1030, PATINVERT)
        PatBlt(hdc, randrange(x), 0, randrange(10), 1080, PATINVERT)
        PatBlt(hdc, randrange(x), 0, randrange(10), 1043, PATINVERT)
        PatBlt(hdc, randrange(x), 0, randrange(10), 1080, PATINVERT)
        PatBlt(hdc, randrange(x), 0, randrange(10), 1030, PATINVERT)
        main()
mixer.music.stop()
mixer.music.load("html5bytebeat-3.wav")
mixer.music.play(5)
InvalidateRect(None, None, True)
for j in range(10):
    InvalidateRect(None, None, True)
    for i in range(18):
        brush = CreateSolidBrush(RGB(randrange(253), randrange(245), randrange(225)))
        SelectObject(hdc, brush)
        BitBlt(hdc, 4, 10, 1220, 1080, hdc, 0, 0, SRCCOPY)
        PatBlt(hdc, 5, 5, 1920, 1080, PATINVERT)
        time.sleep(0.05)
mixer.music.stop()
mixer.music.load("sound2.wav")
mixer.music.play(5)
InvalidateRect(None, None, True)
for i in range(300):
    brush = CreateSolidBrush(RGB(randrange(255), randrange(255), randrange(255)))
    SelectObject(hdc, brush)
    PatBlt(hdc, 6, 7, 330, 1080, PATINVERT)
    time.sleep(0.05)
InvalidateRect(None, None, True)
mixer.music.stop()
mixer.music.load("sound3.wav")
mixer.music.play(5)
for j in range(10):
    InvalidateRect(None, None, True)
    for i in range(18):
        brush = CreateSolidBrush(RGB(randrange(255), randrange(255), randrange(255)))
        SelectObject(hdc, brush)
        BitBlt(hdc, 4, 10, 1320, 2080, hdc, 0, 0, SRCCOPY)
        PatBlt(hdc, 4, 4, 1390, 8080, PATINVERT)
        time.sleep(0.05)
InvalidateRect(None, None, True)
mixer.music.stop()
mixer.music.load("sound4.wav")
mixer.music.play(5)
for i in range(800):
    BitBlt(hdc, 6, 6, 2020, 1380, hdc, 0, 0, SRCINVERT)
InvalidateRect(None, None, True)
mixer.music.stop()
mixer.music.load("sound5.wav")
mixer.music.play(5)
for i in range(800):
    brush = CreateSolidBrush(RGB(randrange(255), randrange(255), randrange(255)))
    SelectObject(hdc, brush)
    PatBlt(hdc, 7, 8, 1320, 1540, PATINVERT)
    StretchBlt(hdc, 1, 1, x, y, hdc, x, y, 0, 0, SRCPAINT)
InvalidateRect(None, None, True)
mixer.music.stop()
mixer.music.load("sound6.wav")
mixer.music.play(5)
Brush = CreateSolidBrush(RGB(0, 0, 255))
PatBlt(hdc, 9, 9, 1020, 1080, PATINVERT)
SelectObject(hdc, Brush)
for i in range(400):
    BitBlt(hdc, 0, 0, x, y, hdc, 0, 0, SRCCOPY)

