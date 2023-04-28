from setuptools import setup, find_packages
from pathlib import Path


install_requires = ["numpy"]


with open(Path(__file__).parent.joinpath("README.md")) as f:
    readme = f.read()

with open(Path(__file__).parent.joinpath("lazytensor", "VERSION"), "r") as f:
    ver = f.read().split("\n")[0]


setup(
    name='lazytensor',
    version=ver,
    packages=find_packages(),
    install_requires=install_requires,
    url='https://github.com/kushalkolar/lazytensor',
    license="Apache-Software-License",
    author='Kushal Kolar',
    author_email='',
    description='An interface for lazy evaluation of tensors in linear algebra routines',
    long_description=readme
)
