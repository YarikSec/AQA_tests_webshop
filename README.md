# Автоматизация тестирования DemoWebShop

![Test & Report](https://github.com/YarikSec/AQA_tests_webshop/actions/workflows/tests.yml/badge.svg)

Проект по автоматизации тестирования для [DemoWebShop](https://demowebshop.tricentis.com) с использованием Python, Pytest и Allure.

## 🛠 Стек технологий

- Python
- Pytest - фреймворк для тестирования
- Requests - для работы с HTTP-запросами
- Allure - для генерации отчетов
- Selene - для UI тестов
- Selenium - для работы с веб-браузером

## 📁 Структура проекта

```
├── tests/                      # Тесты
│   ├── API/                    # API тесты
│   │   ├── test_api.py        # Основные API тесты (авторизация, корзина)
│   │   └── test_user_profile.py # Тесты профиля пользователя
│   └── UI/                     # UI тесты (будут добавлены позже)
├── pages/                      # Page Objects
├── helpers/                    # Вспомогательные модули
│   ├── api_helpers.py         # Методы для работы с API
│   └── attachments.py         # Helpers для Allure вложений
├── data/                      # Тестовые данные
│   ├── test_data.py          # Константы и тестовые данные
│   └── test_cases.py         # Описания тест-кейсов
└── conftest.py               # Конфигурация Pytest
```

## 📝 Описание тест-кейсов

В проекте реализованы автотесты для следующих функциональностей:

### 🔐 Авторизация
- Успешная регистрация нового пользователя
- Проверка регистрации с существующим email
- Успешная авторизация

### 👤 Профиль пользователя
- Получение данных профиля

### 🛒 Корзина
- Добавление товара в корзину
- Просмотр содержимого корзины
- Добавление нескольких товаров

## 🚀 Запуск тестов

### Предварительные требования

1. Установить Python 3.9 или выше
2. Установить зависимости:
```bash
pip install -r requirements.txt
```

### Запуск тестов

Запуск всех тестов:
```bash
pytest
```

Запуск только API тестов:
```bash
pytest tests/API/
```

Запуск с генерацией Allure отчета:
```bash
pytest --alluredir=allure-results
```

### Просмотр отчета

Для просмотра Allure отчета:
```bash
allure serve allure-results
```

## 📊 Статистика покрытия

Для просмотра текущей статистики по автоматизации:
```bash
python -c "from data.test_cases import get_test_coverage_stats; print(get_test_coverage_stats())"
```

## 🔍 Управление тест-кейсами

В проекте реализованы следующие функции для работы с тест-кейсами:

- `get_smoke_tests()` - получение smoke-тестов
- `get_tests_by_layer()` - фильтрация по слою (UI/API)
- `get_tests_by_feature()` - фильтрация по функциональности
- `get_tests_by_severity()` - фильтрация по критичности
- `get_tests_by_tag()` - фильтрация по тегам

## 🔄 CI/CD

Проект настроен на автоматический запуск тестов и генерацию отчетов при каждом пуше в main ветку или создании pull request:

- ✅ Автоматический запуск всех тестов
- 📊 Генерация Allure отчета
- 📱 Публикация отчета на GitHub Pages
- 🔄 Хранение истории прогонов

Отчет доступен по адресу: https://YarikSec.github.io/AQA_tests_webshop

## 👤 Автор

**Yaroslav YAQA**
- Email: [yarik.wade@gmail.com]
- GitHub: [@YarikSec]
