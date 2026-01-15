from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = f"{base_url}/login.php"
        self.wait = WebDriverWait(driver, 10)

    # Locator lebih fleksibel:
    # - cari input username berdasarkan name/id umum ATAU placeholder yang mungkin beda
    USERNAME = (By.XPATH, "//input[@name='username' or @id='username' or contains(@placeholder,'username') or contains(@placeholder,'Username')]")
    PASSWORD = (By.XPATH, "//input[@type='password' or @name='password' or contains(@placeholder,'Password') or contains(@id,'Password')]")

    # Tombol sign in bisa button atau input submit
    BTN_SIGNIN = (By.XPATH, "//button[@type='submit' and @name='submit']")

    ALERT = (By.CSS_SELECTOR, ".alert")

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        print('DEBUG: Current URL:', self.driver.current_url)
        print('DEBUG: Page source snippet:', self.driver.page_source[:500])
        try:
            u = self.wait.until(EC.presence_of_element_located(self.USERNAME))
        except Exception as e:
            print('ERROR: Username field not found:', e)
            raise
        try:
            p = self.wait.until(EC.presence_of_element_located(self.PASSWORD))
        except Exception as e:
            print('ERROR: Password field not found:', e)
            raise

        u.clear(); u.send_keys(username)
        p.clear(); p.send_keys(password)

        try:
            btn = self.wait.until(EC.element_to_be_clickable(self.BTN_SIGNIN))
        except Exception as e:
            print('ERROR: Login button not clickable:', e)
            raise
        btn.click()

    def alert_text(self):
        els = self.driver.find_elements(*self.ALERT)
        return els[0].text.strip() if els else ""
