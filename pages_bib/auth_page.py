from pages_bib.base import WebPage
from pages_bib.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'http://petfriends1.herokuapp.com/login'
        super().__init__(web_driver, url)

    email = WebElement(id='email')

    password = WebElement(id='pass')

    btn = WebElement(class_name='btn.btn-success')
