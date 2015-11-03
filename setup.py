#!/usr/bin/env python

import os
from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='tornado-utils-3',
      version='0.1.0',
      description='Utility scripts for a Tornado site',
      long_description=read('README.md'),
      author='Peter Bengtsson, James Morris',
      author_email='mail@peterbe.com',
      url='http://github.com/rawtoast/tornado-utils',
      packages = [
        'tornado_utils',
        'tornado_utils.send_mail',
        'tornado_utils.send_mail.backends',
        'tornado_utils.tests',
      ],
      install_requires=[
          "tornado",
          "bcrypt",
      ],
      classifiers=[
           'Development Status :: 3 - Alpha',
           'Programming Language :: Python :: 3.5',
           'Intended Audience :: Developers',
           'Operating System :: POSIX :: Linux',
      ],
)
