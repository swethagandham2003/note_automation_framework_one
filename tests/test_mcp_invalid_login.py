from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from utils.logger import get_logger
from pages.login_page import LoginPage
from config.environment import get_config
from mcp.llm_data_generator import LLMDataGenerator


logger = get_logger(__name__)


def test_mcp_invalid_login(driver):

    config = get_config()

    driver.get(config["base_url"])
    logger.info("Application opened")

    WebDriverWait(driver, 80).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    login = LoginPage(driver)

    # MCP-generated invalid credentials
    random_email = LLMDataGenerator.random_email()
    random_password = "InvalidPassword123"

    logger.info(f"Using invalid email: {random_email}")

    # perform invalid login
    login.login(random_email, random_password)

    logger.info("Login attempted with invalid credentials")

    # verify login failed
    WebDriverWait(driver, 5).until(
        EC.url_contains("login")
    )

    assert "login" in driver.current_url.lower()

    logger.info("Invalid login test passed")