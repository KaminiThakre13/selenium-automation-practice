import xlrd

path = r'C:\pythonSelenium\POM-framework\data_\demowebshop_locators.xlsx'
workbook = xlrd.open_workbook(path)                     ## book object

## register
reg_worksheet = workbook.sheet_by_name("register")      ## sheet object
reg_rows = reg_worksheet.get_rows()                     ## generator object
reg_header = next(reg_rows)


def reg_data():
    reg_dict = {}
    for ele in reg_rows:
        reg_dict[ele[0].value] = (ele[1].value, ele[2].value)

    return reg_dict

##########################################################################
## Login

login_worksheet = workbook.sheet_by_name("login")           ## sheet object
login_rows = login_worksheet.get_rows()                     ## generator object
login_header = next(login_rows)


def login_data():
    login_dict = {}
    for ele in login_rows:
        login_dict[ele[0].value] = (ele[1].value, ele[2].value)

    return login_dict