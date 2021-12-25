import requests
from bs4 import BeautifulSoup
import time

print("Enter skill that u are unaware of :")

unknown_skill = input('>')
print(f'Filtering data based on  : {unknown_skill}')

def find_jobs():
    page = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    # print(page)

    # Create a BeautifulSoup object
    soup = BeautifulSoup(page, 'lxml')
    #fine one match for the tag 
    jobs1 = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, jobs in enumerate(jobs1):
        publish_date = jobs.find('span',class_= 'sim-posted').text
        if 'few' in publish_date:
            company_name = jobs.find('h3', class_ = 'joblist-comp-name').text
            more_info = jobs.header.h2.a['href']
        
            skills = jobs.find('span',class_= 'srp-skills').text.replace(' ','' )
            if unknown_skill not in skills:
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Skills : {skills.strip()} \n")
                    f.write(f"Link to Job: {more_info} \n")
                print(f'File saved :{index}.txt')

if __name__ == '__main__':
    while True:
        find_jobs()
        print(f'Waiting for 20 seconds :')
        time.sleep(20)