
from os import path
from setuptools import setup


setup(
    name="hazm",
    version="0.7.1",
    description="Python library for digesting Persian text.",
    author="Alireza Nourian",
    author_email="az.nourian@gmail.com",
    url="https://www.roshan-ai.ir/hazm/",
    long_description=open(
        path.join(path.abspath(path.dirname(__file__)), "README.md"), encoding="utf-8"
    ).read(),
    long_description_content_type="text/markdown",
    packages=["hazm"],
    package_data={"hazm": ["data/*.dat"]},
    classifiers=[
        "Topic :: Text Processing",
        "Natural Language :: Persian",        
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=["nltk==3.8.1", 'libwapiti>=0.2.1;platform_system!="Windows"'],
    extras_require={"wapiti": ["libwapiti>=0.2.1"]},
)
