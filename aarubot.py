import requests
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

def rasaCaller(message, sender="Rasa1"):
	url = 'http://localhost:5005/webhooks/rest/webhook'
	myobj = {'sender': sender, 'message': message}
	x = requests.post(url, json = myobj)
	res = x.json()
	if len(res) > 0:
		return res[0].get("text")
	else:
		return ""

# Edit the path to the path of chromedriver
driver = webdriver.Chrome("C:/Users/hp/Downloads/chromedriver.exe") 
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 
# target is the whatsapp chat name to which you wish the chatbot should interact with
target = '"Me-Sa-Ar"'
x_arg = '//span[contains(@title,' + target + ')]'
time.sleep(10)
group_title = wait.until(EC.presence_of_element_located(( 
	By.XPATH, x_arg))) 
group_title.click()
prevString = ""
newString = ""
while True:
	buffString = ""
	main = driver.find_elements_by_class_name('_1bR5a')
	time.sleep(2)
	text = [i.text for i in main][-1].split('\n')[0]
	if text!="":
		buffString = text
	if buffString!=newString:
		newString = buffString
		print(newString)
	if newString!="" and newString!=prevString:
		# "Rasa10" is the sender id, change this to Rasa11, Rasa12, etc. aur reinitialize rasa chat server
		result = rasaCaller(newString, "Rasa10")
		if result!="":
			inp_xpath = '//div[@class="_2_1wd copyable-text selectable-text"][@dir="ltr"][@data-tab="6"]'
			input_box = wait.until(EC.presence_of_element_located(( 
				By.XPATH, inp_xpath))) 
			input_box.send_keys(result + Keys.ENTER) 
			time.sleep(1)
		prevString = newString
		newString = result