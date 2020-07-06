#made by joldboy69. DO NOT STEAL MY SCRIPT

from selenium import webdriver
import os
import time

times = int(input("Enter the amount of views to add: "))
url = input("Enter the url of adfly link: ")

options = webdriver.ChromeOptions()

options.add_argument("--proxy-server=socks5://127.0.0.1:9050")

for i in range(times):
    os.popen(r'C:\Users\<YOURUSERNAME>\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe')

    browser = webdriver.Chrome(options=options)

    browser.get(url)

    time.sleep(15)

    browser.close()

    os.system("taskkill /F /im tor.exe")
