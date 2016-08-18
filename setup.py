from distutils.core import setup

from passwordcard import __version__

NAME = 'passwordcard'
MODULES = [NAME]

setup(
	name=NAME,
	version=__version__,
	packages=MODULES
	)
