from selenium import webdriver
from UI.classUI import poisk_glavnay
import allure


@allure.epic("kinopoisk")
@allure.severity(severity_level="ctitical")
@allure.title("Поиск актера, режиссера, оператора и т.п.")
@allure.description("Сделать поиск  ФИО актера, режиссера, оператора и т.п. на кирилице")
@allure.feature('Тест 4')
def test_poick_kirilica():
    with allure.step("Открыть браузер"):
        driver = webdriver.Firefox()
        kirilica = poisk_glavnay(driver)
    with allure.step("Сделать поиск на кирилице"):
        kirilica.poisk_kirilica()
    with allure.step("Нажать на лупу"):
        kirilica.click_lupa()
    with allure.step("Результат поиска не пустой"):
        assert kirilica is not None
    with allure.step("Закрыть браузер"):
        kirilica._driver.quit()

@allure.epic("kinopoisk")
@allure.severity(severity_level="ctitical")
@allure.title("Поиск актера, режиссера, оператора и т.п.")
@allure.description("Сделать поиск  ФИО актера, режиссера, оператора и т.п. на латинице")
@allure.feature('Тест 4')
def test_poick_latinica():
    with allure.step("Открыть браузер"):
        driver = webdriver.Firefox()
        latinica = poisk_glavnay(driver)
    with allure.step("Сделать поиск на латинце"):
        latinica.poisk_latinica()
    with allure.step("Нажать на лупу"):
        latinica.click_lupa()
    with allure.step("Результат поиска не пустой"):
        assert latinica is not None
    with allure.step("Закрыть браузер"):
        latinica._driver.quit()


@allure.epic("kinopoisk")
@allure.severity(severity_level="normal")
@allure.title("Поиск  фильма, сериала и т.п. по году выпуска")
@allure.description("Сделать поиск  фильма, сериала и т.п. по году выпуска")
@allure.feature('Тест 4')
def test_poick_by_year_move():
    with allure.step("Открыть браузер"):
        driver = webdriver.Firefox()
        year = poisk_glavnay(driver)
    with allure.step("Нажать на расширеный поиск"):
        year.racshiren_poisk()
    with allure.step("Ввести год создание фильма"):
        year.vvod_year_racshiren_poisk_move()
    with allure.step("Нажать на поиск"):
        year.click_search()
    with allure.step("Результат поиска не пустой"):
        assert year is not None
    with allure.step("Закрыть браузер"):
        year._driver.quit()

@allure.epic("kinopoisk")
@allure.severity(severity_level="normal")
@allure.title("Поиск актера, режиссера, оператора и т.п. по году рождения")
@allure.description("Сделать поиск актера, режиссера, оператора и т.п. по году рождения")
@allure.feature('Тест 4')
def test_poick_by_year_action():
    with allure.step("Открыть браузер"):
        driver = webdriver.Firefox()
        year = poisk_glavnay(driver)
    with allure.step("Нажать на расширеный поиск"):
        year.racshiren_poisk()
    with allure.step("Ввести год рождения актера"):
        year.vvod_year_racshiren_poisk_action()
    with allure.step("Нажать на поиск"):
        year.click_search()
    with allure.step("Результат поиска не пустой"):
        assert year is not None
    with allure.step("Закрыть браузер"):
        year._driver.quit()

@allure.epic("kinopoisk")
@allure.severity(severity_level="normal")
@allure.title("Поиск актера, режиссера, оператора и т.п. по месту рождения")
@allure.description("Сделать поиск актера, режиссера, оператора и т.п. по месту рождения")
@allure.feature('Тест 4')
def test_poick_by_janr():
    with allure.step("Открыть браузер"):
        driver = webdriver.Firefox()
        year = poisk_glavnay(driver)
    with allure.step("Нажать на расширеный поиск"):
        year.racshiren_poisk()
    with allure.step("Ввести место рождения актера"):
        year.vvod_mesto_rojdenia_racshiren_poisk()
    with allure.step("Нажать на поиск"):
        year.click_search()
    with allure.step("Результат поиска не пустой"):
        assert year is not None
    with allure.step("Закрыть браузер"):
        year._driver.quit()
