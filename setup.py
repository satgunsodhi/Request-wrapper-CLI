from setuptools import setup, find_packages

setup(
    name="requester",
    version="1.0",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "requester = requester.cli:main",
        ],
    },
    author="Satgun Sodhi",
    author_email="satgunsodhi@gmail.com",
    description="A simple Python package for requests with CLI",
    url="https://github.com/satgunsodhi/Request-wrapper-CLI",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
