from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest
import requests

#Setup pentru Browser
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


# Test pentru verificarea statusului paginii de start
def test_homepage_status():
    url = "https://istyle.ro"
    response = requests.get(url)
    # Verificarea codului de status HTTP
    assert response.status_code == 200, f"Codul de status este {response.status_code}, dar asteptam 200"
    # Verificarea lungimii raspunsului
    assert len(response.text) > 0, "Continutul raspunsului este gol"


# Test pentru functionalitatea de cautare pe site
def test_website_search(browser):
    url = "https://istyle.ro"
    browser.get(url)
    browser.maximize_window()  

    time.sleep(3)  

        #Inchidere Cookie Element
    cookie_element = browser.find_element(By.XPATH, "//div[4]//button[4]")
    cookie_element.click()
    time.sleep(3)

    # Click pe search_bar
    click_search = browser.find_element(By.ID,"algolia-showsearch")
    click_search.click()

    time.sleep(3)
        
    #Search
    search_bar = browser.find_element(By.ID,"search")
    assert search_bar.is_displayed(), "Bara de căutare nu este vizibila"
    search_bar.send_keys("Airpods")
    time.sleep(1)
    search_bar.send_keys(Keys.ENTER)  

    time.sleep(3)
       

#Test pentru adaugarea produsului in cos
def test_website_add(browser):
    url = "https://istyle.ro"
    browser.get(url)
    browser.maximize_window()  

    #Inchidere Cookie Element
    cookie_element = browser.find_element(By.XPATH, "//div[4]//button[4]")
    cookie_element.click()        
    
    time.sleep(3)

    # Click pe search_bar
    click_search = browser.find_element(By.ID,"algolia-showsearch")
    click_search.click()

    time.sleep(3)
        
    #Search
    search_bar = browser.find_element(By.ID,"search")
    assert search_bar.is_displayed(), "Bara de cautare nu este vizibila"
    search_bar.send_keys("Airpods")
    time.sleep(1)
    search_bar.send_keys(Keys.ENTER)  

    time.sleep(3)

    #Selecteaza produsul
    item_product = browser.find_element(By.CLASS_NAME,"product-item-name")
    item_product.click()

    time.sleep(3)

    #Adauga produsul in cos
    add_product = browser.find_element(By.CLASS_NAME,"tocart-error__text")
    add_product.click()

    time.sleep(3)

    #Vizualizare cos de cumparaturi
    cart = browser.find_element(By.XPATH, "//header//div[3]/div[3]/a/div/div/span[2]")

    cart.click()

    time.sleep(3)

    #Checkout
    checkout = browser.find_element(By.CSS_SELECTOR,"#minicart-content-wrapper > div.block-content > div.actions > a")
    checkout.click()

    time.sleep(3)

#Test pentru adaugarea mai multor produse in cos
def test_add_multiple_prod(browser):
    url = "https://istyle.ro"
    browser.get(url)
    browser.maximize_window()  


    #Inchidere Cookie Element
    cookie_element = browser.find_element(By.XPATH, "//div[4]//button[4]")
    cookie_element.click()
    time.sleep(3)

    # Click pe search_bar
    click_search = browser.find_element(By.ID,"algolia-showsearch")
    click_search.click()

    time.sleep(3)
        
    #Search
    search_bar = browser.find_element(By.ID,"search")
    assert search_bar.is_displayed(), "Bara de căutare nu este vizibila"
    search_bar.send_keys("Airpods")
    time.sleep(1)
    search_bar.send_keys(Keys.ENTER)  

    time.sleep(3)

    #Selecteaza produsul
    item_product = browser.find_element(By.CLASS_NAME,"product-item-name")
    item_product.click()

    time.sleep(3)

    #Adauga produsul in cos
    add_product = browser.find_element(By.CLASS_NAME,"tocart-error__text")
    add_product.click()

    time.sleep(3)

    #Vizualizare cos de cumparaturi
    cart = browser.find_element(By.XPATH, "//header//div[3]/div[3]/a/div/div/span[2]")
    cart.click()

    time.sleep(3)

    #Checkout
    checkout = browser.find_element(By.CSS_SELECTOR,"#minicart-content-wrapper > div.block-content > div.actions > a")
    checkout.click()

    time.sleep(3)

    #Adauga mai multe produse
    add_more_product = browser.find_element(By.XPATH, "//div[2]/form/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]")
  
    # Numarul de produse
    num_prod = 3
    for nr in range(num_prod):
        add_more_product.click()

    time.sleep(3)

#Test pentru inregistrare
def test_login(browser):
    url = "https://istyle.ro"
    browser.get(url)
    browser.maximize_window()  

    #Inchidere Cookie Element
    cookie_element = browser.find_element(By.XPATH, "//div[4]//button[4]")
    cookie_element.click()
    time.sleep(3)

    #Click pe iconita de Login
    user_icon = browser.find_element(By.ID,"header-account-toggle")
    user_icon.click()

    time.sleep(3)

    #Login
    login = browser.find_element(By.CSS_SELECTOR,"#ui-id-2 > ul > li.authorization-link > a")
    login.click()

    time.sleep(3)

    #Date de logare
    email_input = browser.find_element(By.ID, "email")
    password_input = browser.find_element(By.ID, "pass")
    login_button = browser.find_element(By.ID, "send2")

    assert email_input.is_displayed(), "Campul pentru email nu este vizibil"
    assert password_input.is_displayed(), "Campul pentru parolă nu este vizibil"
    assert login_button.is_displayed(), "Butonul de login nu este vizibil"

    email_input.send_keys("neatamarius895@gmail.com")
    password_input.send_keys("!Icloud123")
    login_button.click()
        
    time.sleep(3)

#Test News Letter
def test_news_letter(browser):
    url = "https://istyle.ro"
    browser.get(url)
    browser.maximize_window()  

    #Inchidere Cookie Element
    cookie_element = browser.find_element(By.XPATH, "//div[4]//button[4]")
    cookie_element.click()
    time.sleep(3)

    #Scroll pana jos la Footer
    browser.execute_script("window.scrollTo(0, 4700);")  

    time.sleep(3)

    #Inchidere reclama
    popout_close = browser.find_element(By.CLASS_NAME,"mfp-close")
    popout_close.click()

    time.sleep(3)

    #Introducere date
    nume_input = browser.find_element(By.NAME, "Last Name")
    prenume_input = browser.find_element(By.NAME, "First Name")
    email_input = browser.find_element(By.ID, "Email Address")
    box = browser.find_element(By.ID,"ui-kit-checkbox-1")

    nume_input.send_keys("Marius")
    prenume_input.send_keys("Neata")
    email_input.send_keys("mariusneata955@gmail.com")
    box.click()

    time.sleep(2)

    #Apasa pe butonul de abonare
    subscribe_button = browser.find_element(By.CSS_SELECTOR,"#landingpage > div:nth-child(15) > div > div > div > div > div > form > div > div.col-lg-4 > button")
    assert subscribe_button is not None, "Butonul de abonare nu a fost gasit"
    subscribe_button.click()

    time.sleep(3)
 
#Test pentru Feedback
def test_contact(browser):
    url = "https://istyle.ro"
    browser.get(url)
    browser.maximize_window()  


    #Inchidere Cookie Element
    cookie_element = browser.find_element(By.XPATH, "//div[4]//button[4]")
    cookie_element.click()
    time.sleep(3)

    #Scroll pana jos la Footer
    browser.execute_script("window.scrollTo(0, 5300);")  

    time.sleep(3)

    #Inchidere reclama
    popout_close = browser.find_element(By.CLASS_NAME,"mfp-close")
    popout_close.click()

    time.sleep(3)

    #Contact
    contact = browser.find_element(By.CSS_SELECTOR,"#landingpage > div:nth-child(16) > div > div:nth-child(2) > div > div > a")
    contact.click()

    time.sleep(3)

    #Scroll 
    browser.execute_script("window.scrollTo(0, 1700);")  

    time.sleep(3)

    #Feedback
    feedback = browser.find_element(By.ID,"feedBackForm")
    assert feedback is not None, "Feedback nu a fost gasit"
    feedback.click()

    time.sleep(3)

     #Review
    review_input = browser.find_element(By.NAME,"Text rating")
    assert review_input is not None, "Review nu a fost gasit"
    review_input.send_keys("Foarte bun!")

    #Email
    email_input = browser.find_element(By.NAME,"Email")
    assert email_input is not None, "Email nu a fost gasit"
    email_input.send_keys("mariusneata999@gmail.com")

    #Checkbox
    checkbox = browser.find_element(By.ID,"gdpr_checkbox")
    assert checkbox is not None, "GDPR checkbox nu a fost gasit"
    checkbox.click()

    #Trimite feedback
    send_feedback = browser.find_element(By.CSS_SELECTOR,"#reviewForm > input")
    assert send_feedback is not None, "Feedback send nu a fost gasit"
    send_feedback.click()

    time.sleep(3)
