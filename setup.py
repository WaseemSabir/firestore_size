from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="firestore_size",
    version="1.0.1",
    author="Waseem Sabir",
    author_email="waseemsabir99@gmail.com",
    description="A small package to calculate the approximate size of a firestore document",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WaseemSabir/firestore_size",
    packages=find_packages(include=['firestore_size']),
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
