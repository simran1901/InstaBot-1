from selenium import webdriver
from time import sleep

url = 'https://www.instagram.com/'

print('''Hi! This is InstaBot. Choose what you want to do: 
        Press '1' to search by hashtag;
        Press '2' to follow first 30 people in your recommendation list;
        Press '3' to like first 30 photos on your home page;
        Press '0' to quit the program;''')
choice = input("Please, enter a number from the upper list here: ")

if choice == '1':
    hashtag = "#" + input("Enter a word for hashtag (without the symbol of hashtag): ")
elif choice == "0":
    print(f'\nThank you for choosing InstaBot. We will be waiting for you!')
    exit(0)

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
    select_result = browser.find_element_by_css_selector("a.yCE8d:nth-child(1)")
    select_result.click()

def follow():
    sleep(3)
    follow_button = browser.find_elements_by_css_selector("button:nth-child(1)")
    for i in follow_button:
        sleep(2)
        i.click()

def like():
    sleep(3)
    like_button = browser.find_elements_by_xpath("//*[contains(@aria-label, 'Нравится')]")
    for likes in like_button:
        h = likes.get_attribute("height")
        if h == '24':
            likes.click()
            sleep(2)

with webdriver.Firefox() as browser:
    browser.implicitly_wait(3)
    browser.get(url)

    login_page()
    sleep(2)

    dont_save_window()
    sleep(1)
    not_now_window()

    if choice == '1':
        sleep(5)
        search_by_hashtag()
    elif choice == '2':
        # Follow first 30 people in your recommendation list.
        browser.get("https://www.instagram.com/explore/people/suggested/")
        time = 0
        while time < 30:
            follow()
            time += 1
            sleep(1)
    elif choice == '3':
        # Like first 30 photos on your home page.
        time = 0
        while time < 30:
            like()
            time += 1
            sleep(1)


    sleep(100)
