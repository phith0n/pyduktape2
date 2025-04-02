from os import path
from setuptools import setup, find_packages, Extension
from codecs import open
from Cython.Build import cythonize
from Cython.Distutils import build_ext

readme_path = path.join(path.abspath(path.dirname(__file__)), 'README.rst')
with open(readme_path, encoding='utf-8') as readme:
    long_description = readme.read()

ext_modules = cythonize(
    [
        Extension(
            'pyduktape2',
            ['pyduktape2.pyx'],
            include_dirs=['vendor'],
        )
    ],
    compiler_directives={
        'language_level': 3,
    }
)

setup(
    name='pyduktape2',
    version='0.5.0',
    author='Stefano Dissegna',
    description='Python integration for the Duktape Javascript interpreter',
    long_description=long_description,
    url='https://github.com/phith0n/pyduktape2',
    license='GPL-2.0-only',
    keywords='javascript duktape embed',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Cython',
        'Programming Language :: Python :: 3',
        'Programming Language :: JavaScript',
        'Topic :: Software Development :: Interpreters',
    ],
    packages=find_packages(exclude=['tests']),
    setup_requires=['setuptools>=18.0', 'Cython>=3'],
    test_suite='tests',
    ext_modules=ext_modules,
    cmdclass={'build_ext': build_ext},
    include_package_data=True,
    zip_safe=False
)
