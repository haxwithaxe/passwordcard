from distutils.core import setup
import os
import subprocess


VERSION_FILE = 'VERSION'
NAME = 'passwordcard'
MODULES = [NAME]


def get_version():
    clean = ''
    if os.path.exists('.git'):
        clean_stdout = subprocess.check_output(['git', 'status', '--porcelain'], stderr=subprocess.DEVNULL)
        if len(clean_stdout.split()) > 0:
            clean = '-unclean'
        try:
            tags = subprocess.check_output(['git', 'describe', '--tags'], stderr=subprocess.DEVNULL)
            stdout, stderr = describe.interact()
            version = '%s%s' % (stdout.split('\n')[0].decode().strip(), clean)
        except (subprocess.CalledProcessError, IndexError):
            version = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'])
            version = '0.0-%s%s' % (version.decode().strip(), clean)
        with open(VERSION_FILE, 'w') as version_file:
            version += '\n'
            version_file.write(version)
    else:
        with open(VERSION_FILE, 'r') as version_file:
            version = version_file.readline().strip().decode()
    return version


setup(
	name=NAME,
	version=get_version(),
	packages=MODULES
	)
