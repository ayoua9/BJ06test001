import pytest


class Test01():
    def setup_class(self):
        print("执行setup_class")
    def teardown_class(self):
        print("执行teardown_class")

    def setup(self):
        print("执行setup")
    def teardown(self):
        print("执行teardown")

    def test001(self):
        print("执行test001")

    def test002(self):
        print("执行test002")

if __name__ == '__main__':
    pytest.main("-s test_05.py")





"""
addopts= -s
testpaths= ./
python_files= test*.py
python_classes= Test
python_functions= 

"""