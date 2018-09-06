from cookiecutter import main
import os
import shutil


def is_dir(path):
    return os.path.isdir(os.path.abspath(path))


def is_file(path):
    return os.path.isfile(os.path.abspath(path))


def rm_dir(path):
    return shutil.rmtree(os.path.abspath(path))


class TempCookiecutterProject(object):
    def __enter__(self):
        main.cookiecutter('.', no_input=True)

    def __exit__(self, exc_type, exc_val, exc_tb):
        rm_dir('./pyawesome')


def test_project():
    with TempCookiecutterProject():
        assert is_dir('./pyawesome')

