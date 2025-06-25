import pytest
import allure
from selenium import webdriver

@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        browser = webdriver.Chrome()
        browser.implicitly_wait(4)
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()

@pytest.fixture
def api_client() → BoardApi:
    DataProvider().get_token()
    return BoardApi(
        ConfigProvider().get("api", "base_url"),
        DataProvider().get_token()
    )