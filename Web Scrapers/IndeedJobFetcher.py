## A webscraper that returns the first search results for Software Engineer jobs in Holmdel, NJ.

from bs4 import BeautifulSoup
import re
import urllib
import requests
import datetime

URL = 'https://www.indeed.com/jobs?q=Software+Engineer&l=Holmdel%2C+NJ'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='resultsCol')

currentDate = datetime.datetime.now()


job_elems = results.find_all('div', class_='jobsearch-SerpJobCard unifiedRow row result')

print("List of Indeed Jobs on " + currentDate.strftime("%x") + " near Holmdel, NJ")
print("")

for job_elem in job_elems:
    title = job_elem.find('div', class_='title')
    company = job_elem.find('span', class_='company')
    location = job_elem.find('div', class_='location accessible-contrast-color-location')
    summary = job_elem.find('div', class_='summary')
    if None in (title,company,location,summary):
        continue
    print("Job Title: " + title.text.strip())
    print("Company Name: " + company.text.strip())
    print("Job Location: " + location.text.strip())
    print("Job Description: " + summary.text.strip())
    print()

