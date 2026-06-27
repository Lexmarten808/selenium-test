"""
test_login_flow.py
-------------------
Demuestra el "Ciclo de vida de un script de Selenium" con pytest:

    1. Inicializar el WebDriver       -> fixture `driver`
    2. Navegar a la URL               -> driver.get(URL)
    3. Interactuar con los elementos  -> send_keys / click
    4. Validar (assertions) y cerrar  -> assert ... / driver.quit() en el fixture

Ejecutar:
    pip install -r requirements.txt
    pytest test_login_flow.py -v

"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/login"


@pytest.fixture
def driver():
    # 1. Inicializar el WebDriver
    drv = webdriver.Chrome()
    drv.maximize_window()
    yield drv
    # 4. (parte final) Cerrar el navegador siempre al terminar la prueba
    drv.quit()


def login(driver, username, password):
    """Helper que repite los pasos 2 y 3 del ciclo de vida."""
    wait = WebDriverWait(driver, 10)

    # 2. Navegar a la URL
    driver.get(URL)

    # 3. Interactuar con los elementos
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    return wait.until(EC.visibility_of_element_located((By.ID, "flash")))


def test_login_exitoso(driver):
    """Caso positivo: credenciales correctas."""
    flash = login(driver, "tomsmith", "SuperSecretPassword!")

    # 4. Validar el resultado (assertion)
    assert "You logged into a secure area" in flash.text
    assert "success" in flash.get_attribute("class")


def test_login_credenciales_invalidas(driver):
    """Caso negativo: la página debe rechazar credenciales incorrectas."""
    flash = login(driver, "usuario_invalido", "clave_incorrecta")

    # 4. Validar el resultado (assertion)
    assert "Your username is invalid" in flash.text
    assert "error" in flash.get_attribute("class")