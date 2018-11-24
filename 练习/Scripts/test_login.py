from 练习.Base.get_driver import get_driver
from 练习.Page.page_login import PageLogin


class TestLogin():
    def setup_class(self):
        self.login=PageLogin(get_driver())
    def teardown_class(self):
        self.login.driver.quit()
    def test_login(self):
        pass