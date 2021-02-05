import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="turkish-twitter-preprocess",
    version="0.0.7",
    author="Emirhan Kaplan",
    author_email="emskaplann@gmail.com",
    description="a light-weight python package to pre-process turkish twitter statuses(tweets).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/emskaplann/turkish-twitter-preprocess",
    packages=setuptools.find_packages(),
    keywords='turkish twitter preprocess',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)

#  new version publishing
#  $ python3 setup.py sdist bdist_wheel
#  $ python3 -m twine upload dist/*