from selenium import webdriver
from time import sleep


url = 'https://www.instagram.com/'

login = input("Your login: ")
password = input("Your password: ")
hashtag = "#" + input("Enter a word for hashtag (without the symbol of hashtag): ")


def login_page():
    login_link = browser.find_element_by_name('username')
    login_link.click()
    login_link.send_keys(login)  # Login

    password_link = browser.find_element_by_name('password')
    password_link.click()
    password_link.send_keys(password)  # Password

    click_button = browser.find_element_by_css_selector("button[type='submit']")
    click_button.click()


def not_now_window():
    sleep(2)

    not_now_button = browser.find_element_by_class_name("HoLwm")
    not_now_button.click()


def dont_save_window():
    sleep(2)

    not_now_button = browser.find_element_by_class_name("yWX7d")
    not_now_button.click()


def search_by_hashtag():
    sleep(2)
    search_window = browser.find_element_by_css_selector(".XTCLo")
    search_window.send_keys(hashtag)
    select_result = browser.find_element_by_css_selector(".fuqBx")
    select_result.click()


with webdriver.Firefox() as browser:
    browser.implicitly_wait(3)
    browser.get(url)

    login_page()
    sleep(2)

    dont_save_window()
    sleep(1)
    not_now_window()
    search_by_hashtag()
    sleep(100)


from typing import List

from selenium import webdriver
from time import sleep

from selenium.webdriver.remote.webelement import WebElement

url = 'https://www.instagram.com/'
url1 = 'https://www.instagram.com/ted'

login = input("Your login: ")
password = input("Your password: ")


def login_page():
    login_link = browser.find_element_by_name('username')
    login_link.click()
    login_link.send_keys(login)  # Login

    password_link = browser.find_element_by_name('password')
    password_link.click()
    password_link.send_keys(password)  # Password

    click_button = browser.find_element_by_css_selector("button[type='submit']")
    click_button.click()


def not_now_window():
    sleep(4)

    not_now_button = browser.find_element_by_css_selector("button.aOOlW:nth-child(2)")
    not_now_button.click()

def dont_save_window():
    sleep(4)

    not_now_button = browser.find_element_by_css_selector("button.sqdOP:nth-child(1)")
    not_now_button.click()


#def follow():
#    sleep(3)
#    follow_button = browser.find_element_by_css_selector("._6VtSN")
#    sleep(3)
#    follow_button.click()

# def follow():
#     sleep(3)
#     browser.get("https://www.instagram.com/explore/people/suggested/")
#     follow_button: List[WebElement] = browser.find_elements_by_css_selector("svg:nth-child(1)")
#     for i in follow_button:
#         sleep(2)
#         i.click()


def like():
    sleep(3)
    follow_button: List[WebElement] = browser.find_elements_by_css_selector("div:nth-child(3) > section:nth-child(1) > span:nth-child(1) > button:nth-child(1)")
    for i in follow_button:
        sleep(1)
        i.click()


with webdriver.Firefox() as browser:
    browser.implicitly_wait(5)
    browser.get(url)

    login_page()
    sleep(4)
    #browser.get(url)
    #sleep(4)

    dont_save_window()
    sleep(1)
    not_now_window()

    like()
    sleep(200)

sleep(100)



from typing import List
from selenium import webdriver
from time import sleep
from selenium.webdriver.remote.webelement import WebElement

url = 'https://www.instagram.com/'

login = input("Your login: ")
password = input("Your password: ")


def login_page():
    login_link = browser.find_element_by_name('username')
    login_link.click()
    login_link.send_keys(login)  # Login

    password_link = browser.find_element_by_name('password')
    password_link.click()
    password_link.send_keys(password)  # Password

    click_button = browser.find_element_by_css_selector("button[type='submit']")
    click_button.click()


def not_now_window():
    sleep(4)

    not_now_button = browser.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
    not_now_button.click()


def notification():
    sleep(3)
    later_button = browser.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
    later_button.click()


# def follow():
#     sleep(3)
#     follow_button = browser.find_elements_by_xpath(
#         "//button[contains(text(), 'Follow')][not(contains(text(), 'Unfollow'))][not(contains(text(), 'Followers'))]")
#     for i in follow_button:
#         sleep(2)
#         i.click()


def like():
    sleep(2)
    like_now: List[WebElement] = browser.find_elements_by_css_selector()
    for i in like_now:
        sleep(2)
        i.click()


with webdriver.Firefox() as browser:
    browser.implicitly_wait(5)
    browser.get(url)

    login_page()
    not_now_window()
    notification()
    sleep(10000)
    like()

    # browser.get(url1)
    # follow()

from typing import List

from selenium import webdriver
from time import sleep

from selenium.webdriver.remote.webelement import WebElement

url = 'https://www.instagram.com/'
url1 = 'https://www.instagram.com/ted'

login = input("Your login: ")
password = input("Your password: ")


def login_page():
    login_link = browser.find_element_by_name('username')
    login_link.click()
    login_link.send_keys(login)  # Login

    password_link = browser.find_element_by_name('password')
    password_link.click()
    password_link.send_keys(password)  # Password

    click_button = browser.find_element_by_css_selector("button[type='submit']")
    click_button.click()


def not_now_window():
    sleep(4)

    not_now_button = browser.find_element_by_css_selector("button.aOOlW:nth-child(2)")
    not_now_button.click()


def dont_save_window():
    sleep(4)

    not_now_button = browser.find_element_by_css_selector("button.sqdOP:nth-child(1)")
    not_now_button.click()


# def follow():
#    sleep(3)
#    follow_button = browser.find_element_by_css_selector("._6VtSN")
#    sleep(3)
#    follow_button.click()


def like():
    sleep(3)
    like_button: List[WebElement] = browser.find_elements_by_xpath("//*[contains(@aria-label, 'Нравится')]")

    for likes in like_button:
        h = likes.get_attribute("height")
        if h == '24':
            likes.click()
            sleep(2)


with webdriver.Firefox() as browser:
    browser.implicitly_wait(5)
    browser.get(url)
    login_page()
    sleep(4)
    dont_save_window()
    sleep(1)
    not_now_window()
    browser.get("https://www.instagram.com/JosephDayberg")
    while True:
        like()
        sleep(3)
