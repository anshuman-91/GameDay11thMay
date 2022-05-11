from setuptools import setup, find_packages

setup(
    name='Reformat',
    version='1.0',
    packages=find_packages(include=('job*',)),
    description='Reformat',
    install_requires=[
        'pyhocon==0.3.59'
    ],
    entry_points={
        'console_scripts': [
            'main = job.pipeline:main',
        ],
    },
    tests_require=['pytest', 'pytest-html']
)
