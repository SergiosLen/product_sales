try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='message_process',
    version='0.1',
    description='Load messages from a txt file and process sales notification messages.',
    author='Sergios Lenis',
    author_email='sergioslenis@gmail.com',
    license='MIT',
    packages=['message_process'],
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=['nose'],
    scripts=['bin/message_process'],
    install_requires=[ 'message_process' ],
        )