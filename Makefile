#!make

##
## +--------------------------------------------------------+
## |   K-Testable Machine (KDFA)                            |
## +--------------------------------------------------------+
##
## USAGE
##	make TARGET [OPTIONS]
##
## TARGETS
##
##	install         Install dependencies.
## 	build           Build KDFA PyPI package.
## 	push            Upload KDFA PyPI package.
##	test            Run test suite.
##	clean           Clean environment.
##	demo            Run demo script (library).
##
## OPTIONS
##
##	CACHE=true      Speed-up build using cached files.
##	DEBUG=true      More verbose tests results. 

__dummy := $(shell touch ENV)
include ENV

.PHONY: clean
.DEFAULT_GOAL := help

SHELL = /bin/bash
D_PACKAGE = katestable

help:
	@sed -ne '/@sed/!s/##//p' $(MAKEFILE_LIST)

clean:
	@echo $@
	rm --force --recursive .tox/
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info
	rm --force --recursive .pytest_cache
	rm --force --recursive __pycache__

install: clean
	@echo $@
	pip uninstall ${D_PACKAGE} -y || true
	pip install $(if $(CACHE),,--no-cache-dir) -U pip
	pip install $(if $(CACHE),,--no-cache-dir) -U -r requirements.txt
	rm --force --recursive *.egg-info build
	pip uninstall ${D_PACKAGE} -y || true
	touch ENV

lint: clean
	@echo $@
	pdm run lint

test: clean
	@echo $@
	pdm run test

demo: clean
	@echo $@
	python katestable.py

build: clean
	@echo $@
	pdm run build

push:
	@echo $@
	python -m twine check dist/*
	python -m twine upload dist/*.whl
