# tests.py

import unittest

from functions.get_files_info import run_python_file


class TestFunctions(unittest.TestCase):
    """
    def test_get_files_info(self):
        print(get_files_info("calculator", "."))
        print(get_files_info("calculator", "pkg"))
        print(get_files_info("calculator", "/bin"))
        print(get_files_info("calculator", "../"))

    def test_get_file_content(self):
        print(get_file_content("calculator", "main.py"))
        print(get_file_content("calculator", "pkg/calculator.py"))
        print(get_file_content("calculator", "/bin/cat"))


    def test_write_file(self):
        print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
        print(
            write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        )
        print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

    """

    def test_run_python_file(self):
        # error test: outside working directory
        print(run_python_file("calculator", "../main.py"))
        # error test: not exists
        print(run_python_file("calculator", "nonexistent.py"))
        # error test: not py file
        print(run_python_file("calculator", "lorem.txt"))
        # positive tests
        print(run_python_file("calculator", "main.py"))
        print(run_python_file("calculator", "tests.py"))


if __name__ == "__main__":
    unittest.main()
