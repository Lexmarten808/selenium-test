"""
locators_demo.py
-----------------
Demostración de los 5 localizadores principales de Selenium:
ID, NAME, CLASS_NAME, XPATH y CSS_SELECTOR.

Página usada para la demo: https://the-internet.herokuapp.com/login
(página pública pensada justo para practicar automatización de pruebas)

Ejecutar:
    pip install -r requirements.txt
    python locators_demo.py
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/login"


def main():
    # --- Inicializar el WebDriver ---
    # Desde Selenium 4.6+ no se necesita descargar el driver manualmente,
    # Selenium Manager lo resuelve automáticamente.
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # --- Navegar a la URL ---
        driver.get(URL)
        wait = WebDriverWait(driver, 10)

        # 1) Localizador por ID  --> el más rápido y estable, úsalo primero
        username_input = wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        print("[ID] Campo encontrado:", username_input.get_attribute("name"))

        # 2) Localizador por NAME --> útil cuando no hay id, común en formularios
        password_input = driver.find_element(By.NAME, "password")
        print("[NAME] Campo encontrado:", password_input.get_attribute("id"))

        # 3) Localizador por CLASS_NAME --> ideal para botones/estilos reutilizados
        login_button = driver.find_element(By.CLASS_NAME, "radius")
        print("[CLASS_NAME] Botón encontrado:", login_button.text or "Login")

        # 4) Localizador por CSS_SELECTOR --> flexible, rápido, preferido sobre XPath
        flash_css = "#flash"
        print("[CSS_SELECTOR] Selector preparado para el mensaje:", flash_css)

        # 5) Localizador por XPATH --> el más potente pero el más lento y frágil,
        #    úsalo solo cuando los anteriores no alcanzan (ej. navegar por texto)
        logout_xpath = "//a[contains(text(),'Logout')]"
        print("[XPATH] Selector preparado para el botón de logout:", logout_xpath)

        # --- Interactuar con los elementos ---
        username_input.send_keys("tomsmith")
        password_input.send_keys("SuperSecretPassword!")
        login_button.click()

        # --- Validar el resultado (assertion) ---
        flash_message = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, flash_css))
        )
        assert "You logged into a secure area" in flash_message.text, (
            "El mensaje de éxito no apareció, revisar credenciales o selectores"
        )
        print("Assertion OK: login exitoso ✅")

    finally:
        # --- Cerrar el navegador siempre, incluso si falla una aserción ---
        driver.quit()


if __name__ == "__main__":
    main()