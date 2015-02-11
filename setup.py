#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import (
    setup,
    find_packages,
    )

install_requires = [
    'mako',
    ]
test_require = []


def find_package_data(target, package_root):
    return [
        os.path.relpath(os.path.join(root, filename), package_root)
        for root, dirs, files in os.walk(target)
        for filename in files
        ]
package_data = {
    'scaff': ['templates/**']
    }

setup(
    name='scaff',
    version='0.1.6',
    url='https://github.com/TakesxiSximada/scaff',
    download_url='https://github.com/TakesxiSximada/scaff',
    license='BSD',
    author='TakesxiSximada',
    author_email='takesxi.sximada@gmail.com',
    description="I'm sorry, I also I have made a scaffolding tool.",
    long_description="I'm sorry, I also I have made a scaffolding tool.",
    zip_safe=True,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Natural Language :: Japanese',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.4',
        ],
    platforms='any',
    packages=find_packages(),
    package_data=package_data,
    include_package_data=True,
    install_requires=install_requires,
    test_require=test_require,

    entry_points='''
    [console_scripts]
    scaff=scaff:main
    '''
    )
