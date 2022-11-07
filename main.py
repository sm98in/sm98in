import select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def first_test():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options, executable_path=r'C:/Users/.../.../chromedriver.exe')
    driver.get("https://testsheepnz.github.io/BasicCalculator.html/")

    # Проскроллить вниз до конца
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Поиск элементов и присваивание к переменных.
    # Лучше искать элементы через xpath, так как не всегда есть id.
    input_first_number = driver.find_element("id", "number1Field")
    input_second_number = driver.find_element("id", "number2Field")
    input_calculate_button = driver.find_element("id", "calculateButton")
    answer = driver.find_element("id", "numberAnswerField")

    # Действия с формами

    Select(driver.find_element("id", "SelectBuild"))
    select.select_by_visible_text("Prototype")
    input_first_number.send_keys("2")
    input_second_number.send_keys("3")
    Select(driver.find_element("id", "SelectOperationDropdown"))
    select.select_by_visible_text("Subtrack")
    input_calculate_button.send_keys(Keys.RETURN)

    if answer.text == "-1":
        print("Все работает")
    else:
        print("Ошибка")
