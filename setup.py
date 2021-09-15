"""fbs tutorial

See:
https://github.com/mherrmann/fbs-tutorial
"""

from os.path import relpath, join
from setuptools import setup, find_packages

import os

description = 'fbs tutorial'
setup(
    name='fbs-tutorial',
    version='1.0.0',
    description=description,
    long_description=
        description + '\n\nSee: https://github.com/mherrmann/fbs-tutorial',
    author='Michael Herrmann',
    author_email='michael+removethisifyouarehuman@herrmann.io',
    url='https://github.com/mherrmann/fbs-tutorial',
    install_requires=[
        "fbs;          python_version == '3.5' or python_version == '3.6'",
        "PyQt5==5.9.2; python_version == '3.5' or python_version == '3.6'",
        "fbs-tutorial-shim; python_version >= '3.7'"
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
    
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    
        'Operating System :: OS Independent',
    
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',

        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    license='GPLv3 or later',
    keywords='PyQt',
    platforms=['MacOS', 'Windows', 'Debian', 'Fedora', 'CentOS', 'Arch']
)