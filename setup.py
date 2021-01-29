import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="turkish-twitter-preprocess",
    version="0.0.1",
    author="Emirhan Kaplan",
    author_email="emskaplann@gmail.com",
    description="A light-weight python package to pre-process Turkish Twitter Statuses(Tweets).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/emskaplann/turkish-twitter-preprocess",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)