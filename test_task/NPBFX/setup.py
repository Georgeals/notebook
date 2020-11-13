from setuptools import setup

setup(
    name='depth_xml',
    version='0.1',
    py_modules=['depth'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        depth=depth:cli
    ''',
)
