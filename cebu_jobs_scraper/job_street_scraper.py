import requests
import sys
from bs4 import BeautifulSoup

URL_ROOT = "http://www.jobstreet.com.ph/en/job-search/job-vacancy.php"

def parse_title(soup):
    soup.select("html body .panel-body .header-text h2")

def get_page(url):
    payload = {}
    response = requests.get(url, params=payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.select('#job_listing_panel .panel-body')
    for job in jobs:
        title_selector = '.position-title-link h2'
        title = job.select(title_selector)
        if len(title) > 0: title = title[0].text 
        print(title)

def main():
    get_page(URL_ROOT)
    return 0

if __name__ == '__main__':
    sys.exit(main())
