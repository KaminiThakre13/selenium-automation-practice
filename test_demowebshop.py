from POM.register import Register
from POM.login import Login

def test_reg(_drivers):         ## _drivers --> driver
    reg_obj = Register(_drivers)
    reg_obj.click_on_register()
    reg_obj.select_gender()
    reg_obj.enter_firstname()
    reg_obj.enter_lastname()
    reg_obj.enter_email()
    reg_obj.set_password()
    reg_obj.set_password()
    reg_obj.confirm_password()


def test_login(_drivers):       ## _drivers --> driver
    login_obj = Login(_drivers)
    login_obj.click_on_login()
    login_obj.enter_login_email()
    login_obj.click_on_password()