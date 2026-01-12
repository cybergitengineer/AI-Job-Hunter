import csv
from jobspy import scrape_jobs

# 1. Define your search criteria
jobs = scrape_jobs(
    site_name=["indeed", "linkedin"],
    search_term="AI Engineer",
    location="Dallas, TX",
    results_wanted=20,  # Be careful with high numbers (keep <50 to avoid bans)
    hours_old=72,       # Only jobs posted in the last 3 days
    country_indeed='USA'
)

# 2. Display results
print(f"Found {len(jobs)} jobs")
print(jobs.head())

# 3. Save to CSV for your Resume Optimizer
jobs.to_csv("jobs.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)
print("Saved to jobs.csv")