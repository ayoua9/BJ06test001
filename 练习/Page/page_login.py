from selenium.webdriver.common.by import By

from 练习.Base.base import Base

loc_usa = (By.ID, "com.vcooline.aike:id/etxt_username")
loc_pwd = By.ID, "com.vcooline.aike:id/etxt_pwd"
loc_login_btn = By.ID, "com.vcooline.aike:id/btn_login"

class PageLogin(Base):


    # 输入用户名
    def page_input_username(self,loc,text):
        self.base_input(loc_usa,text)
    # 输入密码
    def page_input_password(self,text):
        self.base_input(loc_pwd, text)
    # 点击登录
    def page_click_login_btn(self):
        self.base_click(loc_login_btn)