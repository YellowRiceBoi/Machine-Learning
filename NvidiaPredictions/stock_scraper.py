from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_stock_price():
    options = Options()
    #options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://finance.yahoo.com/quote/NVDA")

        wait = WebDriverWait(driver, 15)

        # Accept cookies if the popup appears
        try:
            consent_button = wait.until(
                EC.element_to_be_clickable((By.NAME, "agree"))
            )
            consent_button.click()
            print("✅ Accepted cookies")
        except:
            print("⚠️ No cookie popup found (maybe already accepted)")

        # Wait for stock price to load
        price_el = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="qsp-price"]'))
        )

        change_el = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="qsp-price-change"]'))
        )

        return {
            "price": price_el.text,
            "change_today": change_el.text
        }

    finally:
        driver.quit()

# Run the function
print(scrape_stock_price())