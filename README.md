
### Description
Simple Python package to demonstrate pypa/pip/#2892 :bug:


Doing pip install on Windows for a package that creates a
deep hierarchy of directories (e.g. by using npm install
internally) fails to remove its temporary build directory
`pip-*-build` because of the path length limitations imposed
by Windows. This leaves the package "half installed".

### Requirements
* Windows 7
* Python 2.7.9
* pip 7.0.3
* virtualenv 13.0.3
* setuptools 17.0
* nodejs/npm >=0.12.4

### How to reproduce

Running `pip install .` on a Windows machine should fail.
Do this in a virtual environment to keep the system clean.

