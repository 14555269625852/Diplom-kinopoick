from selenium.webdriver.common.by import By
from tokenURL import url_glavnay_kino
import allure


class poisk_glavnay():

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(url_glavnay_kino)

    @allure.step("Сделать поиск на кирилице")
    def poisk_kirilica(self):
        self._driver.find_element(By.TAG_NAME, 'input').send_keys("сумерки")

    @allure.step("Нажать на лупу")
    def click_lupa(self):
        self._driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/div[2]/div[2]/div[1]/form[1]/div[1]/div[1]/button[1]/*[name()='svg'][1]").click()

    @allure.step("Сделать поиск на латинице")
    def poisk_latinica(self):
        self._driver.find_element(By.TAG_NAME, 'input').send_keys("Twilight")

    @allure.step("Нажать на расширенный поиск")
    def racshiren_poisk(self):
        self._driver.find_element(By.CSS_SELECTOR, ".styles_advancedSearch__uwvnd").click()

    @allure.step("Сделать поиск по году создание фильма")
    def vvod_year_racshiren_poisk_move(self):
        self._driver.find_element(By.ID, "year").send_keys("1997")

    @allure.step("Нажать на поиск")
    def click_search(self):
        self._driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[4]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/form[1]/input[11]").click()

    @allure.step("Сделать поиск по году рождения актера")
    def vvod_year_racshiren_poisk_action(self):
        self._driver.find_element(By.ID, "birthday").send_keys("1995")

    @allure.step("Сделать поиск по месту ррждения актера")
    def vvod_mesto_rojdenia_racshiren_poisk(self):
        self._driver.find_element(By.ID, "location").send_keys("Сеул")
