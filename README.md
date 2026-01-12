# 🤖 AI Autonomous Job Hunter

> **An intelligent, fully autonomous agent that scrapes job boards, filters for visa/tech eligibility, and generates tailored application kits using GPT-4.**

![Python](https://img.shields.io/badge/Python-3.11-blue) ![OpenAI](https://img.shields.io/badge/AI-GPT--4-green) ![Automation](https://img.shields.io/badge/Status-Autonomous-orange)

## 🚀 Overview

The **AI Job Hunter** is an automation pipeline designed to solve the "volume vs. quality" problem in modern job hunting. Instead of manually scrolling through hundreds of irrelevant listings, this agent:

1.  **Wakes up daily** via Windows Task Scheduler.
2.  **Scrapes** major job boards (Indeed, LinkedIn, Glassdoor) for specific technical roles.
3.  **Filters** noise (removes "Citizenship Required" clearance jobs, non-technical roles, and scams).
4.  **Analyzes** the remaining descriptions using **GPT-4** to determine fit for an International MS AI Student (CPT/OPT).
5.  **Generates** a custom "Application Kit" (Tailored Resume Bullets, Cover Letter, Strategy) for every valid lead.
6.  **Emails** a daily report with attachments to the user.

## ✨ Key Features

* **🛡️ Smart "Title Guard":** Prevents applying to irrelevant roles (e.g., filters out "Sales", "Wedding Planner", "Technician") even if they match keywords.
* **🛂 Visa Safety Checks:** Automatically discards jobs requiring "US Citizenship Only" or "Security Clearance" to protect international applicants.
* **🧠 GPT-4 Resume Tailoring:** Reads the Job Description (JD) and rewrites professional summary and bullet points to match the JD's keywords (ATS Optimization).
* **📧 Automated Reporting:** Sends a daily digest email with Word Document attachments (`.docx`) ready for submission.
* **🔍 Multi-Source Scraping:** Aggregates data from Indeed, LinkedIn, and more using `python-jobspy`.

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/AI-Job-Hunter.git](https://github.com/YOUR_USERNAME/AI-Job-Hunter.git)
cd AI-Job-Hunter
2. Install Dependencies
Bash

pip install -r requirements.txt
3. Configuration
Open master_job_hunter.py and update the Configuration Section:

Python

# API Keys
API_KEY = "sk-..."              # Your OpenAI API Key
EMAIL_SENDER = "me@gmail.com"   # Your Gmail
EMAIL_PASSWORD = "xxxx..."      # Your App Password (Not Login Password)
EMAIL_RECEIVER = "me@hotmail.com"

# Search Parameters
LOCATION = "United States"
JOBS_TO_SCRAPE = 20
SEARCH_TERM = 'title:(("AI" OR "Machine Learning" OR "Deep Learning") AND "Intern")'
⚙️ How It Works
The system operates in a linear pipeline:

Scraper Engine: Uses HTTP requests (not Selenium) to scrape job aggregators quickly.

Pre-Filter (The Gatekeeper):

Input: 100+ raw jobs.

Logic: Discards duplicates, blocked companies, and non-tech titles.

Output: ~10-15 relevant candidates.

AI Analyst (The Brain):

Input: Job Description + User's Master Resume.

Action: GPT-4 evaluates "Fit Score" (0-100) and writes a strategy.

Output: JSON object with tailored content.

Document Generator: Creates a .docx file for each approved job.

Notification: SMTP server emails the batch to the user.

🤖 Automation (Windows)
To run this autonomously every morning:

Open Windows Task Scheduler.

Create a Basic Task (Trigger: Daily @ 8:00 AM).

Action: Start a Program.

Program: path/to/python.exe

Arguments: path/to/master_job_hunter.py

Start in: path/to/project_folder

Enable "Wake computer to run this task" in the Conditions tab.

📄 License
This project is open-source under the MIT License.

Built by Edgar Pfuma | MS Artificial Intelligence 2026