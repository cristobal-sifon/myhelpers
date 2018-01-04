from __future__ import absolute_import, print_function

from setuptools import setup

from setup_helpers import *


_here = os.path.abspath(os.path.dirname(__file__))


setup(
    name='setup_helpers',
    version=find_version('setup_helpers/__init__.py'),
    description='Package installation and setup helpers',
    author='Cristobal Sifon',
    author_email='sifon@astro.princeton.edu',
    long_description=read(os.path.join(_here, 'README.md')),
    url='https://github.com/cristobal-sifon/setup_helpers',
    packages=['setup_helpers'],
    zip_safe=False
    )
