from fake_useragent.utils import get
from selenium import webdriver
from fake_useragent import UserAgent
import os
import wget
import zipfile

def extract_chrome_version(output):
    try:
        google_version = ''
        for letter in output[output.rindex('DisplayVersion    REG_SZ') + 24:]:
            if letter != '\n':
                google_version += letter
            else:
                break
        return(google_version.strip())
    except TypeError:
        return


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
	
	try:	
		driver = webdriver.Chrome(executable_path='./chromedriver.exe' ,options=options)
	except:
		stream = os.popen('reg query "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Google Chrome"')
		output = stream.read()
		chrome_version = extract_chrome_version(output)

		# build the download url
		download_url = "https://chromedriver.storage.googleapis.com/" + chrome_version +"/chromedriver_win32.zip"

		# download the zip file using the url built above
		latest_driver_zip = wget.download(download_url,'./chromedriver.zip')

		# extract the zip file
		with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
			zip_ref.extractall() # you can specify the destination folder path here
		
		# delete the zip file downloaded above
		os.remove(latest_driver_zip)
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