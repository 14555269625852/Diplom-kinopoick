# from classAPI import Poisk
from API.classAPI import Poisk
from tokenURL import URL_Kinopoisk_API, token


poisk = Poisk(URL_Kinopoisk_API)
token = token


# test поиск  ФИО актера, режиссера, оператора и т.п. на кирилице
def test_search_kirilica():
    params = {'page': '1', 'limit': '3', 'query': 'Роберт Дауни мл.'}
    headers = {'X_API_KEY': token}
    kirilica = poisk.search_kirilica(headers=headers, params=params)
    assert kirilica is not None
    # assert kirilica["name"] == "Роберт Дауни мл."


# поиск актера, режиссера, оператора и т.п. по id
def test_search_by_id():
    params = {'id': '10096'}
    headers = {'X_API_KEY': token}
    by_id = poisk.search_by_id(headers=headers, params=params)
    assert by_id is not None
    # assert by_id["id"] == "10096"


# поиск  ФИО актера, режиссера, оператора и т.п. на латинице
def test_search_latinica():
    params = {'page': '1', 'limit': '3', 'query': 'Lee Kwang-Soo'}
    headers = {'X_API_KEY': token}
    latinica = poisk.search_latinica(headers=headers, params=params)
    assert latinica is not None
    # assert latinica["enName"] == "Kwang-Soo Lee"


# поиск актера, режиссера, оператора и т.п. по году рождения
def test_search_by_year():
    params = {'page': '1', 'limit': '3', 'birthday': '01.01.1995-31.12.1995'}
    headers = {'X_API_KEY': token}
    by_year = poisk.search_by_year(headers=headers, params=params)
    assert by_year is not None


# поиск актера, режиссера, оператора и т.п. по гендеру(Женский, Мужской)
def test_search_by_gender():
    params = {'page': '1', 'limit': '3', 'sex': 'Мужской'}
    headers = {'X_API_KEY': token}
    by_gender = poisk.search_by_gender(headers=headers, params=params)
    assert by_gender is not None
    # assert by_gender["sex"] == "Мужской"
