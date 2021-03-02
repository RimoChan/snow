import os

import yaml

module_path = os.path.dirname(__file__)
with open(module_path + '/自动include对应.yaml', encoding='utf8') as f:
    对应 = yaml.safe_load(f)


def 读取(code):
    if code[0] == '"' and code[-1] == '"':
        code = code[1:-1]
    f = open(code, encoding='utf8')
    return f.read()


def 需要include(code):
    t = 读取(code)
    for i in 对应:
        if t.find(i) != -1:
            return True


def 查询include(code):
    txt = 读取(code)
    全部 = []
    for i in 对应:
        if txt.find(i) != -1:
            print('使用了%s。' % i)
            for j in 对应[i]:
                全部.append(j)
    return ' '.join(全部)
