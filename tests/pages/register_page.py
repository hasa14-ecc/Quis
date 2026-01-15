from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = f"{base_url}/register.php"

    NAME     = (By.XPATH, "//input[@placeholder='Masukkan Nama']")
    EMAIL    = (By.XPATH, "//input[@placeholder='Masukkan email']")
    USERNAME = (By.XPATH, "//input[@placeholder='Masukkan username']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    REPASS   = (By.XPATH, "//input[@placeholder='Re-Password']")
    BTN_REG  = (By.XPATH, "//button[contains(.,'Register')]")
    ALERT    = (By.CSS_SELECTOR, ".alert")

    def open(self):
        self.driver.get(self.url)

    def register(self, name, email, username, password, repass):
        n = self.driver.find_element(*self.NAME)
        e = self.driver.find_element(*self.EMAIL)
        u = self.driver.find_element(*self.USERNAME)
        p = self.driver.find_element(*self.PASSWORD)
        r = self.driver.find_element(*self.REPASS)

        n.clear(); n.send_keys(name)
        e.clear(); e.send_keys(email)
        u.clear(); u.send_keys(username)
        p.clear(); p.send_keys(password)
        r.clear(); r.send_keys(repass)

        self.driver.find_element(*self.BTN_REG).click()

    def alert_text(self):
        els = self.driver.find_elements(*self.ALERT)
        return els[0].text.strip() if els else ""
