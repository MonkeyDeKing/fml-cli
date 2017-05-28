from setuptools import setup
setup(
    name = 'fml-cli',
    version = '0.0.0',
    packages = ['fml-cli'],
    entry_points = {
        'console_scripts': [
            'fml = fml-cli.__main__:main'
        ]
    })