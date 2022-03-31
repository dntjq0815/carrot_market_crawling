import requests
from bs4 import BeautifulSoup

URL = f"https://team.daangn.com/jobs/"

def extract_job(html):
    title = html.find("h3").text
    company, job_type = html.find("div", {"class": "c-kEJcFZ"}).find_all("div")
    company = company.get_text()
    job_type = job_type.get_text()
    job_id = html.find("a")["href"]
    return {'title': title,
            'company': company,
            'job_type': job_type,
            'apply_link': f"https://team.daangn.com{job_id}"}


def extract_jobs():
    jobs = []
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("li", {"class": "c-deAcZv"})
    for result in results:
        job = extract_job(result)
        jobs.append(job)
    return jobs

def get_jobs():
    jobs = extract_jobs()
    return jobs