#pytest -v --driver Chrome --driver-path chromedriver.exe  test_page_object_auth.py

from pages.auth_page import AuthPage
import time

def test_auth_pages(selenium):
    page = AuthPage(selenium)
    page.enter_email("rasdvatri@mail.ru")
    page.enter_pass("test12345")
    page.btn_click()


    assert page.get_relative_link() == '/all_pets', "login error"

    time.sleep(5)