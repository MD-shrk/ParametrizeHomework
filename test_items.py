import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_purchase_button(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    a = browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert len(a) > 0, "Кнопка не найдена"

