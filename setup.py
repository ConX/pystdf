#!/usr/bin/env python

from distutils.core import setup

setup(name='pystdf',
    version='1.0.0',
    description="""
Python module for working with STDF files
PySTDF is a Python module that makes it easy to work with STDF (Teradyne's Standard Test Data Format). STDF is a commonly used file format in semiconductor test -- automated test equipment (ATE) from such vendors as Teradyne, Verigy, LTX, Credence, and others support this format.

PySTDF provides event-based stream parsing of STDF version 4, along with indexers that can help you rearrange the data into a more useful tabular form, as well as generate missing summary records or new types of derivative records.

The parser architecture is very flexible and can easily be extended to support STDF version 3 as well as custom record types.

Potential applications of PySTDF include:
* Debugging a vendor's STDF implementation
* Straight conversion to ASCII-readable form
* Repairing STDF files
* Developing an application that leverages STDF
  - Conversion to tabular form for statistical analysis tools
  - Loading data into a relational database

PySTDF is released under a GPL license. Applications developed with PySTDF can only be released with a GPL-compatible license. Commercial applications can purchase an alternate license agreement for closed-source distribution.
""",
    author='Casey Marshall',
    author_email='casey.marshall@gmail.com',
    url='http://code.google.com/p/pystdf/',
    package_dir={'pystdf':'src'},
    packages=['pystdf'],
    scripts=['scripts/stdf_slice', 'scripts/rec_index', 'scripts/stdf2atdf'],
)
