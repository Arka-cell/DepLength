import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="depLength",
    version="0.0.6",
    author="Samir Ahmane",
    author_email="samirahmane.trading@gmail.com",
    description="A library to compute syntactic dependency length in English",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Arka-cell/DepLength",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)
