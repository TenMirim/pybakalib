#! /usr/bin/env python3

"""
This file is part of Pybakalib.

Pybakalib is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Pybakalib is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Pybakalib.  If not, see <http://www.gnu.org/licenses/>.
"""

from distutils.core import setup

setup(name='pybakalib',
    version='0.1',
    description='Python Bakalari client',
    author='Vaclav Sraier',
    author_email='bakalari@vakabus.cz',
    url='https://www.python.org/sigs/distutils-sig/',
    packages=['pybakalib', 'pybakalib.modules']
)
