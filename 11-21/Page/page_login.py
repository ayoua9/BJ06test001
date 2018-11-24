from Base.base import Base


class PageLogin(Base):
    """
    page页面思路：
    1.一个页面一个对象（新建一个Class）
    2. 对象页面内需要操作的步骤，每一个步骤单独封装一个方法
    """
    def page_input_username(self,text):
        self.base_input(loc_username,text)
    def page_input_password(self,text):
        self.page_input_password()