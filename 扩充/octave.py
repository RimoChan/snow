import os
import subprocess


def run(path):
    path = path[1:-1]
    f = open(path, encoding='utf-8')
    txt = f.read()
    temp_path = 'C:/Windows/Temp/octave_233.tmp'
    f_temp = open(temp_path, 'w', encoding='gbk')
    f_temp.write(txt.encode('gb2312').decode('gb2312') +
                 '\n fprintf("\\n按两下任意键来退出...(为什么是两下2333)")' +
                 '\npause')
    os.system(r' cd /d D:/Octave/Octave-4.2.1/bin & octave.exe ' + temp_path)
