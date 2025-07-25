import sqlite3
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Sample categories and related keywords
categories = {
    "phishing": ["phishing", "email scam", "credentials stolen", "fake banking emails"],
    "ransomware": ["ransomware", "encrypt files", "bitcoin ransom", "locked patient records"],
    "malware": ["malware", "trojan", "spyware", "virus", "zero-day vulnerability"],
    "breach": ["data breach", "leak", "user data exposed", "unauthorized access"],
}

def classify_incidents():
    conn = sqlite3.connect("cyber_incidents.db")
    df = pd.read_sql_query("SELECT id, description FROM incidents", conn)
    conn.close()

    if df.empty:
        print("No data available.")
        return

    # Creating training dataset
    texts = []
    labels = []
    for label, keywords in categories.items():
        for kw in keywords:
            texts.append(kw)
            labels.append(label)

    # Train a simple ML model
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(texts, labels)

    # Predict category for each incident
    df["category"] = model.predict(df["description"])

    # Update database with new "category" column if not exists
    conn = sqlite3.connect("cyber_incidents.db")
    cursor = conn.cursor()
    cursor.execute("ALTER TABLE incidents ADD COLUMN category TEXT")  # Add column (ignore error if already added)

    for idx, row in df.iterrows():
        cursor.execute("UPDATE incidents SET category=? WHERE id=?", (row["category"], row["id"]))

    conn.commit()
    conn.close()
    print("Classification completed!")

if __name__ == "__main__":  
    classify_incidents()