from cookiecutter import main
import os
import shutil


class TempCookiecutterProject(object):
    def __enter__(self):
        main.cookiecutter('.', no_input=True)

    def __exit__(self, exc_type, exc_val, exc_tb):
        shutil.rmtree(os.path.abspath('./pyawesome'))


def test_project():
    with TempCookiecutterProject():
        assert os.path.isdir(os.path.abspath('./pyawesome'))

