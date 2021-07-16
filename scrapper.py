from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests

import json

def loadDriver():
    try:
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        #chrome_options.add_argument("--no-sandbox")
        #chrome_options.add_argument("disable-gpu")
        chrome_options.add_argument("window-size=1500, 700")
        #chrome_options.add_argument("--user-data-dir=./infografia_profile")
        driver = webdriver.Chrome(executable_path='./drivers/chromedriver', options=chrome_options)
        #driver = webdriver.Firefox()
        driver.get("https://www.google.com")
        print("Driver cargado")
        sleep(10)
        return driver
    except KeyboardInterrupt:
        exit()
        x=1/0
    except Exception as e:
        print("Error while initializing driver")
        print(e)
        x=1/0
        return []

def loadNews(driver, query):
	driver.get(query)
	news = []
	solid_news = driver.find_elements_by_tag_name("g-card")
	for sn in solid_news:
		title = sn.find_elements_by_xpath('.//*[@class="JheGif nDgy9d"]')
		description = sn.find_elements_by_xpath('.//*[@class="Y3v8qd"]')
		time = sn.find_elements_by_xpath('.//*[@class="WG9SHc"]')
		img = sn.find_elements_by_xpath('.//img[@height="112"]')
		src = sn.find_elements_by_xpath('.//*[@class="XTjFC WF4CUc"]')
		url = sn.find_elements_by_xpath('.//a')[0].get_attribute('href')
		if(len(title)==0):
			print("Excluded beacuse of title")
			continue
			#print(title[0].text)
		if(len(description)==0):
			print("Excluded beacuse of description")
			continue
			#print(description[0].text)
		if(len(time)==0):
			print("Excluded beacuse of time")
			continue
			#print(time[0].text)
		if(len(img)==0):
			print("Excluded beacuse of img", title[0].text)
			continue
		if(len(src)==0):
			src=""
		else:
			src = src[0].text
		new = {
			"title" : title[0].text,
			"description" : description[0].text,
			"time" : time[0].text,
			"img" : img[0].get_attribute("src"),
			"src" : src,
			"url" : url
		}
		news.append(new)
	return news
def main():
	beans_query = 'https://www.google.com/search?igu=1&ei=&lr=lang_en&q=(CGIAR+OR+"Africa+Rice+Center"+OR+CIFOR+OR+ICARDA+OR+ICRISAT+OR+IFPRI+OR+IITA+OR+ILRI+OR+CIMMYT+OR+CIP+OR+IRRI+OR+IWMI+OR+Bioversity+OR+CIAT+OR+"World+Agroforestry"+OR+ICRAF+OR+WorldFish)+AND+(frejol+OR+frijol+OR+phaseolus+OR+frejol)&rlz=1C1CHBF_enCO920CO920&tbm=nws&sxsrf=ALeKk02RKFVlYZDHreEzANSw2d6ib5cf_w:1620406855719&source=lnt&sa=X&ved=0ahUKEwjQ9pr4hbjwAhUPTjABHQBWBKIQpwUIKg&biw=1920&bih=880&dpr=1&tbas=0'
	musa_query = 'https://www.google.com/search?igu=1&ei=&lr=lang_en&q=(CGIAR+OR+"Africa+Rice+Center"+OR+CIFOR+OR+ICARDA+OR+ICRISAT+OR+IFPRI+OR+IITA+OR+ILRI+OR+CIMMYT+OR+CIP+OR+IRRI+OR+IWMI+OR+Bioversity+OR+CIAT+OR+"World+Agroforestry"+OR+ICRAF+OR+WorldFish)+AND+(bananas+OR+bananos+OR+banana+OR+musa)&rlz=1C1CHBF_enCO920CO920&tbm=nws&sxsrf=ALeKk02RKFVlYZDHreEzANSw2d6ib5cf_w:1620406855719&source=lnt&sa=X&ved=0ahUKEwjQ9pr4hbjwAhUPTjABHQBWBKIQpwUIKg&biw=1920&bih=880&dpr=1&tbas=0'
	cassava_query = 'https://www.google.com/search?igu=1&ei=&lr=lang_en&q=(CGIAR+OR+"Africa+Rice+Center"+OR+CIFOR+OR+ICARDA+OR+ICRISAT+OR+IFPRI+OR+IITA+OR+ILRI+OR+CIMMYT+OR+CIP+OR+IRRI+OR+IWMI+OR+Bioversity+OR+CIAT+OR+"World+Agroforestry"+OR+ICRAF+OR+WorldFish)+AND+(cassava+OR+yuca+OR+manihot+OR+mandioca)&rlz=1C1CHBF_enCO920CO920&tbm=nws&sxsrf=ALeKk02RKFVlYZDHreEzANSw2d6ib5cf_w:1620406855719&source=lnt&sa=X&ved=0ahUKEwjQ9pr4hbjwAhUPTjABHQBWBKIQpwUIKg&biw=1920&bih=880&dpr=1&tbas=0'
	rice_query = 'https://www.google.com/search?igu=1&ei=&lr=lang_en&q=(CGIAR+OR+"Africa+Rice+Center"+OR+CIFOR+OR+ICARDA+OR+ICRISAT+OR+IFPRI+OR+IITA+OR+ILRI+OR+CIMMYT+OR+CIP+OR+IRRI+OR+IWMI+OR+Bioversity+OR+CIAT+OR+"World+Agroforestry"+OR+ICRAF+OR+WorldFish)+AND+(arroz+OR+rice)&rlz=1C1CHBF_enCO920CO920&tbm=nws&sxsrf=ALeKk02RKFVlYZDHreEzANSw2d6ib5cf_w:1620406855719&source=lnt&sa=X&ved=0ahUKEwjQ9pr4hbjwAhUPTjABHQBWBKIQpwUIKg&biw=1920&bih=880&dpr=1&tbas=0'
	
	driver = loadDriver()
	API_KEY = "$2b$10$X0kbxQICfdAyqkQCj6Lv3ugD2uvhllWkbr8mywZyx5s5llC9nbxCy"
	
	bean_news = loadNews(driver, beans_query)
	beans_id = "60e0b73755b7245a20d4ba71"
	url = 'https://api.jsonbin.io/v3/b/'+beans_id
	headers = {
		'Content-Type': 'application/json',
		'X-Master-Key': API_KEY
	}
	data = bean_news
	req = requests.put(url, json=data, headers=headers)
	print(req.text)
	
	musa_news = loadNews(driver, musa_query)
	
	musa_id="60e0b9af55b7245a20d4bba9"
	
	url = 'https://api.jsonbin.io/v3/b/'+musa_id
	headers = {
		'Content-Type': 'application/json',
		'X-Master-Key': API_KEY
	}
	data = musa_news
	req = requests.put(url, json=data, headers=headers)
	print(req.text)
	
	cassava_news = loadNews(driver, cassava_query)
	cassava_id="60e0b9c755b7245a20d4bbb7"
	
	url = 'https://api.jsonbin.io/v3/b/'+cassava_id
	headers = {
		'Content-Type': 'application/json',
		'X-Master-Key': API_KEY
	}
	data = cassava_news
	req = requests.put(url, json=data, headers=headers)
	print(req.text)
	
	rice_news = loadNews(driver, rice_query)
	rice_id="60f20973c1256a01cb70e79a"
	
	url = 'https://api.jsonbin.io/v3/b/'+rice_id
	headers = {
		'Content-Type': 'application/json',
		'X-Master-Key': API_KEY
	}
	data = rice_news
	req = requests.put(url, json=data, headers=headers)
	print(req.text)
	"""
	with open("./microservice/scrapping_data/bean_news.json", "w") as write_file:
		json.dump(bean_news, write_file)
	sleep(5)
	musa_news = loadNews(driver, musa_query)
	with open("./microservice/scrapping_data/musa_news.json", "w") as write_file:
		json.dump(musa_news, write_file)
	sleep(5)
	cassava_news = loadNews(driver, cassava_query)
	with open("./microservice/scrapping_data/cassava_news.json", "w") as write_file:
		json.dump(cassava_news, write_file)
	sleep(5)
	"""

main()
