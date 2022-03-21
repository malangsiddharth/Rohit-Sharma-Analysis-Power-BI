from selenium import webdriver
import pandas as pd
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options,executable_path="C:\\chromedriver.exe")
driver.maximize_window()
time.sleep(5)
driver.get('http://www.howstat.com/cricket/Statistics/Players/PlayerOverviewSummary.asp?PlayerID=3474')
driver.find_element_by_partial_link_text("Detailed IPL Profile & Statistics").click()


driver.find_element_by_partial_link_text("Career Innings - Batting (Detailed)").click()
rows=len(driver.find_elements_by_xpath("//table[@class='TableLined']//tr"))
print(rows)

column=len(driver.find_elements_by_xpath("//table[@class='TableLined']//tr[4]/td"))
print(column)

#print(driver.find_element_by_xpath("//table[@class='TableLined']//tr[4]/td[2]").text)

l=[]
for i in range(4,rows):
	l1=[]

	for j in range(1,column+1):
		l1.append(driver.find_element_by_xpath("//table[@class='TableLined']//tr["+str(i)+"]/td["+str(j)+"]").text)
		#print(i," ",j)
		print(driver.find_element_by_xpath("//table[@class='TableLined']//tr["+str(i)+"]/td["+str(j)+"]").text)
	l.append(l1)

print(l)
import csv
	
# field names
fields = ['Id','Date','Versus','Ground','D/N','How Dismissed','Runs','B/F','S/R',' ','Aggr','Avg','S/R']

filename = "Rohit_Sharma_IPL.csv"
	
# writing to csv file
with open(filename, 'w',newline='', encoding="utf-8") as csvfile:
	# creating a csv writer object
	csvwriter = csv.writer(csvfile)
		
	# writing the fields
	csvwriter.writerow(fields)
		
	# writing the data rows
	csvwriter.writerows(l)



