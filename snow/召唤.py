import os
import time
import platform
from pathlib import Path
from contextlib import contextmanager

import yaml


命令 = {
    'python': 'python3',
}


q = Path.home() / '.snow/命令.yaml'
if q.is_file():
    with open(q) as f:
        命令.update(yaml.safe_load(f))


if platform.system()=='Windows':
    import win32api
    import win32con


def py(文件名):
    os.system(f'{命令["python"]} "{文件名}"')


def pyj(文件名, 主名):
    if os.path.isfile(f'{主名}.js'):
        open(f'{主名}.js', 'w').close()
    os.system(f'rapydscript "{文件名}" -p -o "{主名}.js" -6')
    _log_编译好了()
    os.system(f'node "{主名}.js"')


def m(文件名):
    import 扩充.octave
    扩充.octave.run(文件名)
    os.system('pause 1>nul')
    exit()


def yaml(文件名):
    import yaml
    with open(文件名, encoding='utf-8') as f:
        print(yaml.safe_load(f.read()))


def lisp(文件名):
    os.system(f'clisp "{文件名}"')


def rb(文件名):
    os.system(f'ruby -w "{文件名}"')


def js(文件名):
    os.system(f'node "{文件名}"')


def mjs(文件名):
    os.system(f'node --experimental-modules "{文件名}"')


def coffee(文件名):
    os.system(f'coffee -c "{文件名}"')


def sass(文件名, 主名):
    with _真视(f'{主名}.css.map'):
        with _真视(f'{主名}.css'):
            os.system(f'sass -E utf-8 "{文件名}" "{主名}.css"')


def lua(文件名):
    os.system(f'lua "{文件名}"')


def sh(文件名):
    os.system(f'cmd /c "{文件名}"')


bat = cmd = sh


def dot(文件名):
    os.system(f'cmd /c del "{主名}.png" > nul 2>&1')
    os.system(f'dot "{文件名}" -Tpng -o "{主名}.png"')
    os.system(f'"{主名}.png"')
    # os.system(f'{命令["python"]} D:/黑科技/ultiviz/ultiviz.py "{文件名}"')


def md(文件名):
    os.system(f'{命令["python"]} D:/黑科技/md轉pdf/md轉pdf.py --md "{文件名}"')


def go(文件名, exe):
    os.system(f'go run "{文件名}"')


def java(路径, 主名, 文件名):
    路径 += '\\Rimo_java'
    os.makedirs(路径, exist_ok=True)
    os.system(f'cmd /c del "{路径}\{主名}.class" > nul 2>&1')
    os.system(f'javac -encoding UTF-8 "{文件名}" -d "{路径}"')
    _log_编译好了()
    os.system(f'java -classpath "{路径}" "{主名}"')


def pas(文件名, exe):
    os.system(f'cmd /c del "{exe}" > nul 2>&1')
    os.system(f'D:/_p/fpc/bin/i386-win32/fpc.exe "{文件名}" -o"{exe}"')
    _log_编译好了()
    os.system(exe)


def cpp(文件名, exe):
    import 扩充.自动include
    os.system(f'cmd /c del "{exe}" > nul 2>&1')
    查询include = 扩充.自动include.查询include(文件名)
    if '-shared' in 查询include:
        exe = '"%s.dll"' % 前名

    os.system('chcp 65001')
    # os.system(r'clang++ %s -o %s -v  -std=c++17 -Wall -Wno-return-type-c-linkage -Wno-invalid-noreturn -Wno-unused-function -Wno-deprecated-declarations -Xclang -flto-visibility-public-std %s' % (文件名, exe, 查询include))

    os.system(f'g++ {文件名} -o {exe} -std=c++17 -Wall -lwsock32 -liphlpapi {扩充.自动include.查询include(文件名)}')

    _log_编译好了()

    if '-shared' in 查询include:
        print('dll生成完了。')
    else:
        os.system(exe)


def rs(文件名):
    os.system(f'cmd /c del "{exe}" > nul 2>&1')
    os.system(f'rustc "{文件名}"')
    _log_编译好了()
    os.system(exe)


def ptml(文件名, 主名):
    with _真视(f'{主名}.html'):
        os.system(f'{命令["python"]} d:/_封閉的git項目/ptml/PTML.py --ptml "{文件名}" --jinja2 0')


def liber(文件名, 主名):
    pdf = f'"{主名}.pdf"'
    print()
    os.system(f'{命令["python"]} D:/Librian/Librian本體/導出文件.py --play {文件名} --out {pdf} --css D:/Librian/Librian本體/資源/導出pdf用/紙樣式.css --css D:/Librian/Librian本體/資源/導出pdf用/樣式_人物名.css --chs')
    os.system(f'start "" {pdf}')


def cs(文件名):
    os.system(f'cmd /c del "{exe}" > nul 2>&1')
    os.system(f'C:/Windows/Microsoft.NET/Framework/v4.0.30319/csc.exe /target:library "{文件名}"')
    _log_编译好了()
    os.system(exe)


def sql(文件名):
    os.system('chcp 65001 1>nul')
    os.system('mysql <%s' % 文件名)


def puml(文件名):
    os.system(f'java -jar D:/_p/plantuml/plantuml.jar -charset UTF-8 "{文件名}"')


@contextmanager
def _真视(文件名):
    if not os.path.isfile(文件名):
        yield
    elif win32api.GetFileAttributes(文件名) & win32con.FILE_ATTRIBUTE_HIDDEN:
        win32api.SetFileAttributes(文件名, win32con.FILE_ATTRIBUTE_NORMAL)
        yield
        win32api.SetFileAttributes(文件名, win32con.FILE_ATTRIBUTE_HIDDEN)
    else:
        yield


def _log_编译好了():
    print('以上是编译结果。')
    print('--------------------------------------------------')
