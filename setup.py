from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

VERSION = "0.1.2"
DESCRIPTION = "A package for retrieving transcripts from youtube"

setup(
    name="youtube_transcript_downloader",
    version=VERSION,
    author="Edvinas Adomaitis",
    author_email="edvinasad7@gmail.com",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/t4skmanag3r/youtube_transcript_downloader",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.8.5",
)
