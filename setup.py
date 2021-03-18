import setuptools


setuptools.setup(
    name='snow',
    version='0.0.2',
    author='RimoChan',
    author_email='the@librian.net',
    description='snow',
    long_description=open('readme.md', encoding='utf8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/RimoChan/snow',
    packages=[
        'snow',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'fire>=0.3.1',
    ],
)
