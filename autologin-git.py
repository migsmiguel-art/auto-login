# -*- coding: utf-8 -*-
"""
Spyder Editor

By: Pacman 
"""

# Used to import the webdriver from selenium
from selenium import webdriver 
from selenium.webdriver.common.by import By
# import os
 
# Get the path of chromedriver which you have install
 
def startBot(username, password, url):
    path = "your\\path\\to\\dir\\chromedriver.exe"
     
    # giving the path of chromedriver to selenium webdriver
    driver = webdriver.Chrome(path)
     
    # opening the website  in chrome.
    driver.get(url)
     
    # find the id or name or class of
    # username by inspecting on username input
    driver.find_element("name", "username").send_keys(username)
     
    # find the password by inspecting on password input
    driver.find_element("name", "password").send_keys(password)
     
    # click on submit
    driver.find_element(By.XPATH, '//*[@id="loginButton"]').click()
 
 
# Driver Code
# Enter below your login credentials
username = ""
password = ""
 
# URL of the login page of site
# which you want to automate login.
url = ""
 
# Call the function
startBot(username, password, url)