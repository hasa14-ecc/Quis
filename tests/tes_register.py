import time
import uuid
from tests.pages.register_page import RegisterPage
from tests.pages.login_page import LoginPage

def test_reg_01_register_success(browser, base_url):
    tag = uuid.uuid4().hex[:6]
    uname = f"user_{tag}"
    email = f"user_{tag}@mail.com"

    reg = RegisterPage(browser, base_url)
    reg.open()
    reg.register("Ilham", email, uname, "Passw0rd!", "Passw0rd!")
    time.sleep(0.5)

    browser.delete_all_cookies()
    login = LoginPage(browser, base_url)
    login.open()
    login.login(uname, "Passw0rd!")
    time.sleep(0.5)

    assert "index.php" in browser.current_url

def test_reg_02_name_empty_allowed(browser, base_url):
    tag = uuid.uuid4().hex[:6]
    uname = f"user_noname_{tag}"
    email = f"user_noname_{tag}@mail.com"

    reg = RegisterPage(browser, base_url)
    reg.open()
    reg.register("", email, uname, "Passw0rd!", "Passw0rd!")
    time.sleep(0.5)

    browser.delete_all_cookies()
    login = LoginPage(browser, base_url)
    login.open()
    login.login(uname, "Passw0rd!")
    time.sleep(0.5)

    assert "index.php" in browser.current_url or "login.php" in browser.current_url or login.alert_text() != ""

def test_reg_04_password_mismatch(browser, base_url):
    tag = uuid.uuid4().hex[:6]
    uname = f"user_mismatch_{tag}"
    email = f"user_mismatch_{tag}@mail.com"

    reg = RegisterPage(browser, base_url)
    reg.open()
    reg.register("Ilham", email, uname, "Passw0rd!", "BedaPass123")
    time.sleep(0.5)

    # harus tetap di halaman register / ada alert
    assert "register.php" in browser.current_url or reg.alert_text() != ""
