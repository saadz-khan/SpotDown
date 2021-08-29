from fake_useragent.utils import get
from selenium import webdriver
from fake_useragent import UserAgent
import os

def selenium_setup():
	"""
	Selenium setup with proper argument setup for chrome webdriver
	Args:
	None

	Returns:
	webdriver object (Chrome or Firefox) 
	For firefox uncomment the code below at the end

	"""
	
	options = webdriver.ChromeOptions()
	
	ua = UserAgent()
	userAgent = ua.random

	paren_dir = os.getcwd()
	down_path = os.path.join(paren_dir, 'downloads')
	os.mkdir(down_path)
	# Argument setups for the chrome driver
	options.add_argument(userAgent)
	#options.add_argument('--headless')
	options.add_argument('--no-sandbox')
	options.add_argument('--disable-gpu')
	options.add_experimental_option('excludeSwitches', ['enable-logging'])
	options.add_argument('--disable-dev-shm-usage')
	options.add_argument('--disable-blink-features=AutomationControlled')
	options.add_experimental_option("prefs", {
	"download.default_directory": down_path,
	"download.prompt_for_download": False,
	"download.directory_upgrade": True,
	})
	
	driver = webdriver.Chrome(executable_path='./chromedriver.exe' ,options=options)

	"""For Firefox webdriver use this snippet
	Firefox profile for the neccessary for download the files

	profile = webdriver.FirefoxProfile()
	profile.set_preference("browser.download.folderList",2)
	profile.set_preference("browser.download.manager.showWhenStarting",False)
	profile.set_preference("browser.download.dir", getcwd())
	profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
	driver = webdriver.Firefox(executable_path='<Add_Path>', firefox_profile =profile)
	"""
	return driver