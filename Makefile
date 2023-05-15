all:
	python setup.py build_ext --inplace

clean:
	rm -rf *.out *.so *.pyc test build

cibuildwheel-linux:
	python -m cibuildwheel --platform linux

cibuildwheel-macos:
	python -m cibuildwheel --platform macos
