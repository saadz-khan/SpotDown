from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def download_song(link):
	#try:
		driver = webdriver.Chrome()
		driver.get('https://ytmp3.cc/en14/')
		driver.findElement(By.xpath("//*[@id='input']")).sendKeys(link)
		submit = driver.findElement(By.xpath("//*[@id='submit']"))
		submit.click()
		time.sleep(5)
		driver.close()
	#except:
	#	print("Invalid URL")

download_song('https://youtu.be/A66TYFdz8YA')