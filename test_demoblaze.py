"""
Automatización de pruebas — Demoblaze (Product Store)
Cubre: TC-01 Registro, TC-04 Login, TC-08 Filtro Phones,
       TC-12 Agregar al carrito, TC-16 Compra exitosa, TC-07 Logout

Requisitos (ya instalados de la sesión anterior):
    pip install selenium webdriver-manager

Correr con:
    python test_demoblaze.py
"""
import time
import random
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.demoblaze.com/"


def get_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver


def aceptar_alerta(driver, timeout=5):
    """Espera un alert, devuelve su texto y lo acepta."""
    try:
        WebDriverWait(driver, timeout).until(EC.alert_is_present())
        alerta = driver.switch_to.alert
        texto = alerta.text
        alerta.accept()
        return texto
    except (TimeoutException, NoAlertPresentException):
        return None


def usuario_aleatorio():
    sufijo = "".join(random.choices(string.ascii_lowercase, k=6))
    return f"testuser_{sufijo}", "Test1234"


# ---------------------------------------------------------------------------
# TC-01: Registro de usuario nuevo
# ---------------------------------------------------------------------------
def tc01_registro(driver, username, password):
    print("\n[TC-01] Registro de usuario nuevo...")
    wait = WebDriverWait(driver, 10)

    driver.get(BASE_URL)
    wait.until(EC.element_to_be_clickable((By.ID, "signin2"))).click()
    wait.until(EC.visibility_of_element_located((By.ID, "sign-username"))).send_keys(username)
    driver.find_element(By.ID, "sign-password").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Sign up']").click()

    texto = aceptar_alerta(driver)
    if texto and "successful" in texto.lower():
        print(f"[TC-01] PASS — Usuario '{username}' registrado. Alert: '{texto}'")
        return True
    else:
        print(f"[TC-01] FAIL — Alert inesperado: '{texto}'")
        return False


# ---------------------------------------------------------------------------
# TC-03: Registro con campos vacíos (caso negativo)
# ---------------------------------------------------------------------------
def tc03_registro_campos_vacios(driver):
    print("\n[TC-03] Registro con campos vacíos...")
    wait = WebDriverWait(driver, 10)

    driver.get(BASE_URL)
    wait.until(EC.element_to_be_clickable((By.ID, "signin2"))).click()
    wait.until(EC.visibility_of_element_located((By.ID, "sign-username")))
    # Dejar campos vacíos y hacer submit
    driver.find_element(By.XPATH, "//button[text()='Sign up']").click()

    texto = aceptar_alerta(driver)
    if texto:
        print(f"[TC-03] PASS — El sistema alerta ante campos vacíos: '{texto}'")
    else:
        print("[TC-03] FAIL — No apareció ningún alert con campos vacíos")


# ---------------------------------------------------------------------------
# TC-04: Login con credenciales válidas
# ---------------------------------------------------------------------------
def tc04_login(driver, username, password):
    print("\n[TC-04] Login con credenciales válidas...")
    wait = WebDriverWait(driver, 10)

    driver.get(BASE_URL)
    wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()
    wait.until(EC.visibility_of_element_located((By.ID, "loginusername"))).send_keys(username)
    driver.find_element(By.ID, "loginpassword").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Log in']").click()

    try:
        bienvenida = WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located((By.ID, "nameofuser"))
        )
        print(f"[TC-04] PASS — Login exitoso. Texto de bienvenida: '{bienvenida.text}'")
        return True
    except TimeoutException:
        print("[TC-04] FAIL — No apareció el mensaje de bienvenida tras el login")
        return False


# ---------------------------------------------------------------------------
# TC-05: Login con contraseña incorrecta (caso negativo)
# ---------------------------------------------------------------------------
def tc05_login_password_incorrecto(driver, username):
    print("\n[TC-05] Login con contraseña incorrecta...")
    wait = WebDriverWait(driver, 10)

    driver.get(BASE_URL)
    wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()
    wait.until(EC.visibility_of_element_located((By.ID, "loginusername"))).send_keys(username)
    driver.find_element(By.ID, "loginpassword").send_keys("claveincorrecta")
    driver.find_element(By.XPATH, "//button[text()='Log in']").click()

    texto = aceptar_alerta(driver)
    if texto:
        print(f"[TC-05] PASS — Sistema rechaza contraseña incorrecta. Alert: '{texto}'")
    else:
        print("[TC-05] FAIL — No hubo alert con contraseña incorrecta")


# ---------------------------------------------------------------------------
# TC-08: Filtrar por categoría Phones
# ---------------------------------------------------------------------------
def tc08_filtro_phones(driver):
    print("\n[TC-08] Filtrar por categoría Phones...")
    wait = WebDriverWait(driver, 10)

    driver.get(BASE_URL)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[text()='Phones']"))).click()
    time.sleep(2)  # el filtro carga dinámicamente

    productos = driver.find_elements(By.CLASS_NAME, "card-title")
    if productos:
        nombres = [p.text for p in productos if p.text]
        print(f"[TC-08] PASS — Se muestran {len(nombres)} productos: {nombres}")
        return True
    else:
        print("[TC-08] FAIL — No se encontraron productos en categoría Phones")
        return False


# ---------------------------------------------------------------------------
# TC-12: Agregar un producto al carrito (logueado)
# ---------------------------------------------------------------------------
def tc12_agregar_al_carrito(driver):
    print("\n[TC-12] Agregar primer producto al carrito...")
    wait = WebDriverWait(driver, 10)

    # Ir a Phones y hacer clic en el primer producto
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[text()='Phones']"))).click()
    time.sleep(2)

    primer_producto = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@id='tbodyid']//h4/a")))
    nombre_producto = primer_producto.text
    primer_producto.click()

    # En la página del producto, hacer clic en "Add to cart"
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[text()='Add to cart']"))).click()

    texto = aceptar_alerta(driver)
    if texto and "added" in texto.lower():
        print(f"[TC-12] PASS — '{nombre_producto}' agregado al carrito. Alert: '{texto}'")
        return nombre_producto
    else:
        print(f"[TC-12] FAIL — Alert inesperado: '{texto}'")
        return None


# ---------------------------------------------------------------------------
# TC-14: Verificar producto en el carrito
# ---------------------------------------------------------------------------
def tc14_ver_carrito(driver, nombre_producto):
    print("\n[TC-14] Verificar producto en el carrito...")
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, "cartur").click()
    time.sleep(2)

    filas = driver.find_elements(By.XPATH, "//tbody[@id='tbodyid']//tr")
    if filas:
        print(f"[TC-14] PASS — El carrito tiene {len(filas)} producto(s):")
        for fila in filas:
            celdas = fila.find_elements(By.TAG_NAME, "td")
            if celdas:
                print(f"         → {celdas[1].text if len(celdas) > 1 else ''} — ${celdas[2].text if len(celdas) > 2 else ''}")
        return True
    else:
        print("[TC-14] FAIL — El carrito aparece vacío")
        return False


# ---------------------------------------------------------------------------
# TC-16: Compra exitosa (Place Order)
# ---------------------------------------------------------------------------
def tc16_place_order(driver):
    print("\n[TC-16] Completar proceso de compra...")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[text()='Place Order']"))).click()

    wait.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys("Juan Perez")
    driver.find_element(By.ID, "country").send_keys("Argentina")
    driver.find_element(By.ID, "city").send_keys("Tucuman")
    driver.find_element(By.ID, "card").send_keys("1234567890123456")
    driver.find_element(By.ID, "month").send_keys("12")
    driver.find_element(By.ID, "year").send_keys("2026")

    driver.find_element(By.XPATH, "//button[text()='Purchase']").click()

    try:
        confirmacion = WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h2[contains(text(),'Thank you')]"))
        )
        print(f"[TC-16] PASS — Compra confirmada: '{confirmacion.text}'")
        driver.save_screenshot("resultado_compra.png")

        # Cerrar el modal de confirmación
        driver.find_element(By.XPATH, "//button[text()='OK']").click()
        return True
    except TimeoutException:
        print("[TC-16] FAIL — No apareció el modal de confirmación de compra")
        driver.save_screenshot("resultado_compra.png")
        return False


# ---------------------------------------------------------------------------
# TC-07: Logout
# ---------------------------------------------------------------------------
def tc07_logout(driver):
    print("\n[TC-07] Logout...")
    wait = WebDriverWait(driver, 10)

    driver.get(BASE_URL)
    try:
        wait.until(EC.element_to_be_clickable((By.ID, "logout2"))).click()
        time.sleep(1)
        # Verificar que vuelve a mostrar "Log in"
        driver.find_element(By.ID, "login2")
        print("[TC-07] PASS — Logout exitoso, botón 'Log in' visible nuevamente")
    except Exception:
        print("[TC-07] FAIL — No se pudo hacer logout o no apareció el botón de login")


# ---------------------------------------------------------------------------
# TC-18: Enviar mensaje de contacto
# ---------------------------------------------------------------------------
def tc18_contacto(driver):
    print("\n[TC-18] Enviar mensaje de contacto...")
    wait = WebDriverWait(driver, 10)

    driver.get(BASE_URL)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[text()='Contact']"))).click()

    wait.until(EC.visibility_of_element_located(
        (By.ID, "recipient-email"))).send_keys("test@test.com")
    driver.find_element(By.ID, "recipient-name").send_keys("Juan Perez")
    driver.find_element(By.ID, "message-text").send_keys("Este es un mensaje de prueba automatizado.")
    driver.find_element(By.XPATH, "//button[text()='Send message']").click()

    texto = aceptar_alerta(driver)
    if texto:
        print(f"[TC-18] PASS — Mensaje enviado. Alert: '{texto}'")
    else:
        print("[TC-18] FAIL — No apareció confirmación al enviar el mensaje")


# ---------------------------------------------------------------------------
# Ejecución principal
# ---------------------------------------------------------------------------
PAUSA = 5  # segundos de espera entre cada caso de prueba

if __name__ == "__main__":
    username, password = usuario_aleatorio()
    print(f"Usuario de prueba generado: {username}")

    driver = get_driver()
    try:
        driver.get(BASE_URL)

        # Registro
        tc01_registro(driver, username, password)
        time.sleep(PAUSA)

        tc03_registro_campos_vacios(driver)
        time.sleep(PAUSA)

        # Login válido
        tc04_login(driver, username, password)
        time.sleep(PAUSA)

        # Login inválido — TC-05 hace logout implícito al fallar, así que
        # después volvemos a loguear para el flujo del carrito
        tc05_login_password_incorrecto(driver, username)
        time.sleep(PAUSA)

        # Login para el flujo de carrito y compra (único login extra, necesario)
        tc04_login(driver, username, password)
        time.sleep(PAUSA)

        # Navegación y carrito
        tc08_filtro_phones(driver)
        time.sleep(PAUSA)

        nombre = tc12_agregar_al_carrito(driver)
        time.sleep(PAUSA)

        tc14_ver_carrito(driver, nombre)
        time.sleep(PAUSA)

        # Compra
        tc16_place_order(driver)
        time.sleep(PAUSA)

        # Contacto
        tc18_contacto(driver)
        time.sleep(PAUSA)

        # Logout
        tc07_logout(driver)

        print("\n=== Ejecución finalizada. Revisar capturas para evidencia visual. ===")

    finally:
        time.sleep(3)
        driver.quit()
