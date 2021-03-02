import os
import sys
import platform


def pause():
    if platform.system() == 'Windows':
        os.system('pause')
    else:
        import tty, termios
        print('按任意键继续……')
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)