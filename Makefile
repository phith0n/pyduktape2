unittest:
	python -m unittest

clean:
	python setup.py clean
	rm -rf pyduktape2.c build/ dist/ pyduktape2.egg-info/ .eggs/

package:
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/*