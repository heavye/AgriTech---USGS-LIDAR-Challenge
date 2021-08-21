#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['pandas>=1.1.0', 'numpy>=1.19.0', 'sklearn',
                'seaborn', 'matplotlib', 'pdal', 'plotly']

test_requirements = ['pytest>=3', ]

setup(
    author="Euel Fantaye",
    email="euelfantaye@gmail.com",
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="to fetch, visualise, and transform publicly available satellite and LIDAR data. A code that interface with USGS 3DEP and fetch data using their API. 
",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='LIDAR, Pdal, Geopandas,',
    name='USGS-LIDAR',
    packages=find_packages(include=['scripts', 'scripts.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/heavye/AgriTech---USGS-LIDAR-Challenge',
    version='0.1.0',
    zip_safe=False,
)