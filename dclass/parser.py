from selenium import webdriver
import time
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import subprocess

login = sys.argv[1]
password = sys.argv[2]

def main(login, password):
    if login=='' or password=='': 
        raise ValueError('')
    if type(login) == str and type(password) == str:


        options = webdriver.ChromeOptions()

        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--headless") #Для скрытого включения хром
        driver = webdriver.Chrome(
            executable_path = "C:/Python310/chromedriver-win32/chromedriver.exe",
            options=options
        )

        try:
            driver.get("https://edu.tatar.ru/login/")
            login_input = driver.find_element(By.NAME, "main_login2")  # поиск элемента по индексу и имени индекса
            login_input.clear()  # Очистка поля ввода логина
            login_input.send_keys(login)  # ввод логина

            password_input = driver.find_element(By.NAME, "main_password2")
            password_input.clear()
            password_input.send_keys(password)

            password_input.send_keys(Keys.ENTER)

            time.sleep(3)
            i = 0
            if driver.current_url=='https://edu.tatar.ru/message': #проверка на пароль и логин
                raise ValueError ('У одного из пользователей неправильный пароль')
            driver.find_element(By.LINK_TEXT, "Мой дневник").click()
            time.sleep(3)
        
            elements = driver.find_elements(By.CLASS_NAME, 'tt-mark') #Берём оценки тут список
            elements_text = [element.text for element in elements]

            massiv = list(filter(bool, elements_text))
            if massiv != []:
                subprocess.run(["python3", "dcoin.py",  massiv) #проверка на пустой список
                return massiv #возвращаем их
            else:
                return [0]
        


        except Exception as ex:
            print(ex)
            
        finally:

            driver.quit()
            
    else:
        raise ValueError ('Нужно передавать строки')
    
if __name__ == '__main__':
    main()
