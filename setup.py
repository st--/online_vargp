from setuptools import find_packages, setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, "README.rst")) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, "README.rst"), encoding="utf-8") as f:
        long_description = f.read()

setup(
    name="volatilitygp",
    version="0.0.1",
    description=("Repo for SVGPs"),
    long_description=long_description,
    author="",
    author_email="",
    url="",
    license="MPL-2.0",
    packages=find_packages(exclude=["notebooks", "experiments", "tests"]),
    install_requires=[],
    include_package_data=True,
    classifiers=[
        "Development Status :: 0",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.7",
    ],
)
