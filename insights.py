import sqlite3

def generate_insights():
    conn = sqlite3.connect("cyber_incidents.db")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT COUNT(*), category FROM incidents GROUP BY category")
        insights = cursor.fetchall()

        print("\n📊 Cyber Incident Categories Breakdown:")
        for count, category in insights:
            print(f"Category: {category}, Incidents Reported: {count}")
    except sqlite3.OperationalError as e:
        print("Error: Make sure incidents have been classified and 'category' column exists.")
        print("Details:", e)
    finally:
        conn.close()

if __name__ == "__main__":  
    generate_insights()