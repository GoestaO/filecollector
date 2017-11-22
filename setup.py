from setuptools import setup

setup(
    name='collector',
    version='0.1',
    py_modules=['command_line'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        collector=command_line:collect
    ''',
)