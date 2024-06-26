from datetime import time


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени.
    """
    current_time = time(hour=23)
    # Переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)
    if 22 <= current_time.hour or current_time.hour < 6:
        is_dark_theme = True
    else:
        is_dark_theme = False

    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=16)
    is_dark_theme = None
    dark_theme_enabled_by_user = True
    if dark_theme_enabled_by_user is True:
        is_dark_theme = True
    elif dark_theme_enabled_by_user is False:
        is_dark_theme = False
    elif dark_theme_enabled_by_user is None:
        if current_time.hour >= 22 or current_time.hour < 6:
            is_dark_theme = True
        else:
            is_dark_theme = False

    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # Найдите пользователя с именем "Olga"
    suitable_user = None
    for user in users:
        if user["name"] == "Olga":
            suitable_user = user
            break

    assert suitable_user == {"name": "Olga", "age": 45}

    # Найдите всех пользователей младше 20 лет
    suitable_users = []
    for user in users:
        if user["age"] < 20:
            suitable_users.append(user)

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


def print_readable_function(func, *args):
    func_name = func.__name__.replace('_', ' ').title()
    args_str = ', '.join(str(arg) for arg in args)
    readable_output = f"{func_name} [{args_str}]"
    print(readable_output)
    return readable_output


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = print_readable_function(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = print_readable_function(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_readable_function(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
