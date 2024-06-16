from setuptools import setup, find_packages

setup(
    name='opal_fetcher_graphql',  # Change this to match your package name
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'opal-common',
        'pydantic'
    ],
)
