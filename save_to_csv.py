import csv

def save_to_csv(jobs):
    file = open("jobs.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "job_type", "apply_link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return