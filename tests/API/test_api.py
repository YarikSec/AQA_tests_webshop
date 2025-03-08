import requests
import allure
import pytest
from helpers.api_helpers import DemoWebShopAPI
from data.test_data import TestData


@allure.label("owner", "Yaroslav YAQA")
@allure.epic("DemoWebShop")
@allure.feature("API Авторизация")
class TestAuth:
    
    @allure.story("Регистрация")
    @allure.title("Успешная регистрация нового пользователя")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("""
    Тест проверяет успешную регистрацию нового пользователя:
    1. Отправляем POST запрос с данными пользователя
    2. Проверяем успешность регистрации
    3. Проверяем отсутствие ошибки о существующем email
    """)
    def test_successful_registration(self):
        api = DemoWebShopAPI()
        
        with allure.step("Регистрируем нового пользователя"):
            response = api.register(
                email=TestData.TEST_USER["email"],
                password=TestData.TEST_USER["password"],
                first_name=TestData.TEST_USER["first_name"],
                last_name=TestData.TEST_USER["last_name"]
            )
            
            allure.attach(
                response.text,
                "response.html",
                allure.attachment_type.HTML
            )
        
        with allure.step("Проверяем успешность регистрации"):
            assert response.status_code == 200
            assert "The specified email already exists" not in response.text
    
    @allure.story("Регистрация")
    @allure.title("Регистрация с существующим email")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
    Тест проверяет невозможность регистрации с уже существующим email:
    1. Регистрируем первого пользователя
    2. Пытаемся зарегистрировать второго пользователя с тем же email
    3. Проверяем наличие сообщения об ошибке
    """)
    def test_registration_with_existing_email(self):
        api = DemoWebShopAPI()
        
        # Сначала регистрируем пользователя
        with allure.step("Регистрируем первого пользователя"):
            first_response = api.register(
                email=TestData.TEST_USER["email"],
                password=TestData.TEST_USER["password"],
                first_name=TestData.TEST_USER["first_name"],
                last_name=TestData.TEST_USER["last_name"]
            )
            
            allure.attach(
                first_response.text,
                "first_registration_response.html",
                allure.attachment_type.HTML
            )
        
        # Пытаемся зарегистрировать второго пользователя с тем же email
        with allure.step("Пытаемся зарегистрировать пользователя с существующим email"):
            second_response = api.register(
                email=TestData.TEST_USER["email"],  # Тот же email
                password="DifferentPassword123",
                first_name="Another",
                last_name="User"
            )
            
            allure.attach(
                second_response.text,
                "second_registration_response.html",
                allure.attachment_type.HTML
            )
        
        with allure.step("Проверяем наличие сообщения об ошибке"):
            assert "The specified email already exists" in second_response.text
    
    @allure.story("Вход")
    @allure.title("Успешный вход в систему")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("""
    Тест проверяет успешный вход в систему:
    1. Отправляем POST запрос с учетными данными
    2. Проверяем успешность входа
    3. Проверяем наличие токена авторизации
    """)
    def test_successful_login(self):
        api = DemoWebShopAPI()
        
        with allure.step("Выполняем вход в систему"):
            response = api.login(
                email=TestData.TEST_USER["email"],
                password=TestData.TEST_USER["password"]
            )
            
            allure.attach(
                response.text,
                "response.html",
                allure.attachment_type.HTML
            )
        
        with allure.step("Проверяем успешность входа"):
            assert response.status_code == 200
        
        with allure.step("Проверяем наличие токена авторизации"):
            token = api.get_auth_token()
            assert token is not None
            allure.attach(
                str(token),
                "auth_token.txt",
                allure.attachment_type.TEXT
            )

@allure.epic("DemoWebShop")
@allure.feature("Корзина")
class TestCart:
    
    @allure.story("Работа с корзиной")
    @allure.title("Добавление товара в корзину")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_to_cart(self):
        api = DemoWebShopAPI()
        
        with allure.step("Авторизуемся в системе"):
            api.login(
                email=TestData.TEST_USER["email"],
                password=TestData.TEST_USER["password"]
            )
        
        with allure.step("Добавляем товар в корзину"):
            product = TestData.PRODUCTS["simple_computer"]
            response = api.add_to_cart(product_id=product["id"], quantity=1)
            
            allure.attach(
                response.text,
                "response.html",
                allure.attachment_type.HTML
            )
        
        with allure.step("Проверяем успешность добавления"):
            assert response.status_code == 200
            assert "The product has been added" in response.text
    
    @allure.story("Работа с корзиной")
    @allure.title("Просмотр содержимого корзины")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_view_cart(self):
        api = DemoWebShopAPI()
        
        with allure.step("Авторизуемся в системе"):
            api.login(
                email=TestData.TEST_USER["email"],
                password=TestData.TEST_USER["password"]
            )
        
        with allure.step("Получаем содержимое корзины"):
            response = api.get_cart()
            
            allure.attach(
                response.text,
                "cart_content.html",
                allure.attachment_type.HTML
            )
        
        with allure.step("Проверяем успешность получения корзины"):
            assert response.status_code == 200
            # Проверяем, что страница корзины загрузилась
            assert "Shopping cart" in response.text
    
    @allure.story("Работа с корзиной")
    @allure.title("Добавление нескольких товаров в корзину")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_multiple_products(self):
        api = DemoWebShopAPI()
        
        with allure.step("Авторизуемся в системе"):
            api.login(
                email=TestData.TEST_USER["email"],
                password=TestData.TEST_USER["password"]
            )
        
        products = [
            (TestData.PRODUCTS["simple_computer"], 1),
            (TestData.PRODUCTS["laptop"], 2)
        ]
        
        for product, quantity in products:
            with allure.step(f"Добавляем товар {product['name']} в количестве {quantity}"):
                response = api.add_to_cart(product_id=product["id"], quantity=quantity)
                
                allure.attach(
                    response.text,
                    f"add_{product['name']}_response.html",
                    allure.attachment_type.HTML
                )
                
                assert response.status_code == 200
                assert "The product has been added" in response.text
        
        with allure.step("Проверяем содержимое корзины"):
            cart_response = api.get_cart()
            assert cart_response.status_code == 200
            # Проверяем наличие товаров в корзине
            for product, _ in products:
                assert product["name"] in cart_response.text
