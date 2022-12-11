from googlesearch import search
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def store_links(query):
    links_arr = []
    # store the links in an array
    for link in search(query):
        links_arr.append(link)
    
    # store the text and link in a class 
    class Link:
        def __init__(self, url, text):
            self.url= url
            self.text = text
    
    links_obj_arr = []
    # traverse through the array and get the text    
    for i in range(len(links_arr)):
        # using the request lib and beautiful soup to parse the html
        url = links_arr[i]
        r = requests.get(url)
        site_content = r.text
        soup = BeautifulSoup(site_content, 'html.parser')
        text = soup.get_text()
        links_obj_arr.append(Link(url, text))
        
    for test in range(len(links_obj_arr)):
        print(links_obj_arr[test].url)
    
    return 'success'

# function to automatically cite all the links
def cite_sources(link):    
        print('In function')
        service = ChromeService(executable_path=ChromeDriverManager().install())

        driver = webdriver.Chrome(service=service) # create the webdriver
        driver.get("https://www.easybib.com/mla/website/search-form") # navigating to easybib website
        driver.maximize_window()
        
        # finding the form
        text_box = driver.find_element(by=By.ID, value="search-input") # search for the textbox
        print('text box found')
        search_button = driver.find_element(by=By.CLASS_NAME, value="sc-fzplWN") # search for the submit button
        
        text_box.send_keys(link)
        search_button.click()
        
        print('submit found')
        
        cite_button = driver.find_element(by=By.CLASS_NAME, value='sc-fzplWN')
        cite_button.click()
        
        continue_button = driver.find_element(by=By.CLASS_NAME, value='sc-fzplWN')
        continue_button.click()
        
        complete_button = driver.find_element(by=By.CLASS_NAME, value='sc-fzplWN')
        complete_button.click()
        
        copy_all_button = driver.find_element(by=By.CLASS_NAME, value = 'sc-fzplWN')
        copy_all_button.click()
        print('cite button pressed')
        # display the citations
        with open('citations.txt', 'w') as f:
            f.write('Citations')
        print('Your sources have been copied, please paste them in the citations file')
        driver.quit()
        return "Sources cited"
