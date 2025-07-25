
def get_static_cyber_incidents():
    incidents = [
        {
            "title": "Data Breach at XYZ Corp",
            "date": "2025-04-04",
            "description": "XYZ Corp experienced a data breach affecting 100,000 users."
        },
        {
            "title": "New Phishing Scam Targets Banks",
            "date": "2025-03-30",
            "description": "Hackers are using fake banking emails to steal user credentials."
        },
        {
            "title": "Ransomware Attack on Healthcare Provider",
            "date": "2025-03-28",
            "description": "A ransomware attack has locked patient records at ABC Health."
        },
        {
            "title": "Zero-Day Exploit Discovered in Windows OS",
            "date": "2025-03-25",
            "description": "A new zero-day vulnerability is being actively exploited in the wild."
        }
    ]
    return incidents

if __name__ == "__main__":
    data = get_static_cyber_incidents()
    for incident in data:
        print(f"Title: {incident['title']}")
        print(f"Date: {incident['date']}")
        print(f"Description: {incident['description']}\n")