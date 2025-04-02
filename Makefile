.PHONY: build

unittest:
	python -m unittest

pytest:
	python -m pytest

clean:
	python setup.py clean
	rm -rf pyduktape2.c build/ dist/ pyduktape2.egg-info/ .eggs/ *.so pyduktape2.html cython_debug .pytest_cache

build:
	python setup.py build_ext --inplace

package:
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/*