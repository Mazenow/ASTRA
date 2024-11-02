from behave import step
from selenium import webdriver
from time import sleep
import yaml

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@step('Открываем "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)
    context.driver.maximize_window()


@step('Вводим в поле "Учётная запись или адрес эл. почты" текст "{login}"')
def step_impl(context, login):
    with open("config.yaml") as config_file:
        config = yaml.safe_load(config_file)
    context.login = config['login']
    xpath_login = "//*[@data-login-form-input-user]"
    login_pitch = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_login)),
                                                          message='Строка ввода логина отсутствует, либо не работает xpath_login')
    login_pitch.send_keys(context.login)
    sleep(1)


@step('Вводим в поле "Пароль" текст "{password}"')
def step_impl(context, password):
    with open("config.yaml") as config_file:
        config = yaml.safe_load(config_file)
        context.password = config['password']
    xpath_password = "//*[@data-login-form-input-password]"
    password_pitch = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_password)),
                                                             message='Строка ввода логина отсутствует, либо не работает xpath_password')
    password_pitch.send_keys(config['password'])
    sleep(1)


@step('Нажимаем кнопку "{button_name}"')
def step_impl(context, button_name):
    xpath_button = f"//*[text() = '{button_name}']"
    button = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_button)),
                                                     message=f'Кнопка "{button_name}" отсутствует, либо не работает xpath_button')
    actions = ActionChains(context.driver)
    actions.move_to_element(button)
    actions.click()
    actions.perform()
    sleep(2)


@step("Загружаем тестовый файлы")
def step_impl(context):
    test_files = {'bmp': "C:\\Users\\Uncle_Faster\\Desktop\\ASTRA\\test_bmp.bmp",
                  'text': "C:\\Users\\Uncle_Faster\\Desktop\\ASTRA\\test_txt.txt"}
    xpath_load = "//input[@type='file']"
    for key, value in test_files.items():
        file_input = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_load)),
                                                             message='Отсутствует возможность загрузки файлов')
        file_input.send_keys(value)
        sleep(2)


@step('Создаем новую папку с названием "Новая папка"')
def step_impl(context):
    xpath_button = "//*[@aria-label = 'Создать папку']"
    button = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_button)),
                                                     message='Кнопка загрузки "Новой папки" отсутствует, либо не работает xpath_button')
    actions = ActionChains(context.driver)
    actions.move_to_element(button)
    actions.click()
    actions.perform()
    sleep(2)


@step("Выбираем все файлы к удалению")
def step_impl(context):
    xpath_button = "//*[@for = 'select_all_files']"
    button = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_button)),
                                                     message='Кнопка выбора всех файлов к удалению отсутствует, либо не работает xpath_button')
    actions = ActionChains(context.driver)
    actions.move_to_element(button)
    actions.click()
    actions.perform()
    sleep(2)


@step('Появляется окно "подтверждения действий при удалении"')
def step_impl(context):
    xpath_del_window = "//*[@class = 'oc-dialog']//*[contains(text(), 'Удалить')]"
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_del_window)),
                                            message='Окно "подтверждения действий при удалении" отсутствует, либо не работает xpath_del_window')
    xpath_yes = "//*[@class = 'oc-dialog']//*[text() = 'Да']"
    button = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_yes)),
                                                     message='Кнопка "Да" отсутствует, либо не работает xpath_yes')
    actions = ActionChains(context.driver)
    actions.move_to_element(button)
    actions.click()
    actions.perform()
    sleep(1)
    context.driver.quit()
