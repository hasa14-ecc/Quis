import os
import uuid
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "http://localhost/quiz-pengupil")

@pytest.fixture(scope="session")
def browser():
    opts = Options()
    # Aktifkan headless agar bisa jalan di CI
    opts.add_argument("--headless=new")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    driver.set_window_size(1280, 720)
    yield driver
    driver.quit()
