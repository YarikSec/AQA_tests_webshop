"""
Модуль содержит описания всех тест-кейсов проекта.
Каждый тест-кейс описан как словарь с подробной информацией.
"""

from dataclasses import dataclass
from typing import List, Optional, Dict, Union


@dataclass
class TestCase:
    id: str
    title: str
    description: str
    preconditions: List[str]
    steps: List[str]
    expected_result: str
    severity: str
    layer: str  # UI/API
    feature: str
    tags: List[str]
    automated: bool = True


# UI тест-кейсы для раздела Регистрации
registration_test_cases = {
    "test_successful_registration": TestCase(
        id="REG-001",
        title="Успешная регистрация нового пользователя",
        description="Проверка успешной регистрации пользователя с валидными данными",
        preconditions=[
            "Открыт браузер",
            "Пользователь находится на странице регистрации"
        ],
        steps=[
            "Заполнить поле Email валидным значением",
            "Заполнить поле Password",
            "Заполнить поле Confirm Password тем же значением",
            "Нажать кнопку Register"
        ],
        expected_result="Пользователь успешно зарегистрирован и авторизован в системе",
        severity="critical",
        layer="UI",
        feature="Registration",
        tags=["smoke", "registration", "positive"],
        automated=True
    ),
    
    "test_registration_with_existing_email": TestCase(
        id="REG-002",
        title="Регистрация с существующим email",
        description="Проверка невозможности регистрации с уже существующим email",
        preconditions=[
            "Открыт браузер",
            "В системе уже есть зарегистрированный пользователь",
            "Пользователь находится на странице регистрации"
        ],
        steps=[
            "Заполнить поле Email существующим значением",
            "Заполнить поле Password",
            "Заполнить поле Confirm Password",
            "Нажать кнопку Register"
        ],
        expected_result="Отображается сообщение об ошибке о существующем email",
        severity="critical",
        layer="UI",
        feature="Registration",
        tags=["registration", "negative"],
        automated=True
    )
}

# UI тест-кейсы для раздела Логина
login_test_cases = {
    "test_successful_login": TestCase(
        id="LOGIN-001",
        title="Успешный вход в систему",
        description="Проверка входа в систему с валидными учетными данными",
        preconditions=[
            "Открыт браузер",
            "Пользователь зарегистрирован в системе"
        ],
        steps=[
            "Перейти на страницу логина",
            "Ввести валидный email",
            "Ввести валидный пароль",
            "Нажать кнопку Login"
        ],
        expected_result="Пользователь успешно авторизован",
        severity="blocker",
        layer="UI",
        feature="Login",
        tags=["smoke", "login", "positive"],
        automated=True
    )
}

# API тест-кейсы
api_test_cases = {
    "test_get_user_profile": TestCase(
        id="API-001",
        title="Получение профиля пользователя",
        description="Проверка получения данных профиля авторизованного пользователя",
        preconditions=[
            "Пользователь авторизован",
            "Получен валидный токен авторизации"
        ],
        steps=[
            "Отправить GET запрос на эндпоинт /api/profile",
            "Проверить статус код ответа",
            "Проверить структуру ответа"
        ],
        expected_result="Получен корректный ответ с данными профиля пользователя",
        severity="critical",
        layer="API",
        feature="User Profile",
        tags=["api", "profile", "smoke"],
        automated=True
    )
}

# Корзина
cart_test_cases = {
    "test_add_item_to_cart": TestCase(
        id="CART-001",
        title="Добавление товара в корзину",
        description="Проверка добавления товара в корзину авторизованным пользователем",
        preconditions=[
            "Пользователь авторизован",
            "Открыта страница с товаром"
        ],
        steps=[
            "Нажать кнопку 'Add to cart'",
            "Перейти в корзину",
            "Проверить наличие добавленного товара"
        ],
        expected_result="Товар успешно добавлен в корзину",
        severity="critical",
        layer="UI",
        feature="Shopping Cart",
        tags=["cart", "smoke", "positive"],
        automated=True
    ),
    
    "test_view_cart": TestCase(
        id="CART-002",
        title="Просмотр содержимого корзины",
        description="Проверка отображения содержимого корзины авторизованного пользователя",
        preconditions=[
            "Пользователь авторизован",
            "В корзине есть товары"
        ],
        steps=[
            "Открыть страницу корзины",
            "Проверить загрузку страницы",
            "Проверить отображение товаров"
        ],
        expected_result="Страница корзины успешно загружена, товары отображаются корректно",
        severity="critical",
        layer="UI",
        feature="Shopping Cart",
        tags=["cart", "smoke", "positive"],
        automated=True
    ),
    
    "test_add_multiple_products": TestCase(
        id="CART-003",
        title="Добавление нескольких товаров в корзину",
        description="Проверка добавления нескольких разных товаров в корзину",
        preconditions=[
            "Пользователь авторизован",
            "Доступны разные товары для добавления"
        ],
        steps=[
            "Добавить первый товар в корзину",
            "Проверить успешность добавления",
            "Добавить второй товар в корзину",
            "Проверить успешность добавления",
            "Открыть корзину",
            "Проверить наличие всех добавленных товаров"
        ],
        expected_result="Все товары успешно добавлены в корзину и отображаются в ней",
        severity="normal",
        layer="UI",
        feature="Shopping Cart",
        tags=["cart", "positive"],
        automated=True
    )
}

# Словарь всех тест-кейсов по разделам
all_test_cases = {
    "Registration": registration_test_cases,
    "Login": login_test_cases,
    "API": api_test_cases,
    "Cart": cart_test_cases
}

# Получение статистики по покрытию тестами
def get_test_coverage_stats() -> Dict[str, Union[int, float]]:
    """
    Получение статистики по автоматизации тест-кейсов
    
    Метод подсчитывает:
    1. Общее количество тест-кейсов
    2. Количество автоматизированных тестов
    3. Процент покрытия автоматизацией
    
    Returns:
        Dict[str, Union[int, float]]: Словарь со статистикой, где:
            - total (int): общее количество тест-кейсов в проекте
            - automated (int): количество автоматизированных тест-кейсов
            - coverage_percentage (float): процент покрытия автоматизацией, 
              вычисляется как (automated / total) * 100
              
    Return Type:
        {
            "total": int,  # например: 10
            "automated": int,  # например: 8
            "coverage_percentage": float  # например: 80.0
        }
    
    # вывод статистики по покрытию тестами (пример использования)
    Example:
        >>> stats = get_test_coverage_stats()
        >>> print(f"Статистика по покрытию тестами:")
        >>> print(f"Всего тестов: {stats['total']}")  # Всего тестов: 10
        >>> print(f"Автоматизировано: {stats['automated']}")  # Автоматизировано: 8
        >>> print(f"Процент покрытия: {stats['coverage_percentage']}%")  # Процент покрытия: 80.0%
    """
    total_tests = 0
    automated_tests = 0
    
    for feature_tests in all_test_cases.values():
        for test in feature_tests.values():
            total_tests += 1
            if test.automated:
                automated_tests += 1
                
    return {
        "total": total_tests,
        "automated": automated_tests,
        "coverage_percentage": (automated_tests / total_tests) * 100
    }

def get_test_case_by_id(test_id: str) -> Optional[TestCase]:
    """
    Поиск тест-кейса по его ID
    
    Args:
        test_id: Уникальный идентификатор тест-кейса (например, 'REG-001', 'LOGIN-001')
    
    Returns:
        Optional[TestCase]: Найденный тест-кейс или None, если тест не найден
    """
    for feature_tests in all_test_cases.values():
        for test in feature_tests.values():
            if test.id == test_id:
                return test
    return None

def get_tests_by_tag(tag: str) -> List[TestCase]:
    """
    Получение всех тестов с определенным тегом
    
    Args:
        tag: Тег для поиска (например, 'smoke', 'positive', 'negative')
    
    Returns:
        List[TestCase]: Список тест-кейсов с указанным тегом
    """
    return [
        test for tests in all_test_cases.values() 
        for test in tests.values() 
        if tag in test.tags
    ]

def get_tests_by_layer(layer: str) -> List[TestCase]:
    """
    Получение всех тестов определенного слоя (UI/API)
    
    Args:
        layer: Слой тестирования ('UI' или 'API')
    
    Returns:
        List[TestCase]: Список тест-кейсов выбранного слоя
    """
    return [
        test for tests in all_test_cases.values() 
        for test in tests.values() 
        if test.layer == layer
    ]

def get_tests_by_feature(feature: str) -> List[TestCase]:
    """
    Получение всех тестов определенной функциональности
    
    Args:
        feature: Название функциональности (например, 'Login', 'Registration')
    
    Returns:
        List[TestCase]: Список тест-кейсов выбранной функциональности
    """
    return all_test_cases.get(feature, {}).values()

def get_tests_by_severity(severity: str) -> List[TestCase]:
    """
    Получение всех тестов определенной критичности
    
    Args:
        severity: Уровень критичности ('blocker', 'critical', etc.)
    
    Returns:
        List[TestCase]: Список тест-кейсов выбранной критичности
    """
    return [
        test for tests in all_test_cases.values() 
        for test in tests.values() 
        if test.severity == severity
    ]

def get_smoke_tests() -> List[TestCase]:
    """
    Получение всех smoke-тестов
    
    Returns:
        List[TestCase]: Список smoke тест-кейсов
    """
    return get_tests_by_tag("smoke")

def print_test_cases(tests: List[TestCase], title: str = "Тест-кейсы"):
    """
    Красивый вывод списка тест-кейсов
    
    Args:
        tests: Список тест-кейсов для вывода
        title: Заголовок для вывода
    """
    print(f"\n=== {title} ===")
    print(f"Всего тестов: {len(tests)}\n")
    for test in tests:
        print(f"ID: {test.id}")
        print(f"Название: {test.title}")
        print(f"Слой: {test.layer}")
        print(f"Критичность: {test.severity}")
        print(f"Теги: {', '.join(test.tags)}")
        print("-" * 50)

# Примеры использования:
if __name__ == "__main__":
    # Получение и вывод всех smoke-тестов
    smoke_tests = get_smoke_tests()
    print_test_cases(smoke_tests, "SMOKE-тесты")
    
    # Получение и вывод всех UI-тестов
    ui_tests = get_tests_by_layer("UI")
    print_test_cases(ui_tests, "UI-тесты")
    
    # Получение и вывод всех критичных тестов
    critical_tests = get_tests_by_severity("critical")
    print_test_cases(critical_tests, "Критичные тесты")
    
    # Получение и вывод всех тестов регистрации
    registration_tests = get_tests_by_feature("Registration")
    print_test_cases(list(registration_tests), "Тесты регистрации") 