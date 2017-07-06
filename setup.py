import setuptools
from setuptools import setup, find_packages


setup(
    name="tgclient",
    packages=find_packages(),
    version='1.3.3',
    description='Telegram Api Client',
    author='Negative',
    author_email='negative.officiall@gmail.com',
    url='https://github.com/negative23/tgclient',
    install_requires=['six', 'requests'],
    keywords='telegram bot api',
    license='GPL2',
    classifiers=[
        'Programming Language :: Python :: 3'
    ]
)
