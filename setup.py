import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "nvpy",
    version = "0.1",
    author = "Charl P. Botha",
    author_email = "cpbotha@vxlabs.com",
    description = "A cross-platform simplenote-syncing note-taking app inspired by nvALT.",
    license = "BSD",
    keywords = "simplenote note-taking tkinter nvalt markdown",
    url = "http://vxlabs.com/software/nvpy",
    packages=['nvpy'],
    long_description=read('README.md'),
    install_requires = ['Markdown'],
    entry_points = {
        'gui_scripts' : ['nvpy = nvpy.nvpy:main']
    },
    package_data = {
        # http://peak.telecommunity.com/DevCenter/setuptools#including-data-files
        # documentation implies path is relative to package key.
        'nvpy' : ['icons/nvpy.ico', 'icons/nvpy.gif']
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: X11 Applications",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)

