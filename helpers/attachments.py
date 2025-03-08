import json
import allure
from allure_commons.types import AttachmentType
from datetime import datetime


def add_screenshot(browser):
    """Добавляет скриншот страницы в отчет Allure."""
    png = browser.driver.get_screenshot_as_png()
    allure.attach(
        body=png,
        name=f'screenshot_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}',
        attachment_type=AttachmentType.PNG,
        extension='.png'
    )


def add_logs(browser):
    """Добавляет логи браузера в отчет Allure."""
    log = "\\n".join(f'{log["level"]}: {log["message"]}' 
                   for log in browser.driver.get_log(log_type='browser'))
    allure.attach(
        body=log,
        name='browser_logs',
        attachment_type=AttachmentType.TEXT,
        extension='.log'
    )


def add_html(browser):
    """Добавляет HTML страницы в отчет Allure."""
    html = browser.driver.page_source
    allure.attach(
        body=html,
        name='page_source',
        attachment_type=AttachmentType.HTML,
        extension='.html'
    )


def add_video(video_url):
    """Добавляет видео в отчет Allure."""
    allure.attach(
        '<html><body><video width="100%" height="100%" controls autoplay><source src="{}" type="video/mp4"></video></body></html>'.format(video_url),
        name='test_video',
        attachment_type=AttachmentType.HTML,
    )


def attach_all_artifacts(browser):
    """Добавляет все артефакты тестирования в отчет."""
    add_screenshot(browser)
    add_logs(browser)
    add_html(browser) 
    add_video(browser)