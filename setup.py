from setuptools import setup, find_packages

setup(
    name="infomentor",
    version="1.0.1",
    url="https://github.com/NisseDILLIGAF/infomentor.git",
    author="Matthias Bilger",
    author_email="nisse@dilligaf.nu",
    description="forked from Matthias Bilger grab infomentor news and push or mail them",
    packages=find_packages(),
    entry_points = {
        'console_scripts': [
            'infomentor=infomentor.__main__:main',
        ],
    },
    install_requires=[
        #"pycrypto",
        "requests",
        #"sqlalchemy",
        #"dateparser",
        #"python-pushover",
        #"flask",
        #"flask-bootstrap",
        #"caldav",
        #"bs4",
        #"icalendar",
    ],
)
