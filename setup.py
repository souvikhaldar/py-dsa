import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-dsa", 
    version="0.0.1",
    author="Souvik Haldar",
    author_email="souvikhaldar32@gmail.com",
    description="All abstract data types and algorithms implemented in Python 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/souvikhaldar/py-dsa",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)