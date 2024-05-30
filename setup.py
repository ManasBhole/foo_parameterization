from setuptools import setup, find_packages

setup(
    name='foo_parameterization',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'calculate_volume=foo.volume:calculate_volume',
        ],
    },
)
