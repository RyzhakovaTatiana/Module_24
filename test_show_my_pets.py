#pytest -v --driver Chrome --driver-path chromedriver.exe  test_show_my_pets.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest



@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('./chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends1.herokuapp.com/login')

    yield

    pytest.driver.quit()

def my_list(l1, l2, l3):
    for i in l1:
        for j in l2:
            for z in l3:
                yield [i, j, z]
                break

def test_show_my_pets():
# Вводим email
    pytest.driver.find_element_by_id('email').send_keys('rasdvatri@mail.ru')
# Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('test12345')
# Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
# Проверяем, что мы оказались на главной странице пользователя
    pytest.driver.implicitly_wait(10)


    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
    pytest.driver.find_element_by_css_selector('button.navbar-toggler').click()
    pytest.driver.find_element_by_link_text("Мои питомцы").click()



#Задание 1 Присутствуют все питомцы/По заданию нужно добавить явное ожидание



    #Находим количество питомцев в статистике
    number_of_pets = pytest.driver.find_element_by_xpath('//*[h2][1]').text.split()
    assert int(number_of_pets[2]) == 5


    #Считаем количество карточек питомцев в таблице
    #pet_card = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]//tbody/tr')
    pet_card = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]//tbody/tr')))

    my_pet = []
    for i in range(len(pet_card)):
        if pet_card[i].text != '':
            my_pet.append(i)
        return my_pet

    assert int(len(my_pet)) == int(number_of_pets[2])

#Задание 2 Хотя бы у половины питомцев есть фото/По заданию нужно добавить неявное ожидание
    number_of_pets = pytest.driver.find_element_by_xpath('//*[h2][1]').text.split()
    number_of_pets = int(number_of_pets[2])
    images = pytest.driver.find_elements_by_tag_name('img')
    pet_photo = []
    for i in range(number_of_pets):
        if images[i].get_attribute('src') !='':
            pet_photo.append(i)
        return pet_photo
    assert pet_photo == 4
    assert int(pet_photo) > int(number_of_pets[2]) / 2


#Задание 3 У всех питомцев есть имя, возраст и порода. По заданию нужно добавить неявное ожидание

def test_show_name_breed_age():
# Вводим email
    pytest.driver.find_element_by_id('email').send_keys('rasdvatri@mail.ru')
# Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('test12345')
# Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
# Проверяем, что мы оказались на главной странице пользователя
    pytest.driver.implicitly_wait(10)


    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
    pytest.driver.find_element_by_css_selector('button.navbar-toggler').click()
    pytest.driver.find_element_by_link_text("Мои питомцы").click()

    pytest.driver.implicitly_wait(10)


    names = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]//tbody/tr/td[1]')
    breed = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]//tbody/tr/td[2]')
    age = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]//tbody/tr/td[3]')

    for i in range(len(names)):
        assert names[i].text != ''
        assert breed[i].text != ''
        assert age[i].text != ''

#Задание 4  У всех питомцев разные имена
    names_of_pets = []
    for i in range(len(names)):
        names_of_pets.append(i)
    #Проверяем уникальные элементы или нет. Если элементы не уникальны, то в массиве будет меньше элементов
    assert len(list(names_of_pets)) == len(set(names_of_pets))


#Задание 5  В списке нет повторяющихся питомцев
    l_names = []
    for i in range(len(names)):
        l_names.append(i)
    return l_names

    l_breeds = []
    for j in range(len(breed)):
        l_breeds.append(j)
    return l_breeds

    l_ages = []
    for z in range(len(age)):
        l_ages.append(z)
    return l_ages
    #Обратимся к фукции my_list, чтобы объединить 3 разных списка по индексам в 3 другие списка, чтобы для каждого питомца
#сформировать список имя, порода, возраст
    values_of_pets = list(my_list(l_names, l_breeds, l_ages))
    print(values_of_pets)
#А теперь сравним количество элементов в списке с количеством элементов в сете
    assert len(list(values_of_pets)) == len(set(values_of_pets))




































