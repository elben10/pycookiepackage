.PHONY: build clean clean-build clean-default-project clean-pyc clean-test doc \
doc-browser install test test-all
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

build: ## Build project with default settings
	cookiecutter --no-input --overwrite-if-exists .

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -fr {} +
	find . -name '*.pyo' -exec rm -fr {} +
	find . -name '*~' -exec rm -fr {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -fr .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

clean-default-project:
	rm -fr pyawesome

doc: ## Generate Sphinx HTML documentation, including API docs
	$(MAKE) -C doc clean
	$(MAKE) -C doc html

doc-browser: doc ## Open sphinx generated documentation
	$(BROWSER) doc/_build/html/index.html

install: clean ## Install package
	python setup.py install

test: install ## Run tests from default python
	pytest

test-all: install ## Run tests using tox on specified python dists
	tox


