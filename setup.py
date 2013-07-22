#!/usr/bin/env python
from distutils.core import setup

requires = [
    'pillow'
]

try:
    with open(os.path.join(here, 'README.md')) as f:
        README = f.read()
except:
    README = ''

setup (name = "PyCAPTCHA",
       version = "0.4.1",
       description = "A Python framework for CAPTCHA tests",
       maintainer = "Micah Dowty",
       maintainer_email = "micah@navi.cx",
       license = "MIT",
       install_requires=requires,
       packages = [
           'captcha',
           'captcha.visual',
       ],
       )
