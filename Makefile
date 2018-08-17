.PHONY: build clean

help:
	@echo "build		Build project with default settings"
	@echo "clean		Clean project"

build:
	cookiecutter --no-input --overwrite-if-exists .

clean:
	rm -R pyawesome

