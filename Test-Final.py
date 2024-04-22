from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_website_search(browser):
    url = "https://snapsify.com"
    browser.get(url)
    browser.maximize_window()

    time.sleep(3)

    try:
        # Identifică și dă click pe iconița de căutare
        search_icon = browser.find_element(By.XPATH, "/html/body/div[1]/sticky-header/header/details-modal/details/summary/span ")
        search_icon.click()

        time.sleep(3)

        # Completează bara de căutare cu un termen
        search_bar = browser.find_element(By.ID, "Search-In-Modal-1")
        search_bar.send_keys("Portable Digital Frame")

        time.sleep(3)

        # Alege un element din rezultatele căutării
        click_bar = browser.find_element(By.XPATH, "/html/body/div[1]/sticky-header/header/details-modal/details/div/div[2]/predictive-search/form/div[2]/div/div[1]/div[2]/div/ul/li/a/div")
        click_bar.click()

        time.sleep(3)

        # Navighează înapoi la pagina principală
        back = browser.find_element(By.XPATH, "/html/body/div[1]/sticky-header/header/a/div/img")
        back.click()

        time.sleep(3)
        
        

        print("Testul a fost finalizat cu succes!")

        
    except Exception as e:
        pytest.fail(f"Testul a eșuat cu eroarea: {e}")


def test_website_add(browser):
    url = "https://snapsify.com"
    browser.get(url)
    browser.maximize_window()

    time.sleep(3)

    try:
        select_product = browser.find_element(By.ID, "ProductSubmitButton-template--21367574724943__featured_product_iTmGJe")
        select_product.click()

        time.sleep(3)

        view_cart = browser.find_element(By.ID , "cart-notification-button")
        view_cart.click()

        time.sleep(3)

        add_to_cart = browser.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div/div[3]/div/div/div[2]/div/ul/li[1]/div")
        add_to_cart.click()

        time.sleep(5)

        back = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/header/div/div/div/div/header/h2/span/a")
        back.click()

        time.sleep(3)

        browser.close()

        print("Testul a fost finalizat cu succes!")
    except Exception as e:
        pytest.fail(f"Testul a eșuat cu eroarea: {e}")



def test_website_review(browser):
    url = "https://snapsify.com"
    browser.get(url)
    browser.maximize_window()

    time.sleep(3)

    try:

        scroll = browser.execute_script("window.scrollTo(0, 1300);")

        time.sleep(2)

        write_review = browser.find_element(By.XPATH , "/html/body/main/section[4]/div/div/div[2]/div/div[1]/div[1]/div[3]/a")
        write_review.click()

        time.sleep(2)

        nota_review = browser.find_element(By.XPATH , "/html/body/main/section[4]/div/div/div[2]/div/div[1]/div[2]/form/div[2]/span/a[5]")
        nota_review.click()

        time.sleep(2)

        review_title = browser.find_element(By.NAME, "review_title")
        review_title.send_keys("Title")

        time.sleep(2)

        review_comments = browser.find_element(By.NAME, "review_body")
        review_comments.send_keys("Very good!")

        time.sleep(2)

        scroll = browser.execute_script("window.scrollTo(1300, 2050);")

        time.sleep(2)

        name_review = browser.find_element(By.NAME, "reviewer_name")
        name_review.send_keys("John Smith")

        time.sleep(2)

        email_review = browser.find_element(By.NAME, "reviewer_email")
        email_review.send_keys("john_smith2002@gmail.com")

        time.sleep(2)

        submit_review = browser.find_element(By.XPATH, "/html/body/main/section[4]/div/div/div[2]/div/div[1]/div[2]/form/div[10]/input")
        submit_review.click()

        scroll = browser.execute_script("window.scrollTo(0, 1300);")

        time.sleep(2)

        browser.close()


        print("Testul a fost finalizat cu succes!")
        
    except Exception as e:
        pytest.fail(f"Testul a eșuat cu eroarea: {e}")


    







    





