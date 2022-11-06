import setuptools
import subprocess
import os

remote_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

if "-" in remote_version:
    # when not on tag, git describe outputs: "1.3.3-22-gdf81228"
    # pip has gotten strict with version numbers
    # so change it to: "1.3.3+22.git.gdf81228"
    # See: https://peps.python.org/pep-0440/#local-version-segments
    v,i,s = remote_version.split("-")
    remote_version = v + "+" + i + ".git." + s

assert "-" not in remote_version
assert "." in remote_version

assert os.path.isfile("pydantic_custom_types/version.py")
with open("pydantic_custom_types/VERSION", "w", encoding="utf-8") as fh:
    fh.write("%s\n" % remote_version)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydantic-custom-types",
    version=remote_version,
    author="Per Lejon",
    author_email="per.lejon@netigate.se",
    description="Some custom pydantic types",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/netigate/pydantic-custom-types",
    packages=setuptools.find_packages(exclude=("tests",)),
    package_data={"cf_remote": ["VERSION"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: The MIT License (MIT)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    # install_requires=[],
)

