import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

UP_SPEED = 40
DOWN_SPEED = 40
EMAIL = "Your Email"
PASS = "Password"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-dev-shm-usage")
chrome_options.add_argument("no-sandbox")
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("disable-blink-features=AutomationControlled")

chrome_driver_path = "C:\dev\chromedriver.exe"
service = Service(chrome_driver_path)


class InternetSpeedTwitterBot:

    def __init__(self, services, options):
        self.driver = webdriver.Chrome(service=services, options=options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(1)
        tos_popup = self.driver.find_element(By.XPATH, '//*[@id="onetrust-close-btn-container"]/button')
        tos_popup.click()
        go_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        time.sleep(5)
        go_button.click()
        time.sleep(50)
        self.down = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.up = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        try:
            self.driver.get("https://twitter.com/i/flow/login")
            time.sleep(3)
            username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
            username.send_keys(EMAIL)
            time.sleep(2)
            next_key = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
            next_key.click()
            time.sleep(2)
            password = self.driver.find_element(By.XPATH,
                                                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(PASS)
            time.sleep(3)
            log_in = self.driver.find_element(By.XPATH,
                                              '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
            log_in.click()
        except:
            time.sleep(2)
            authentication = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            authentication.send_keys("TwitRepB")
            time.sleep(2)
            next_next = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
            next_next.click()
            time.sleep(2)
            password = self.driver.find_element(By.XPATH,
                                                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(PASS)
            time.sleep(3)
            log_in = self.driver.find_element(By.XPATH,
                                              '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
            log_in.click()
        finally:
            time.sleep(5)
            self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]').click()
            time.sleep(1)
            tweet_text = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
            tweet_text.send_keys(f"WOW! My Airtel is giving {self.down}mbps download/{self.up}mbps upload speed!")
            time.sleep(1)
            tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
            tweet.click()


bot = InternetSpeedTwitterBot(service, chrome_options)
bot.get_internet_speed()
bot.tweet_at_provider()

