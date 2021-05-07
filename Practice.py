import requests
from bs4 import BeautifulSoup
import pandas as pd


def extract(page):
    header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    url = f'https://in.indeed.com/jobs?q=Python+Developer&l=Bangalore&start={page}'
    r = requests.get(url, header)
    soup = BeautifulSoup(r.content,'html.parser')
    return soup


def transform(soup):
    divs = soup.find_all('div', class_ = "jobsearch-SerpJobCard")
    for item in divs:
        title = item.find('a').text.strip()

        company = item.find('span', class_ ='company').text.strip()

        summary = item.find('div', class_ ='summary').text.strip().replace('\n', '')

        # using try & except since salary is not mentioned for each job listing
        try:
            salary = item.find('span', class_ = 'salaryText' ).text.strip()

        except:
            salary = ''

        # we create a dcitionary to ctore the above values
        jobs = {
            'title' : title,
            'company' : company,
            'summary' : summary,
            'salary' : salary
        }
        joblist.append(jobs)

    return


joblist = []
#range 0 to 40 in 10s
for i in range(0,40, 10):
    print(f'Getting page {i}')
    c = extract(0)
    transform(c)
df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('jobs.csv')