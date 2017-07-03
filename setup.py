from distutils.core import setup
import setuptools


setup(
    name="tgclient",
    packages=["tgclient", "tgclient.utils"],
    version='0.2',
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
    download_url="https://github.com/negative23/tgclient/archive/0.2.tar.gz"
)
