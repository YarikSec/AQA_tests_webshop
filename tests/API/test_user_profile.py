import allure
from helpers.api_helpers import DemoWebShopAPI
from data.test_data import TestData


@allure.label("owner", "Yaroslav YAQA")
@allure.epic("DemoWebShop")
@allure.feature("Профиль пользователя")
class TestUserProfile:
    
    @allure.story("Получение данных профиля")
    @allure.title("Получение профиля пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
    Тест проверяет получение данных профиля авторизованного пользователя:
    1. Авторизуемся в системе
    2. Отправляем GET запрос на получение профиля
    3. Проверяем корректность полученных данных
    """)
    def test_get_user_profile(self):
        api = DemoWebShopAPI()
        
        with allure.step("Авторизуемся в системе"):
            api.login(
                email=TestData.TEST_USER["email"],
                password=TestData.TEST_USER["password"]
            )
        
        with allure.step("Получаем данные профиля"):
            response = api.get_profile()
            
            allure.attach(
                response.text,
                "profile_response.html",
                allure.attachment_type.HTML
            )
        
        with allure.step("Проверяем корректность данных"):
            assert response.status_code == 200
            # Проверяем наличие email в профиле
            assert TestData.TEST_USER["email"] in response.text
            # Проверяем наличие имени пользователя
            assert TestData.TEST_USER["first_name"] in response.text
            assert TestData.TEST_USER["last_name"] in response.text 