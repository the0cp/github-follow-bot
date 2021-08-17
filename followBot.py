########################################################################
# You need a Github account, python, Chrome and a boring brain(nonsense)
#---------------------------------------------------------------
# You need selenium to run.
# So install it: pip install selenium
########################################################################
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Initializing
options = Options()

# This is where your chrome located, changed it if you installed chrome in another location.
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

driver = webdriver.Chrome(chrome_options = options, executable_path=r'.\chromedriver.exe')

driver.get("https://github.com/login")
wait = WebDriverWait(driver, 10)

username = wait.until(EC.presence_of_element_located((By.ID, "login_field")))
password = wait.until(EC.presence_of_element_located((By.ID, "password")))

# Your Github username and password, please input correctly
username.send_keys("username")
password.send_keys("password")

login_form = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='Sign in']")))
login_form.click()

nameOfUser = "theodorecooper" 
# Input github username here, the script will first bulk follow this guy's followers

driver.get("https://github.com/{}?tab=followers".format(nameOfUser))
time.sleep(3)

users = driver.find_elements_by_xpath("//a[@data-hovercard-type='user']")
temp = []
for follower in users:
    temp.append(follower.get_attribute("href"))
list_set = set(temp) 
followers = (list(list_set))

# Start spamming
for user in followers:
    for page in range(1, 5):
        string = "{}?page={}&tab=following".format(user, page)
        driver.get(string)
        time.sleep(3)

        follow_button = driver.find_elements_by_xpath("//input[@aria-label='Follow this person']")

        try:
            for i in follow_button:
                i.submit()
        except:
            pass

driver.close() #close this f**king script.
