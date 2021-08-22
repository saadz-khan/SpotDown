from selenium import webdriver
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from os import getcwd
from fake_useragent import UserAgent

def download_song(link):
	"""This function is trying to download the songs using selenium setup and """
	#try:
	browser=selenium_setup()
	browser.get("https://ytmp3.cc/en14/")
	browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/form/input[1]").send_keys(link)
	submit = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/form/input[2]")
	submit.click()
	element = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[3]/a[1]")))
	download = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/a[1]')
	download.click()
	browser.close()
	#except:
	print("Download Failed. Trying next song link please wait until complete")


def selenium_setup():
	"""Function works on trying to setup selenium so that download 
	can be made possible through the headless web-driver"""
	options = webdriver.ChromeOptions()
	ua = UserAgent()
	userAgent = ua.random

	# Argument setups for the chrome driver
	options.add_argument(userAgent)
	options.add_argument('--headless')
	options.add_argument('--no-sandbox')
	#options.add_argument('--disable-dev-shm-usage')
	#options.add_argument('--disable-blink-features=AutomationControlled')
	driver = webdriver.Chrome('chromedriver',options=options)

	# Firefox mode for the neccessary for download the files
	fp = webdriver.FirefoxProfile()
	fp.set_preference("browser.download.folderList",2)
	fp.set_preference("browser.download.manager.showWhenStarting",False)
	fp.set_preference("browser.download.dir", os.getcwd())
	fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

	return driver


download_song('https://youtu.be/A66TYFdz8YA')