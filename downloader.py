from selenium_setup import selenium_setup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from os import getcwd
from time import sleep


def download_multiple_song(links):
	"""
	Downloads multiple songs using the selenium_setup function for webdriver object
	Args:
	links(list): Youtube vido links list from using the spotify-api and youtube data-api v3
	Result:
	Download multiple songs in the current working directory
	
	"""

	browser=selenium_setup()
	browser.get("https://ytmp3.cc/en14/")
	for item in links:
		try:
			browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/form/input[1]").send_keys(item)
			submit = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/form/input[2]")
			submit.click()
			
			# Waiting for the download button to appear
			element = WebDriverWait(browser, 50).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[3]/a[1]")))
			download = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/a[1]')
			download.click()

			# Convert Next Button
			conv_next= browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/a[3]')
			conv_next.click()
			print('Started download for ', item)
		except:
			print("Download Failed. Trying next song-link please wait until complete")

	# waits for all the files to be completed and returns the paths
	paths = WebDriverWait(browser, 120, 1).until(download_complete_check)
	
	

def download_song(link):
	"""
	Download a song using the selenium_setup function for webdriver object
	Args:
	link (str): Youtube video link from using the spotify-api
	
	Result:
	Downloads a song in the current working directory	
	
	"""
	#try:
	browser=selenium_setup()
	browser.get("https://ytmp3.cc/en14/")

	browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/form/input[1]").send_keys(link)
	submit = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/form/input[2]")
	submit.click()
	element = WebDriverWait(browser, 50).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[3]/a[1]")))
	download = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/a[1]')
	download.click()

	# waits for all the files to be completed and returns the paths
	paths = WebDriverWait(browser, 120, 1).until(download_complete_check)
	print('Download Completed')
	#except:
		#print("Download Failed. Trying next song-link please wait until complete")


def download_complete_check(driver):
	"""
	This checks the download list and waits for all the downloads to complete 
	and then closes the webdriver.
	Args:
	driver (object): Webdriver object from selenium.webdriver

	"""
	if not driver.current_url.startswith("chrome://downloads"):
		driver.get("chrome://downloads/")
	return driver.execute_script("""
	var items = document.querySelector('downloads-manager')
		.shadowRoot.getElementById('downloadsList').items;
	if (items.every(e => e.state === "COMPLETE"))
		return items.map(e => e.fileUrl || e.file_Url);
	""")
# Sample Script	
#download_song('https://youtu.be/-Z0Im1SaWik')