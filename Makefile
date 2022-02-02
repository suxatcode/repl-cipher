PYTHON ?= python
setup:
	python -m venv venv
	. ./venv/bin/activate && python -m pip install -r ./requirements.txt
test:
	. ./venv/bin/activate && python -m pytest .
.PHONY: setup test
