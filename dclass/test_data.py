import datetime
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tkinter import * 

def main():
    today = datetime.datetime.now().strftime("%d") # берём свою дату
#C:\Python310\chromedriver_win32\chromedriver.exe

    options = webdriver.ChromeOptions()

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--headless")
    driver = webdriver.Chrome(
    #executable_path="chromedriver.exe",
        options=options
    )

    try:
        driver.get("https://edu.tatar.ru/login/")
        login_input = driver.find_element(By.NAME, "main_login2")  # поиск элемента по индексу и имени индекса
        login_input.clear()  # Очистка поля ввода логина
        login_input.send_keys("509025576")  # ввод логина

        password_input = driver.find_element(By.NAME, "main_password2")
        password_input.clear()
        password_input.send_keys("7SHU")

        password_input.send_keys(Keys.ENTER)
        #login = driver.find_element(By.PARTIAL_LINK_TEXT, "Приключения").click()
        time.sleep(3)
        i = 0
        driver.find_element(By.LINK_TEXT, "Мой дневник").click()
        time.sleep(3)
        x = driver.find_elements(By.CLASS_NAME, "tt-days")
        spisok_date = [j.text for j in x]
        if not today in spisok_date:
            driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/a[2]").click()
            list_of_lesson = int(today) + 1
            x = driver.find_elements(By.CLASS_NAME, "tt-days")
            spisok_date = [j.text for j in x]
            number_of_column = spisok_date.index(str(list_of_lesson))
        else:
            number_of_column = spisok_date.index(today)
        #тут сложные расчёты для вывода опрёделённого дня
        end_range = number_of_column * 8 + 1
        start_range = end_range - 8    
    
        elements = driver.find_elements(By.CLASS_NAME, 'tt-mark') #Берём оценки
        elements_text = [element.text for element in elements]
        first_eight_elements=[] 
        for i in range(start_range, end_range):
            first_eight_elements.append(elements_text[i])
        massiv = list(filter(bool, first_eight_elements))
        return massiv #возвращаем их


    except Exception as ex:
        print(ex)
    finally:
        driver.quit()
if __name__ == '__main__':
    main()
