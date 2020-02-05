from setuptools import setup, find_packages

setup(
        name='mypackage',
        version='0.1',
        packages=find_packages(exclude=['tests*']),
        license='MIT',
        description='EDSA example python package 2020',
        long_description=open('README.md').read(),
        install_requires=['numpy'],
        url='https://github.com/JonGerrand/mypackage.git',
        author='Zeus',
        author_email='zeus@explore-ai.net'
)
