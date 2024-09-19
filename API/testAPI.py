# from classAPI import Poisk
from API.classAPI import Poisk
from tokenURL import URL_Kinopoisk_API, token
import allure


poisk = Poisk(URL_Kinopoisk_API)
token = token


@allure.epic("kinopoisk")
@allure.severity(severity_level="ctitical")
@allure.title("Поиск актера, режиссера, оператора и т.п.")
@allure.description("Сделать поиск  ФИО актера, режиссера, оператора и т.п. на кирилице")
@allure.feature('Тест 3')
def test_search_kirilica():
    params = {'page': '1', 'limit': '3', 'query': 'Роберт Дауни мл.'}
    headers = {'X_API_KEY': token}
    kirilica = poisk.search_kirilica(headers=headers, params=params)
    with allure.step("Результат поиска не пустой"):
        assert kirilica is not None


@allure.epic("kinopoisk")
@allure.severity(severity_level="normal")
@allure.title("Поиск актера, режиссера, оператора и т.п.")
@allure.description("Сделать поиск  ФИО актера, режиссера, оператора и т.п. по id")
@allure.feature('Тест 3')
def test_search_by_id():
    params = {'id': '10096'}
    headers = {'X_API_KEY': token}
    by_id = poisk.search_by_id(headers=headers, params=params)
    with allure.step("Результат поиска не пустой"):
        assert by_id is not None


@allure.epic("kinopoisk")
@allure.severity(severity_level="ctitical")
@allure.title("Поиск актера, режиссера, оператора и т.п.")
@allure.description("Сделать поиск  ФИО актера, режиссера, оператора и т.п. на латинице")
@allure.feature('Тест 3')
def test_search_latinica():
    params = {'page': '1', 'limit': '3', 'query': 'Lee Kwang-Soo'}
    headers = {'X_API_KEY': token}
    latinica = poisk.search_latinica(headers=headers, params=params)
    with allure.step("Результат поиска не пустой"):
        assert latinica is not None


@allure.epic("kinopoisk")
@allure.severity(severity_level="normal")
@allure.title("Поиск актера, режиссера, оператора и т.п.")
@allure.description("Сделать поиск  ФИО актера, режиссера, оператора и т.п. по году рождения")
@allure.feature('Тест 3')
def test_search_by_year():
    params = {'page': '1', 'limit': '3', 'birthday': '01.01.1995-31.12.1995'}
    headers = {'X_API_KEY': token}
    by_year = poisk.search_by_year(headers=headers, params=params)
    with allure.step("Результат поиска не пустой"):
        assert by_year is not None


@allure.epic("kinopoisk")
@allure.severity(severity_level="normal")
@allure.title("Поиск актера, режиссера, оператора и т.п.")
@allure.description("Сделать поиск  ФИО актера, режиссера, оператора и т.п. по по гендеру(Женский, Мужской)")
@allure.feature('Тест 3')
def test_search_by_gender():
    params = {'page': '1', 'limit': '3', 'sex': 'Мужской'}
    headers = {'X_API_KEY': token}
    by_gender = poisk.search_by_gender(headers=headers, params=params)
    with allure.step("Результат поиска не пустой"):
        assert by_gender is not None

