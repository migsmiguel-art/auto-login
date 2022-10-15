# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 10:10:12 2022

@author: PACMAN

What does this program do?

This program automates logging into devry

Provide your username and password on lines 19 && 20
"""
# Used to import the webdriver from selenium
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#There is a more secure method to store your password,
#However this is just a proof of concept.
username = "ENTER YOUR D# here"
password = "ENTER YOUR PASSWORD HERE"
 
"""
WHAT YOU NEED TO IN ORDER FOR THIS PROGRAM TO WORK:
    -CHROMEDRIVER
    -SELENIUM(LIBRARY)

1. PIP INSTALL SELENIUM
2. FIND THE VERSION OF YOUR GOOGLE CHROME(GC) AND
   AND DOWNLOAD CHROMEDRIVER VERSION THAT WORKS
   WITH YOUR GC.
   - HERE IS THE LINK TO DOWNLOAD CHROMEDRIVER
   - https://chromedriver.chromium.org/home

3. ONCE YOU HAVE DOWNLOADED CHROMEDRIVER, EXTRACT FILES
4. GET THE PATH OF chromedriver.exe as shown in line# 43 & 44
5. Run the program!
Get the path of chromedriver which you have install
"""

# Note here: on the path there is \\ to navigate to your file.
# Copy this format for your path
# path = "C:\\Users\\your-pc-username\\Downloads\\chrome-folder\\chromedriver.exe"
path = "C:\\Users\\your-pc-username\\Downloads\\chrome\\chromedriver.exe"
     
# giving the path of chromedriver to selenium webdriver
driver = webdriver.Chrome(path)

# URL of the login page of site
# which you want to automate login.
url = "https://learn.devry.edu/login?forwardUrl=%2Fhome"
     
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
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
