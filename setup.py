#! /usr/bin/env python
#
# Copyright (C) 2018-2022 Dmytro Samchuk

DESCRIPTION = "CharSplit - An *ngram*-based compound splitter for German"
LONG_DESCRIPTION = """\
Splits a German compound into its body and head, e.g.
> Autobahnraststätte -> Autobahn - Raststätte
Implementation of the method decribed in the appendix of the thesis:
Tuggener, Don (2016). *Incremental Coreference Resolution for German.* University of Zurich, Faculty of Arts.
**TL;DR**: The method calculates probabilities of ngrams occurring at the beginning, end and in the middle of words and identifies the most likely position for a split.
The method achieves ~95% accuracy for head detection on the [Germanet compound test set](http://www.sfs.uni-tuebingen.de/lsd/compounds.shtml).
A model is provided, trained on 10 Mio German nouns from newspaper text.
"""
DISTNAME = 'charsplit'
MAINTAINER = 'Dmytro Samchuk'
MAINTAINER_EMAIL = 'dvsamchuk@gmail.com'
URL = 'https://github.com/Codealist/CharSplit'
LICENSE = 'GNU GPL-3.0'
DOWNLOAD_URL = 'https://github.com/Codealist/CharSplit/releases'
VERSION = '1.3.5.1'

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup


if __name__ == "__main__":

    setup(name=DISTNAME,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        license=LICENSE,
        url=URL,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        install_requires=[],
        packages=['charsplit', 'charsplit.pretrained'],
        classifiers=[
                     'Intended Audience :: Science/Research',
                     'Programming Language :: Python :: 3.4',
                     'Programming Language :: Python :: 3.5',
                     'Programming Language :: Python :: 3.6',
                     'License :: OSI Approved :: {}'.format(LICENSE),
                     'Topic :: Scientific/Engineering :: Natural language processing',
                     'Operating System :: POSIX',
                     'Operating System :: Unix',
                     'Operating System :: MacOS'])
