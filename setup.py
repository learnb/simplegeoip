import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simplegeoip",
    version="0.0.1",
    author="Bryan Learn",
    author_email="learn.bryan@gmail.com",
    description="Uses geoip2 package to read coordinates from a MaxMind GeoLite2 database.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/learnb/simplegeoip",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
