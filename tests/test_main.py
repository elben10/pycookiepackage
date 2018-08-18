# The testfile is inspired by pypackage
# See https://github.com/audreyr/cookiecutter-pypackage

from cookiecutter.main import cookiecutter
from shutil import rmtree

import os
import shlex
import subprocess


class within_dir(object):
    def __init__(self, path):
        self.new_path = path
        self.old_path = os.getcwd()

    def __enter__(self):
        os.chdir(self.new_path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.old_path)


class TempCookiecutterProject(object):
    def __init__(self, template=None):
        if template:
            self.template = os.path.abspath(template)
        else:
            self.template = os.path.abspath(".")

    def __enter__(self):
        cookiecutter(self.template, no_input=True)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        rmtree("pyawesome")


def check_call_within_dir(cmd, path):
    with within_dir(path):
        return subprocess.check_call(shlex.split(cmd))


def check_output_within_dir(cmd, path):
    with within_dir(path):
        return subprocess.check_output(shlex.split(cmd))


def test_temp_project_works():
    with TempCookiecutterProject():
        assert os.path.isdir('pyawesome')
        assert os.path.isdir('pyawesome/pyawesome')
        assert os.path.isfile('pyawesome/pyawesome/__init__.py')

