from __future__ import division, absolute_import, print_function

import os
import sys
import subprocess

from setuptools import setup, find_packages

from setuptools.command.install import install as _install

# Allow execution of node.js dependencies (e.g. gulp).
# You will still need to have node in your PATH.
os.environ['PATH'] = './node_modules/.bin' + os.pathsep + os.environ['PATH']


class install(_install):
    def run(self):
        subprocess.check_call(['npm', 'install'], shell=(sys.platform == 'win32'))
        _install.run(self)


setup(
    cmdclass={
        'install': install,
    },
    name='win_max_path_error',
    version='0.0.1',
    description='pip install fails to remove temporary files on Windows due to max_path limits',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
