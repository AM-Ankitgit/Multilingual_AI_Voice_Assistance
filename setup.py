from setuptools import find_packages,setup


HYPEN_DOT = '-e .'
with  open ("requirements.txt") as f:
    dependencies = f.readlines()
    if HYPEN_DOT in dependencies:
        dependencies.remove(HYPEN_DOT)


setup(
    name='Multilingual AI Assistance',
    version="0.0.0",
    packages=find_packages(),
    author="Ankit Mahalle",
    install_requires = dependencies
)