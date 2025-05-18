import pytest
import allure
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from helpers.attachments import attach_all_artifacts


@pytest.fixture(scope="function", autouse=True)
def allure_report():
    try:
        allure.attach.file("allure-results/latest-report.json", 
                          name="Отчет о тестировании",
                          attachment_type=allure.attachment_type.JSON)
    except FileNotFoundError:
        pass  # Игнорируем ошибку, если файл не найден

@pytest.fixture(scope="function", autouse=True)
def browser_management():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 10
    browser.config.base_url = 'https://demowebshop.tricentis.com'
    
    options = Options()
    options.add_argument('--headless')  # опционально для запуска в фоновом режиме (проверить на разных браузерах)
    # Тут можно добавить другие опции для браузера
    browser.config.driver_options = options
    
    browser.open('')
    
    yield
    
    attach_all_artifacts(browser) # добавляю в отчет allure все артефакты

    browser.quit()