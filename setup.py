"""
Create unix package:    python setup.py sdist
Create windows package: python setup.py bdist_wininst
Create windows .exe:    python setup.py py2exe
"""

from distutils.core import setup
import os
import sys

## determine the version
# p = subprocess.Popen(['svn','info'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# revision = re.findall(r'Revision: (\d+)',p.communicate()[0])[0]
revision = '0.1'

params = {'author': 'Noah Hoffman',
          'author_email': 'ngh2@u.washington.edu',
          'description': 'Utilities for using unittest (Python standard library)',
          'name': 'unittools',
          'package_dir': {'unittools': '.'},
          'packages': ['unittools'],
          'scripts': ['runtests.py'],
          'url': 'http://faculty.washington.edu/ngh2',
          'version': revision}

setup(**params)

