from setuptools import find_packages, setup

setup(
    name='URLShortener',
    version='0.1',
    author="Christopher Dickson",
    author_email="chris.dickson1994@gmail.com",
    url="https://github.com/ChrisDickson/URLShortener",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask', 'Flask-MySQL'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
