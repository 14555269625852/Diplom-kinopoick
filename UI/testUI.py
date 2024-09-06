from selenium import webdriver
from UI.classUI import poisk_glavnay


# test поиск  фильма, сериала и т.п. на кирилице
def test_poick_kirilica():
    driver = webdriver.Firefox()
    kirilica = poisk_glavnay(driver)
    kirilica.poisk_kirilica()
    kirilica.click_lupa()
    assert kirilica is not None
    kirilica._driver.quit()


# поиск фильма, сериала и т.п. на латинице
def test_poick_latinica():
    driver = webdriver.Firefox()
    latinica = poisk_glavnay(driver)
    latinica.poisk_latinica()
    latinica.click_lupa()
    assert latinica is not None
    latinica._driver.quit()


# поиск фильма, сериала и т.п. по году выпуска
def test_poick_by_year_move():
    driver = webdriver.Firefox()
    year = poisk_glavnay(driver)
    year.racshiren_poisk()
    year.vvod_year_racshiren_poisk_move()
    year.click_search()
    assert year is not None
    year._driver.quit()


# поиск актера, режиссера, оператора и т.п. по году рождения
def test_poick_by_year_action():
    driver = webdriver.Firefox()
    year = poisk_glavnay(driver)
    year.racshiren_poisk()
    year.vvod_year_racshiren_poisk_action()
    year.click_search()
    assert year is not None
    year._driver.quit()


# поиск актера, режиссера, оператора и т.п. по месту рождения
def test_poick_by_janr():
    driver = webdriver.Firefox()
    year = poisk_glavnay(driver)
    year.racshiren_poisk()
    year.vvod_mesto_rojdenia_racshiren_poisk()
    year.click_search()
    assert year is not None
    year._driver.quit()
