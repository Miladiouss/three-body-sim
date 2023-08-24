from setuptools import find_packages, setup

setup(
    name='repo-name',
    package_dir={'': 'py_src'},
    packages=find_packages(),
    version='0.0.1',
    description='''A simple three-body simulation in 1-D.''',
    author='Miladiouss',
    python_requires='>=3.8.5',
    install_requires=[
                    ],
)
