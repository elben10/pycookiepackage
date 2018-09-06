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


class ChangeDir(object):
    def __init__(self, path):
        self.old_path = os.getcwd()
        self.new_path = path

    def __enter__(self):
        os.chdir(self.new_path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.old_path)


def test_project():
    with TempCookiecutterProject():
        assert is_dir('./pyawesome')
        assert is_file('./pyawesome/setup.py')
        assert is_dir('./pyawesome/pyawesome')
        assert is_file('./pyawesome/pyawesome/__init__.py')


def test_changed_dir_correctly():
    new_path = os.path.join(os.getcwd(), 'tests')
    old_path = os.getcwd()
    with ChangeDir('./tests'):
        assert os.getcwd() == new_path
    assert old_path == os.getcwd()




