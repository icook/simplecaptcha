import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'pillow'
]

try:
    with open(os.path.join(here, 'README.md')) as f:
        README = f.read()
except:
    README = ''

setup (name = "simplecaptcha",
       version = "0.4-icook",
       description = "A Python framework for CAPTCHA tests",
       maintainer = "Micah Dowty",
       maintainer_email = "micah@navi.cx",
       license = "MIT",
       install_requires=requires,
       packages=find_packages(),
       )
