Cybersecurity Incident Tracking System Features

Web Scraping: Extracts cybersecurity incident data from reliable sources. Machine Learning Classification: Uses TF-IDF + Naive Bayes to categorize incidents into types like Phishing, Ransomware, Malware. SQLite Storage: Stores all incidents and predictions in a persistent local database. Insights Generation: Aggregates incident data by type. Streamlit Dashboard: User-friendly frontend for displaying incidents and insights interactively. README.md You're here!

Setup Instructions

Clone the Repository
bash git clone https://github.com/shruthiaddagudi/T230_Hackathoncd cybersecurity-tracker

Create a Virtual Environment
bash python -m venv venv source venv/bin/activate # On Windows: venv\Scripts\activate

Install Requirements
bash pip install -r requirements.txt

Run the Pipeline

Scrape data python scraper.py

Store data python database.py

Classify incidents python ml_classification.py

Generate insights (optional) python insights.py

Run Streamlit app streamlit run app.py

System Architecture - Website Scraper ──▶ SQLite DB ──▶ ML Classifier ──▶ Insights Generator ──▶ Streamlit UI Each stage feeds the next, making this a complete ETL + ML visualization pipeline for cybersecurity events.
