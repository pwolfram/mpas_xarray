#!/usr/bin/env python

import os
from setuptools import setup

setup(name='mpas_xarray',
        version='0.0.3',
        description='Wrapper for xarray to interface with MPAS *.nc files',
        url='https://github.com/pwolfram/mpas_xarray/',
        maintainer='Phillip J. Wolfram',
        maintainer_email='phillipwolfram@gmail.com',
        license='BSD',
        keywords='mpas xarray wrapper',
        packages=['mpas_xarray'],
        install_requires=[open('requirements.txt').read().strip().split('\n')],
        long_description=(open('README.rst').read() if os.path.exists('README.rst') else ''),
        zip_safe=False)
