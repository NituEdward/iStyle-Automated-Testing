from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_homepage_status():
    import requests
    url = "https://snapsify.com"
    response = requests.get(url)
    assert response.status_code == 200, f"Status code is {response.status_code}, expected 200"

def test_website_search(browser):
    url = "https://snapsify.com"
    browser.get(url)
    browser.maximize_window()

    time.sleep(3)

    try:
        search_icon = browser.find_element(By.XPATH, "/html/body/div[1]/sticky-header/header/details-modal/details/summary/span")
        assert search_icon is not None, "Search icon not found"
        search_icon.click()

        time.sleep(3)

        search_bar = browser.find_element(By.ID, "Search-In-Modal-1")
        assert search_bar is not None, "Search bar not found"
        search_bar.send_keys("Portable Digital Frame")

        time.sleep(3)

        click_bar = browser.find_element(By.XPATH, "/html/body/div[1]/sticky-header/header/details-modal/details/div/div[2]/predictive-search/form/div[2]/div/div[1]/div[2]/div/ul/li/a/div")
        assert click_bar is not None, "Search result not found"
        click_bar.click()

        time.sleep(3)

        back = browser.find_element(By.XPATH, "/html/body/div[1]/sticky-header/header/a/div/img")
        assert back is not None, "Back button not found"
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
        assert select_product is not None, "Product button not found"
        select_product.click()

        time.sleep(3)

        view_cart = browser.find_element(By.ID, "cart-notification-button")
        assert view_cart is not None, "View cart button not found"
        view_cart.click()

        time.sleep(3)

        add_to_cart = browser.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div/div[3]/div/div/div[2]/div/ul/li[1]/div")
        assert add_to_cart is not None, "Add to cart button not found"
        add_to_cart.click()

        time.sleep(5)

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
        browser.execute_script("window.scrollTo(0, 1300);")

        time.sleep(2)

        write_review = browser.find_element(By.XPATH, "/html/body/main/section[4]/div/div/div[2]/div/div[1]/div[1]/div[3]/a")
        assert write_review is not None, "Write review button not found"
        write_review.click()

        time.sleep(2)

        nota_review = browser.find_element(By.XPATH, "/html/body/main/section[4]/div/div/div[2]/div/div[1]/div[2]/form/div[2]/span/a[5]")
        assert nota_review is not None, "Review rating button not found"
        nota_review.click()

        time.sleep(2)

        review_title = browser.find_element(By.NAME, "review_title")
        assert review_title is not None, "Review title input not found"
        review_title.send_keys("Title")

        time.sleep(2)

        review_comments = browser.find_element(By.NAME, "review_body")
        assert review_comments is not None, "Review comments input not found"
        review_comments.send_keys("Very good!")

        time.sleep(2)

        browser.execute_script("window.scrollTo(1300, 2050);")

        time.sleep(2)

        name_review = browser.find_element(By.NAME, "reviewer_name")
        assert name_review is not None, "Reviewer name input not found"
        name_review.send_keys("John Smith")

        time.sleep(2)

        email_review = browser.find_element(By.NAME, "reviewer_email")
        assert email_review is not None, "Reviewer email input not found"
        email_review.send_keys("john_smith2002@gmail.com")

        time.sleep(3)
        
        browser.close()

        print("Testul a fost finalizat cu succes!")
        
    except Exception as e:
        pytest.fail(f"Testul a eșuat cu eroarea: {e}")


