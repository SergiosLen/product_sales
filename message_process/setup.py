try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='JPMorgan_test',
    version='0.1',
    description='Load messages from a txt file and process sales notification messages.',
    author='Sergios Lenis',
    author_email='sergioslenis@gmail.com',
    license='MIT',
    packages=['JPMorgan_test'],
    include_package_data=True,
    scripts=['bin/JPMorgan_test'],
    install_requires=[ 'message_process' ],
        )