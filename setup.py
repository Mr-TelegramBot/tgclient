import setuptools
from setuptools import setup, find_packages


setup(
    name="tgclient",
    packages=find_packages(),
    version='0.3',
    description='Telegram Api Client',
    author='Negative',
    author_email='negative.officiall@gmail.com',
    url='https://github.com/negative23/telegram',
    install_requires=['six', 'requests'],
    keywords='telegram bot',
    license='GPL2',
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    download_url="https://github.com/negative23/tgclient/archive/0.3.tar.gz"
)
