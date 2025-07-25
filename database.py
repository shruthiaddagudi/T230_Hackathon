import sqlite3
from scraper import get_static_cyber_incidents  


def store_data(incidents):
    conn = sqlite3.connect("cyber_incidents.db")  
    cursor = conn.cursor()

   
    cursor.execute('''CREATE TABLE IF NOT EXISTS incidents (
                      id INTEGER PRIMARY KEY, 
                      title TEXT, 
                      date TEXT, 
                      description TEXT)''')

    
    for incident in incidents:
        cursor.execute("INSERT INTO incidents (title, date, description) VALUES (?, ?, ?)",
                       (incident["title"], incident["date"], incident["description"]))

    conn.commit()  
    conn.close()   
    print("Data stored successfully!")

if __name__ == "__main__":
    incidents = get_static_cyber_incidents()  
    store_data(incidents)  