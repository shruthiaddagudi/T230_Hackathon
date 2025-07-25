import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Cybersecurity Incidents", layout="wide")
st.title("🛡 Cybersecurity Incidents Dashboard")


def load_data():
    conn = sqlite3.connect("cyber_incidents.db")
    df = pd.read_sql_query("SELECT * FROM incidents ORDER BY date DESC", conn)
    conn.close()
    return df


df = load_data()


if df.empty:
    st.warning("⚠ No incidents found in the database. Please run the scraper and classifier scripts.")
else:
    st.subheader("📋 Incident Table")
    st.dataframe(df, use_container_width=True)

    st.subheader("📊 Incidents by Category")
    if 'category' in df.columns:
        category_counts = df['category'].value_counts()
        st.bar_chart(category_counts)
    else:
        st.info("No categories found. Please run the ML classification module.")