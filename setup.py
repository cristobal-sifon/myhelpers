from __future__ import absolute_import, print_function

from setuptools import setup

from myhelpers.setup_helpers import *


_here = find_location(__file__)


setup(
    name='myhelpers',
    version=find_version('myhelpers/__init__.py'),
    description='Custom helpers'
    author='Cristobal Sifon',
    author_email='sifon@astro.princeton.edu',
    long_description=read(os.path.join(_here, 'README.md')),
    url='https://github.com/cristobal-sifon/myhelpers',
    packages=['myhelpers'],
    zip_safe=False
    )
