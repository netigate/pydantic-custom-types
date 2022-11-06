from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.0.1"
DESCRIPTION = "Custom type for pydantic"

setup(
    name="pydantic-custom-types",
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    author="Per Lejon",
    author_email="<per.lejon@netigate.se>",
    url="https://github.com/netigate/pydantic-custom-types",
    packages=find_packages(exclude="tests*"),
    # install_requires=[],
)

