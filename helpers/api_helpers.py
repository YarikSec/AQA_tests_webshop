import requests
import allure
from typing import Optional, Dict, Any


class DemoWebShopAPI:
    def __init__(self):
        self.base_url = "https://demowebshop.tricentis.com"
        self.session = requests.Session()
    
    @allure.step("Выполняем вход через API")
    def login(self, email: str, password: str) -> requests.Response:
        data = {
            "Email": email,
            "Password": password,
            "RememberMe": "true"  # Добавим это для сохранения сессии
        }
        response = self.session.post(
            f"{self.base_url}/login",
            data=data,
            allow_redirects=True  # Убедимся, что следуем за редиректами
        )
        
        # Добавим отладочную информацию
        allure.attach(
            response.text,
            'response.html',
            allure.attachment_type.HTML
        )
        return response
    
    @allure.step("Регистрация нового пользователя")
    def register(self, email: str, password: str, 
                first_name: str, last_name: str, gender: str = "M") -> requests.Response:
        return self.session.post(
            f"{self.base_url}/register",
            data={
                "Gender": gender,
                "FirstName": first_name,
                "LastName": last_name,
                "Email": email,
                "Password": password,
                "ConfirmPassword": password
            }
        )
    
    @allure.step("Получение токена авторизации")
    def get_auth_token(self) -> Optional[str]:
        # Добавим отладочную информацию
        all_cookies = self.session.cookies.get_dict()
        allure.attach(
            str(all_cookies),
            'cookies.txt',
            allure.attachment_type.TEXT
        )
        # Проверяем разные варианты имени куки
        return (self.session.cookies.get("NOPCOMMERCE.AUTH") or 
                self.session.cookies.get(".NOPCOMMERCE.AUTH") or
                self.session.cookies.get("Authentication"))
    
    @allure.step("Добавление товара в корзину")
    def add_to_cart(self, product_id: int, quantity: int = 1) -> requests.Response:
        return self.session.post(
            f"{self.base_url}/addproducttocart/catalog/{product_id}/1",
            data={
                "quantity": quantity
            }
        )
    
    @allure.step("Получение содержимого корзины")
    def get_cart(self) -> requests.Response:
        return self.session.get(f"{self.base_url}/cart")
    
    @allure.step("Получение информации о пользователе")
    def get_customer_info(self) -> requests.Response:
        return self.session.get(f"{self.base_url}/customer/info")
    
    @allure.step("Оформление заказа")
    def checkout(self, order_data: Dict[str, Any]) -> requests.Response:
        return self.session.post(
            f"{self.base_url}/checkout",
            data=order_data
        )
    
    @allure.step("Получение списка товаров по категории")
    def get_category_products(self, category: str) -> requests.Response:
        return self.session.get(f"{self.base_url}/{category}")
    
    @allure.step("Поиск товаров")
    def search_products(self, query: str) -> requests.Response:
        return self.session.get(
            f"{self.base_url}/search",
            params={"q": query}
        )
    
    @allure.step("Получение списка заказов")
    def get_orders(self) -> requests.Response:
        return self.session.get(f"{self.base_url}/order/history")
    
    @allure.step("Добавление товара в список желаний")
    def add_to_wishlist(self, product_id: int) -> requests.Response:
        return self.session.post(
            f"{self.base_url}/addproducttocart/details/{product_id}/2"
        )
    
    @allure.step("Получение списка желаний")
    def get_wishlist(self) -> requests.Response:
        return self.session.get(f"{self.base_url}/wishlist")
    
    @allure.step("Подписка на рассылку")
    def subscribe_newsletter(self, email: str) -> requests.Response:
        return self.session.post(
            f"{self.base_url}/subscribenewsletter",
            data={"email": email}
        )
    
    def get_profile(self) -> requests.Response:
        """
        Получение данных профиля пользователя
        
        Returns:
            requests.Response: Ответ от сервера с данными профиля
        """
        return self.session.get(
            url=f"{self.base_url}/customer/info",
            headers=self._get_headers()
        ) 