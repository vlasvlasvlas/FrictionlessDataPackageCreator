from setuptools import setup, find_packages

setup(
    name='frictionless_data_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'frictionless',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'create-package=src.create_packages:main',
        ],
    },
)