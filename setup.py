from setuptools import setup
from os import path

def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

setup(
    name='denv',
    version='1.4.2',
    author='sloev',
    author_email='jgv@trustpilot.com',
    url='https://github.com/trustpilot/python-denv',
    description='runs commands with env stored in dotfile',
    long_description=read_md('README.md'),
    packages=['denv'],
    entry_points={
        'console_scripts': [
            'denv=denv:main',
        ],
    },
    license='MIT'
)
