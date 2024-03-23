import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):

    if browser =='ie':
        driver = webdriver.Ie()
        print('Launching Edge browser............')
    elif browser == 'firefox':
        driver=webdriver.Firefox()
        print('Launching Firefox browser............')
    else:
        driver=webdriver.Chrome()
        print('Launching Chrome browser............')
    return driver

def pytest_addoption(parser):  # This will get the value  from  CLI/Hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # This will return the browser value to setup method
    return request.config.getoption("--browser")

########### Html Report Generation Configuration###############

# def pytest_configure(config):
#     config.metadata['Project Name']='nop Commerce'
#     config.metadata['Module Name']='Login'
#     config.metadata['Tester']='Nagesh'
#
# # It is a hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME",None)
#     metadata.pop("Plugins",None)
