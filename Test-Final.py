from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
import requests
import logging

# Configurare logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestData:
    """Clasa pentru datele de test"""
    BASE_URL = "https://istyle.ro"
    EMAIL = "neatamarius895@gmail.com"
    PASSWORD = "!Icloud123"
    SEARCH_TERM = "Airpods"
    NEWSLETTER_EMAIL = "mariusneata955@gmail.com"
    FEEDBACK_EMAIL = "mariusneata999@gmail.com"
    FEEDBACK_TEXT = "Foarte bun!"

@pytest.fixture
def browser():
    """Fixture pentru browser"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    logger.info("Browser inițializat")
    yield driver
    driver.quit()
    logger.info("Browser închis")

def handle_cookie_consent(browser):
    """Funcție pentru gestionarea cookie consent"""
    try:
        cookie_element = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[4]//button[4]"))
        )
        cookie_element.click()
        logger.info("Cookie consent acceptat")
        time.sleep(2)
    except Exception as e:
        logger.warning(f"Nu s-a putut gestiona cookie consent: {e}")

def test_homepage_status():
    """Test pentru verificarea statusului paginii de start"""
    logger.info("Verificare status homepage")
    response = requests.get(TestData.BASE_URL)
    assert response.status_code == 200, f"Status code invalid: {response.status_code}"
    assert len(response.text) > 0, "Răspuns gol"
    logger.info("Test status homepage completat cu succes")

def test_website_search(browser):
    """Test pentru funcționalitatea de căutare"""
    logger.info("Începere test căutare")
    browser.get(TestData.BASE_URL)
    handle_cookie_consent(browser)

    # Click pe search_bar
    search_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "algolia-showsearch"))
    )
    search_button.click()
    time.sleep(2)

    # Căutare produs
    search_bar = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )
    assert search_bar.is_displayed(), "Bara de căutare nu este vizibilă"
    search_bar.send_keys(TestData.SEARCH_TERM)
    search_bar.send_keys(Keys.ENTER)
    logger.info("Test căutare completat cu succes")
    time.sleep(2)

def test_website_add(browser):
    """Test pentru adăugarea produsului în coș"""
    logger.info("Începere test adăugare în coș")
    browser.get(TestData.BASE_URL)
    handle_cookie_consent(browser)

    # Căutare și selectare produs
    search_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "algolia-showsearch"))
    )
    search_button.click()
    time.sleep(2)

    search_bar = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )
    search_bar.send_keys(TestData.SEARCH_TERM)
    search_bar.send_keys(Keys.ENTER)
    time.sleep(2)

    # Adăugare în coș
    item_product = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "product-item-name"))
    )
    item_product.click()
    time.sleep(2)

    add_product = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "tocart-error__text"))
    )
    add_product.click()
    time.sleep(2)

    # Checkout
    cart = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//header//div[3]/div[3]/a/div/div/span[2]"))
    )
    cart.click()
    time.sleep(2)

    checkout = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#minicart-content-wrapper > div.block-content > div.actions > a"))
    )
    checkout.click()
    logger.info("Test adăugare în coș completat cu succes")
    time.sleep(2)

def test_add_multiple_prod(browser):
    """Test pentru adăugarea mai multor produse în coș"""
    logger.info("Începere test adăugare multiple produse")
    browser.get(TestData.BASE_URL)
    handle_cookie_consent(browser)

    # Repetă pașii de adăugare în coș
    test_website_add(browser)

    # Adaugă cantitate multiplă
    add_more_product = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[2]/form/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]"))
    )

    for _ in range(3):
        add_more_product.click()
        time.sleep(1)
    
    logger.info("Test adăugare multiple produse completat cu succes")

def test_login(browser):
    """Test pentru funcționalitatea de login"""
    logger.info("Începere test login")
    browser.get(TestData.BASE_URL)
    handle_cookie_consent(browser)

    # Login process
    user_icon = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "header-account-toggle"))
    )
    user_icon.click()
    time.sleep(2)

    login = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#ui-id-2 > ul > li.authorization-link > a"))
    )
    login.click()
    time.sleep(2)

    email_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    password_input = browser.find_element(By.ID, "pass")
    login_button = browser.find_element(By.ID, "send2")

    email_input.send_keys(TestData.EMAIL)
    password_input.send_keys(TestData.PASSWORD)
    login_button.click()
    logger.info("Test login completat cu succes")
    time.sleep(2)

def test_news_letter(browser):
    """Test pentru abonarea la newsletter"""
    logger.info("Începere test newsletter")
    browser.get(TestData.BASE_URL)
    handle_cookie_consent(browser)

    # Scroll la footer
    browser.execute_script("window.scrollTo(0, 4700);")
    time.sleep(2)

    # Închide popup dacă există
    try:
        popout_close = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mfp-close"))
        )
        popout_close.click()
        time.sleep(2)
    except:
        logger.info("Nu există popup de închis")

    # Completare formular newsletter
    nume_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "Last Name"))
    )
    prenume_input = browser.find_element(By.NAME, "First Name")
    email_input = browser.find_element(By.ID, "Email Address")
    box = browser.find_element(By.ID, "ui-kit-checkbox-1")

    nume_input.send_keys("Neata")
    prenume_input.send_keys("Marius")
    email_input.send_keys(TestData.NEWSLETTER_EMAIL)
    box.click()
    time.sleep(1)

    subscribe_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#landingpage > div:nth-child(15) > div > div > div > div > div > form > div > div.col-lg-4 > button"))
    )
    subscribe_button.click()
    logger.info("Test newsletter completat cu succes")
    time.sleep(2)

def test_contact(browser):
    """Test pentru formularul de contact"""
    logger.info("Începere test formular contact")
    browser.get(TestData.BASE_URL)
    handle_cookie_consent(browser)

    # Scroll la secțiunea de contact
    browser.execute_script("window.scrollTo(0, 5300);")
    time.sleep(2)

    # Închide popup dacă există
    try:
        popout_close = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mfp-close"))
        )
        popout_close.click()
        time.sleep(2)
    except:
        logger.info("Nu există popup de închis")

    # Completare formular contact
    contact = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#landingpage > div:nth-child(16) > div > div:nth-child(2) > div > div > a"))
    )
    contact.click()
    time.sleep(2)

    browser.execute_script("window.scrollTo(0, 1700);")
    time.sleep(2)

    feedback = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "feedBackForm"))
    )
    feedback.click()
    time.sleep(2)

    review_inputs = browser.find_elements(By.NAME, "Text rating")
    review_inputs[0].send_keys(TestData.FEEDBACK_TEXT)

    email_input = browser.find_element(By.NAME, "Email")
    email_input.send_keys(TestData.FEEDBACK_EMAIL)
    time.sleep(2)

    actions = ActionChains(browser)
    actions.send_keys(Keys.PAGE_DOWN)
    actions.send_keys(Keys.PAGE_DOWN)
    actions.perform()
    time.sleep(2)

    checkbox = browser.find_elements(By.ID, "gdpr_checkbox")[0]
    checkbox.click()

    submit_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#reviewForm > input"))
    )
    submit_button.click()
    logger.info("Test formular contact completat cu succes")
    time.sleep(2)

if __name__ == "__main__":
    pytest.main(["-v"])
