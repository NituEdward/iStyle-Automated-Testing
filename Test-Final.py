# TESTCASE
# Plan de Testare
# Scopul Testării:
# Testele urmăresc verificarea funcționalității de bază a site-ului https://snapsify.com, incluzând verificarea statusului paginii de start, funcționalitatea căutării, adăugarea unui produs în coș și adăugarea unui review.

# Modalitatea de Testare:

# Black Box Testing (testare automată cu Selenium pentru interfață utilizator și requests pentru HTTP)
# Testare Automată
# Instrumentele Folosite pentru Testare:

# Selenium WebDriver pentru testarea interfeței utilizatorului
# Modulul requests din Python pentru testarea HTTP
# Pytest pentru organizarea și rularea testelor
# Mediul de Testare:

# Web pe Windows 11
# Browser: Google Chrome

# Ce va fi testat și rezultatul așteptat:

# Verificarea statusului paginii de start:
# URL: https://snapsify.com
# Rezultatul așteptat: Codul de status HTTP 200
# Funcționalitatea de căutare pe site:
# URL: https://snapsify.com
# Rezultatul așteptat: Găsirea unui produs specific și revenirea la pagina principală
# Adăugarea unui produs în coș:
# URL: https://snapsify.com
# Rezultatul așteptat: Produsul este adăugat cu succes în coș
# Adăugarea unui review pe site:
# URL: https://snapsify.com
# Rezultatul așteptat: Review-ul este adăugat cu succes


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

#Setup pentru Browser
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Test pentru verificarea statusului paginii de start
def test_homepage_status():
    import requests
    url = "https://snapsify.com"
    response = requests.get(url)
    # Verificarea codului de status HTTP
    assert response.status_code == 200, f"Codul de status este {response.status_code}, dar asteptam 200"
    # Verificarea lungimii raspunsului
    assert len(response.text) > 0, "Conținutul răspunsului este gol"

# Test pentru functionalitatea de cautare pe site
def test_website_search(browser):
    url = "https://snapsify.com"
    browser.get(url)
    browser.maximize_window()  

    time.sleep(3)  

    try:
        # Click pe search_bar
        search_icon = browser.find_element(By.XPATH, "/html/body/div[1]/sticky-header/header/details-modal/details/summary/span")
        assert search_icon is not None, "Iconița de căutare nu a fost găsită"
        search_icon.click()  

        time.sleep(3)  

        # Verificarea existentei search_bar
        search_bar = browser.find_element(By.ID, "Search-In-Modal-1")
        assert search_bar is not None, "Bara de căutare nu a fost găsită"
        search_bar.send_keys("Portable Digital Frame")  

        time.sleep(3) 

        # Găsirea existentei rezultatului cautat
        click_bar = browser.find_element(By.XPATH, "/html/body/div[1]/sticky-header/header/details-modal/details/div/div[2]/predictive-search/form/div[2]/div/div[1]/div[2]/div/ul/li/a/div")
        assert click_bar is not None, "Rezultatul căutării nu a fost găsit"
        click_bar.click()  

        time.sleep(3)  

        # Inapoi la pagina principala
        back = browser.find_element(By.XPATH, "/html/body/div[1]/sticky-header/header/a/div/img")
        assert back is not None, "Butonul de revenire nu a fost găsit"
        back.click()  

        time.sleep(3)  
        
        print("Testul a fost finalizat cu succes!")  

    except Exception as e:
        pytest.fail(f"Testul a eșuat cu eroarea: {e}")  

# Test pentru adaugarea unui produs în cos
def test_website_add(browser):
    url = "https://snapsify.com"
    browser.get(url)
    browser.maximize_window()  

    time.sleep(3)  

    try:
        # Selectarea produsului
        select_product = browser.find_element(By.ID, "ProductSubmitButton-template--21367574724943__featured_product_iTmGJe")
        assert select_product is not None, "Butonul de selectare a produsului nu a fost găsit"
        select_product.click()  

        time.sleep(3)  

        # Vizualizarea cosului de cumparaturi
        view_cart = browser.find_element(By.ID, "cart-notification-button")
        assert view_cart is not None, "Butonul de vizualizare a coșului nu a fost găsit"
        view_cart.click()  

        time.sleep(3)  

        # Adaugare in cosul de cumparaturi
        add_to_cart = browser.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div/div[3]/div/div/div[2]/div/ul/li[1]/div")
        assert add_to_cart is not None, "Butonul de adăugare în coș nu a fost găsit"
        add_to_cart.click()  

        time.sleep(5)  

        browser.close() 

        print("Testul a fost finalizat cu succes!") 
    except Exception as e:
        pytest.fail(f"Testul a eșuat cu eroarea: {e}") 

# Test pentru adaugarea unui review pe site
def test_website_review(browser):
    url = "https://snapsify.com"
    browser.get(url)
    browser.maximize_window()  

    time.sleep(3) 

    try:
        #Scroll pana jos la sectiunea de Review
        browser.execute_script("window.scrollTo(0, 1300);")  

        time.sleep(2) 

        # Scriere review
        write_review = browser.find_element(By.XPATH, "/html/body/main/section[4]/div/div/div[2]/div/div[1]/div[1]/div[3]/a")
        assert write_review is not None, "Butonul de scriere a review-ului nu a fost găsit"
        write_review.click()  

        time.sleep(2) 

        # Nota Review
        nota_review = browser.find_element(By.XPATH, "/html/body/main/section[4]/div/div/div[2]/div/div[1]/div[2]/form/div[2]/span/a[5]")
        assert nota_review is not None, "Butonul de notare a review-ului nu a fost găsit"
        nota_review.click() 

        time.sleep(2)  

        # Titlu Review
        review_title = browser.find_element(By.NAME, "review_title")
        assert review_title is not None, "Câmpul pentru titlul review-ului nu a fost găsit"
        review_title.send_keys("Title") 

        time.sleep(2)  

        # Comentariu Review
        review_comments = browser.find_element(By.NAME, "review_body")
        assert review_comments is not None, "Câmpul pentru comentariile review-ului nu a fost găsit"
        review_comments.send_keys("Very good!")  

        time.sleep(2)  

        browser.execute_script("window.scrollTo(1300, 2050);")  

        time.sleep(2)  

        # Nume Review
        name_review = browser.find_element(By.NAME, "reviewer_name")
        assert name_review is not None, "Câmpul pentru numele reviewer-ului nu a fost găsit"
        name_review.send_keys("John Smith") 

        time.sleep(2)  

        # Email Review
        email_review = browser.find_element(By.NAME, "reviewer_email")
        assert email_review is not None, "Câmpul pentru email-ul reviewer-ului nu a fost găsit"
        email_review.send_keys("john_smith2002@gmail.com") 

        time.sleep(3) 
        
        browser.close()  

        print("Testul a fost finalizat cu succes!")  
        
    except Exception as e:
        pytest.fail(f"Testul a eșuat cu eroarea: {e}")  


