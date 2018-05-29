from setuptools import find_packages
from setuptools import setup

setup(
    name='pre-commit-sql-formatter',
    version='1.0.0',

    author='Alex Silva',

    platforms='linux',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages('.'),
    install_requires=[
        'sqlparse',
    ],
    entry_points={
        'console_scripts': [
            'sql_formatter = pre_commit_hooks.sql_formatter:main',
        ],
    },
)
