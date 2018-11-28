import os

from setuptools import setup

requires = [
    ]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',  # includes virtualenv
    'pytest-cov',
    ]

setup(name='git-bv',
      version='0.0',
      description='Manage many BrainVISA projects with git',
      long_description='',
      classifiers=[
          "Programming Language :: Python",
      ],
      author='',
      author_email='',
      url='',
      keywords='brainvisa git',
      scripts=['git-bv'],
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'testing': tests_require,
      },
      install_requires=requires,
      )
