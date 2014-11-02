#! /usr/bin/env python
#-*- coding: utf-8 -*-
from setuptools import (
    setup,
    find_packages,
    )

def find_package_data(target, package_root):
    return [
        os.path.relpath(os.path.join(root, filename), package_root)
        for root, dirs, files in os.walk(target)
        for filename in files
        ]

install_requires = []
test_require = []
package = find_packages()
package_data = {}


setup(
    name='${package}',
    version='${version}',
    url='${web}',
    download_url='${download}',
    license='${license}',
    author='${name}',
    author_email='${email}',
    description="${description}",
    long_description="${description}",
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.4',
        ],
    platforms='any',
    package=package,
    package_data=package_data,
    include_package_data=True,
    install_requires=install_requires,
    test_require=test_require,
    entry_points='''
    [console_scripts]
    '''
    )
