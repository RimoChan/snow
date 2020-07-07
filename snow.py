import sys
import os
import logging
import inspect
import tempfile

import 位置控制
import 召唤


虚无 = True


位置控制.自动调整()



def nya():
    if len(sys.argv) == 1:
        os.system('pmd')
        sys.exit()
    print('------------------------------------------------------------')

    全名 = sys.argv[1]
    全名.replace('/', '\\')

    路径, 文件名 = os.path.split(全名)
    主名, 扩展名  = os.path.splitext(文件名)
    扩展名 = 扩展名[1:]
    logging.info(f'{路径=}, {文件名=}, {主名=}, {扩展名=}')
    
    exe = f'{主名}.exe'
    if 虚无:
        exe = f'{tempfile.gettempdir()}\\the_program_of_Rimo.exe'
        路径 = tempfile.gettempdir()
       
    os.system(f'title {文件名} - snow')

    if 扩展名 in 召唤.__dict__:
        f = 召唤.__dict__[扩展名]
        需要的参数 = inspect.getfullargspec(f).args
        t = locals()
        填充 = {i:t[i] for i in 需要的参数}
        f(**填充)
    else:
        print(f'「{文件名}」这什么后缀反正我没做')


try:
    nya()
except Exception as e:
    logging.exception(e)

print()
os.system('pause')
