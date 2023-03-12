from setuptools import setup, find_packages

setup(
    name="example_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    package_data={"example_package": ["data.json"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
