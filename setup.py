from setuptools import setup, find_packages

setup(
    name='foo_parameterization',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        # dependencies
    ],
    entry_points='''
        [console_scripts]
        foo-cli=cli.main:main
    ''',
    extras_require={
        'dev': ['pytest', 'flake8'],
    }
)
