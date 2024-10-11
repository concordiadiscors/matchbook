import os
import re
from setuptools import setup, find_packages

def read(*parts):
    with open(os.path.join(os.path.dirname(__file__), *parts), 'r') as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name="matchbook",
    version=find_version("matchbook", "__init__.py"),
    author="Rory Cole",
    author_email="rory.cole1990@gmail.com",
    description="Matchbook API Python wrapper",
    url="https://github.com/rozzac90/matchbook",
    packages=find_packages(),
    install_requires=[
        "requests==2.32.3",
        "python-dateutil==2.9.0",
        "pytz==2024.2"
    ],
    long_description=open('README.md').read(),
    tests_require=['pytest'],
)