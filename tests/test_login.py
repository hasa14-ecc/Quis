import time
import uuid
from tests.pages.login_page import LoginPage
from tests.pages.register_page import RegisterPage

def test_log_01_login_success(browser, base_url):
    tag = uuid.uuid4().hex[:6]
    uname = f"user_ok_{tag}"
    email = f"ilham_{tag}@mail.com"

    reg = RegisterPage(browser, base_url)
    reg.open()
    reg.register("Ilham", email, uname, "Passw0rd!", "Passw0rd!")
    time.sleep(0.5)

    # Hapus semua cookies agar session bersih sebelum login
    browser.delete_all_cookies()

    login = LoginPage(browser, base_url)
    login.open()

    try:
        login.login(uname, "Passw0rd!")
        time.sleep(0.5)
        assert "index.php" in browser.current_url
    except Exception:
        # simpan bukti saat gagal
        print("\n=== DEBUG URL ===")
        print(browser.current_url)

        with open("debug_login_page.html", "w", encoding="utf-8") as f:
            f.write(browser.page_source)

        browser.save_screenshot("debug_login_page.png")
        raise
