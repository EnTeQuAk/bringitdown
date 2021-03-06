from __future__ import unicode_literals
import codecs
import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


test_requires = [
    'py>=1.4.20',
    'pyflakes>=0.7.3',
    'pytest>=2.5.2',
    'pytest-cache>=1.0',
    'pytest-cov>=1.6',
    'pytest-flakes==0.2',
    'pytest-pep8==1.0.5',
    'pytest-django==2.6',
    'cov-core==1.7',
    'coverage==3.7.1',
    'mock==1.0.1',
    'pep8==1.4.6',
]


install_requires = [
    'Django>=1.7',
    'ansible',
    'fabric',
    'boto',
    'paramiko',
]


dev_requires = [
    'tox',
]


docs_requires = [
    'sphinx',
    'sphinx_rtd_theme'
]


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='bringitdown',
    version='0.1.0',
    description='Bring down your infrastructure. Effectively, immediately, monitored and controllable.',
    long_description=read('README.rst') + read('CHANGES.rst'),
    author='Christopher Grebs',
    author_email='cg@webshox.org',
    url='https://github.com/EnTeQuAk/bringitdown/',
    extras_require={
        'docs': docs_requires,
        'tests': test_requires,
        'dev': dev_requires,
    },
    tests_require=test_requires,
    install_requires=install_requires,
    cmdclass={'test': PyTest},
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Testing :: Traffic Generation',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
    ],
    zip_safe=False,
)
