import streamlit as st
import pandas as pd
import sqlite3
import os
import urllib.parse
from datetime import datetime
import plotly.express as px

# --- 1. لوگو کا لنک اور سیٹنگز ---
LOGO_URL = "https://raw.githubusercontent.com/Gemini-User/Dpowered/main/1000313964.jpg" # آپ کا لوگو
DB_FILE = "dpowered_solar_master.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, inv REAL)')
    c.execute('CREATE TABLE IF NOT EXISTS referrals (id INTEGER PRIMARY KEY, referrer_id INTEGER, ref_name TEXT, status TEXT)')
    conn.commit()
    conn.close()

init_db()

# --- 2. ایپ کا ڈیزائن ---
st.set_page_config(page_title="Dpowered Solar AI", layout="wide")

# ہر جگہ لوگو دکھانے کے لیے
st.sidebar.image(LOGO_URL, width=150)
st.sidebar.title("Dpowered Solar AI")
st.image(LOGO_URL, width=100)

menu = st.sidebar.radio("Navigate", ["📊 کسٹمر ڈیش بورڈ", "🔐 ایڈمن پینل"])

if menu == "📊 کسٹمر ڈیش بورڈ":
    st.header("🔍 آپ کا سولر سسٹم")
    c_id = st.text_input("آئی ڈی درج کریں", type="password")
    if c_id:
        st.success("خوش آمدید! آپ کا ڈیش بورڈ تیار ہے۔")
        st.info("🎁 ریفرل آفر: اپنے دوست کو ریفر کریں اور 30% رعایت پائیں۔")

elif menu == "🔐 ایڈمن پینل":
    st.header("⚙️ ایڈمن کنٹرول")
    if st.sidebar.text_input("پاس ورڈ", type="password") == "admin786":
        st.write("ایڈمن لاگ ان کامیاب!")
