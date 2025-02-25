import os

from setuptools import setup, find_packages

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md")) as f:
    long_description = f.read()

setup(
    name="boomslang-os",
    version="0.3",
    description="A simple UNIX like single core multitasking operating system simulator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Niraj Kamdar",
    packages=find_packages(),
    license="MIT",
    url="https://github.com/Niraj-Kamdar/OS",
    download_url="https://github.com/Niraj-Kamdar/OS/archive/master.zip",
    keywords=["boomslang", "os", "simulator"],
    classifiers=[
        "Development Status :: 4 - Beta",
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)