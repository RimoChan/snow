import time
import random

import win32api
import win32gui
import win32con


def 获得自我句柄(): 
    原标题 = win32api.GetConsoleTitle()
    新标题 = f'snow({random.random()})'
    win32api.SetConsoleTitle(新标题)
    time.sleep(0.05)
    句柄 = win32gui.FindWindow(None, 新标题)
    win32api.SetConsoleTitle(原标题)
    return 句柄
    
    
def 主显示器右下(margin=7): 
    monitors = win32api.EnumDisplayMonitors()
    区域 = win32api.GetMonitorInfo(monitors[0][0])['Work']
    a, b, c, d = 区域
    x = a
    y = b
    w = c - a
    d = d - b
    return x+w//2, y+d//2, w//2, d//2+margin
    
    
def 副显示器区域(margin=6):
    monitors = win32api.EnumDisplayMonitors()
    区域 = win32api.GetMonitorInfo(monitors[1][0])['Work']
    a, b, c, d = 区域
    x = a
    y = b
    w = c - a
    d = d - b
    return x-margin, y, w+2*margin, d+margin


def 自动调整(): 
    monitors = win32api.EnumDisplayMonitors()
    if len(monitors)==1:
        自我句柄 = 获得自我句柄()
        win32gui.SetWindowPos(自我句柄, win32con.HWND_NOTOPMOST, *主显示器右下() , 0)
    elif len(monitors)==2:
        自我句柄 = 获得自我句柄()
        win32gui.SetWindowPos(自我句柄, win32con.HWND_NOTOPMOST, *副显示器区域(), 0)
