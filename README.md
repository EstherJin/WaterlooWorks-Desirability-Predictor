# Waterloo-Works-Scraping
 
Series of scripts to scrape job listings from WaterlooWorks into a CSV then filter based on companies

scrape.py is the main script, using Selenium to scrape WaterlooWorks data in to a CSV. 

filter.py can then be used to filter results from scrape.py based on a blacklist stored in the plain-text file 'blacklist.txt'. You can edit that file as you wish. The script will also remove any duplicates from 'blacklist.txt'

## Requirements:

- BeautifulSoup
- Selenium
- Progressbar
- Pick

To install all dependencies , simply run 
```pip install -r requirements.txt```
in your  terminal

## Use / Installation

First, clone or download this repository, then navigate to the local repository and run 

```python3 scrape.py```

from a bash terminal.

If on windows you can probably do it from the python IDLE without issue.

Make sure that chromedriver is in the same folder as your script when you run it, as it is required for selenium to run. 

You will be prompted for your WaterlooWorks Login, and then asked if you want to run in headless mode. Note, if you run with the chromium browser showing, you may need to navigate back to the terminal window in order to select a couple options.

Select what category you want to scrape in the Terminal (eg: "For my program", "Applied to", etc.)

Once the script has finished, it will save the list of jobs to output.csv.

To filter your results based on 'blacklist.txt', run 

```python3 filter.py```

in your bash terminal. Again, on windows running from Python IDLE should be fine.


