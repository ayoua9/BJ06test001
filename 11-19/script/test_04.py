import pytest


class Test():
    def test01(self):
        print("test01被执行")

    def test02(self):
        print("test02被执行")
        assert 0
    # def hello(self):
    #     print("hello被执行")


if __name__ == '__main__':
    pytest.main("-s test_04.py")