import pytest


class Test06:
    @pytest.mark.run(order=4)
    def test_delete(self):
        print("删除成功")

    @pytest.mark.run(order=3)
    def test_get(self):
        print("查询成功")

    @pytest.mark.run(order=2)
    def test_put(self):
        print("修改成功")

    @pytest.mark.run(order=1)
    def test_post(self):
        print("新增成功")

