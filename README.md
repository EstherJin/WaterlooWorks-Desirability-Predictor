# Waterloo-Works-Scraping

Series of scripts to scrape job listings from WaterlooWorks into a CSV then filter based on companies

scrape.py is the main script, using Selenium to scrape WaterlooWorks data in to a CSV.

filter.py can then be used to filter results from scrape.py based on a blacklist stored in the plain-text file 'blacklist.txt'. You can edit that file as you wish. The script will also remove any duplicates from 'blacklist.txt'

## Requirements:

- BeautifulSoup
- Selenium
- Progressbar
- Pick
- ChromeDriver

To install all python dependencies, run  `pip install -r requirements.txt` in your terminal.

Download chromedriver from here: https://chromedriver.chromium.org. put it in the same directory as the `scrape.py` script.

On MacOS, you can alternatively use `brew install chromedriver`

## Use / Installation

### scrape.py

Run scrape.py using `python3 scrape.py`

The browser will open up to the Waterloo WaterlooWorks site. Log in and navigate to "Hire Waterloo Coop". Once you're done, input any character

On Mac, the first time you run the script you will get an error saying the `ChromeDriver cannot be opened as the developer cannot be verified`. Close the prompt, then go to `Settings -> Security & Privacy` and select `Open Anyways`. Rerun the script.

Select what category you want to scrape in the Terminal (eg: "For my program", "Applied to", etc.)

Once the script has finished, it will save the list of jobs to output.csv.

### filter.py

To filter your results based on 'blacklist.txt', run `python3 filter.py`. `blacklist.txt` should specify any companies you do not want to see the postings of
