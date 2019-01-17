#!/usr/bin/env python3



from bs4 import BeautifulSoup
import getpass
import re
from pick import pick
import progressbar
import os
import time
from selenium import webdriver

def main():
    # Get user login information
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    # monk user input
    # username = ''
    # password = ''

    # default co-op url
    dashboard_url = "http://waterlooworks.uwaterloo.ca/myAccount/co-op/coop-postings.htm"
    login_url = 'https://cas.uwaterloo.ca/cas/login?service=https://waterlooworks.uwaterloo.ca/waterloo.htm'
    output_name = 'output.csv'

    # start selenium in chromium 
    chrome_options = webdriver.chrome.options.Options()  
    chrome_options.add_argument("--headless") 

    #Uncomment next bit to make it headless
    browser = webdriver.Chrome(executable_path="./chromedriver")#, chrome_options=chrome_options)

    main_page_html = login(username, password, login_url, dashboard_url, browser)
    # get quick search options from main page content
    quick_search_options = get_quick_search_options(main_page_html)

    choice = prompt_quick_search(quick_search_options)

    # mock user promt
    # choice = 'For My Program'
    

    # peek the first page of the quick search page, get the token and page count
    data = get_job_lists(choice, browser, output_name)

    print("Done!")

def login(username, password, login_url, dashboard_url, browser):

    # log in
    browser.get(login_url)
    user_field = browser.find_element_by_id("username") #username form field
    pass_field = browser.find_element_by_id("password") #password form field
    user_field.send_keys(username)
    pass_field.send_keys(password)

    # click submit
    browser.find_element_by_name("submit").click()

    browser.get(dashboard_url) #navigate to page behind login
    
    # Wait for javascript to run then grab page contents
    time.sleep(3)
    return repr(browser.execute_script("return document.body.innerHTML")) #returns the inner HTML

def get_quick_search_options(main_page_html):

        print("Getting options...")

        # Only get the options that has jobs, exclude those that have 0 job.
        #pattern = r'<td class="full"><a href=".+?:\\\'(.+?)\\\'.+?">(.+?)<\/a><\/td>'     # THIS PATTERN IS WRONG
        pattern = r'<td class="full"><a href=".+?:.+?" onclick=(.+?)>(.+?)<\/a><\/td>'
        
        results = re.findall(pattern, main_page_html)

        quick_search_options = {}
        for result in results:
            key = "".join(re.findall(r'(?<!\\)(?:\w|\s)', result[1])).lstrip().rstrip()
            quick_search_options[key] = result[0]

        return quick_search_options

def prompt_quick_search(quick_search_options):
    message = "Which quick search do you want to crawl? "
    choices = list(quick_search_options)
    choice, index = pick(choices, message)
    return choice

def get_job_lists(choice, browser, output_name):
    
    print("Getting job lists ...")

    # Navigate to the job listings page then wait for the javascript to load
    browser.find_element_by_link_text(choice).click()

    # Get the HTML of the page and check if this is the last page (next_page_buttons)
    page_html = browser.execute_script("return document.body.innerHTML")
    pattern = r'<a href=".+?" onclick="loadPostingTable(.+?)">\s*»\s*<\/a>'
    next_page_buttons = []
    next_page_buttons = re.findall(pattern, page_html)

    print(next_page_buttons)

    # bar = progressbar.ProgressBar(max_value=self.job_lists_page_count)
    # bar.update(self.gather_current_progress)

    # Scrape the tables and save it to output_name as a CSV
    with open(output_name, 'w') as f:
        while (next_page_buttons):
            print("Next Page")

            time.sleep(1)
            soup = BeautifulSoup(page_html, "html.parser")

            for tr in soup.find_all('tr')[2:]:
                tds = tr.find_all('td')
                for x in tds[2:]:
                    f.write( ' '.join(x.text.split()).replace(',', ' ') + ","),
                f.write("\n")

            # navigate to the next page and get the HTML, next page buttons
            browser.find_element_by_link_text("»").click()

            page_html = browser.execute_script("return document.body.innerHTML")
            next_page_buttons = re.findall(pattern, page_html)


if __name__ == "__main__":
    main()

