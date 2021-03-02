import os
import sys
import logging
import inspect
import tempfile
import platform

import fire

from snow import 召唤
from snow.utils import pause


def nya(file=None, 虚无=True, 独立=True):
    if platform.system() == 'Windows' and 独立:
        from snow import 位置控制
        位置控制.自动调整()
    try:
        if file is None:
            os.system('pmd')
            sys.exit()

        全名 = file
        全名.replace('/', '\\')

        路径, 文件名 = os.path.split(全名)
        主名, 扩展名 = os.path.splitext(文件名)
        扩展名 = 扩展名[1:]
        logging.info(f'{路径=}, {文件名=}, {主名=}, {扩展名=}')

        if 独立:
            print('------------------------------------------------------------')
            os.system(f'title {文件名} - snow')

        os.chdir(路径)

        exe = f'{主名}.exe'
        if 虚无:
            exe = f'{tempfile.gettempdir()}\\the_program_of_Rimo.exe'
            路径 = tempfile.gettempdir()

        if 扩展名 in 召唤.__dict__:
            f = 召唤.__dict__[扩展名]
            需要的参数 = inspect.getfullargspec(f).args
            t = locals()
            填充 = {i: t[i] for i in 需要的参数}
            f(**填充)
        else:
            print(f'「{文件名}」这什么后缀反正我没做')
    except Exception as e:
        logging.exception(e)

    if 独立:
        print()
        pause()


fire.Fire(nya)
