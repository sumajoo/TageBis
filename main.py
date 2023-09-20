import streamlit as st
import datetime

# Header
st.title("Anki Countdown")

# Subheader
st.caption("Anki Countdown hilft dir, deine Karten bis zur Prüfung zu beenden. Gib einfach die Daten ein und schon kannst du loslegen.")

# Exam date input on sidebar
examdate = st.sidebar.date_input("Prüfungs Datum", datetime.date(2023, 9, 26))

# Start Date input on sidebar
startdate = st.sidebar.date_input("Lernstart", datetime.date(2023, 7, 27))

# Total cards input on sidebar
total_cards = st.sidebar.number_input("Gesamte Karten", 0, 10000, 3821)

# Cards left input on sidebar
cards_left = st.sidebar.number_input("Übrige Karten", 0, total_cards, 384)

# How many days buffer input on sidebar
days_buffer = st.sidebar.number_input("Puffer Tage", 0, 100, 2)

# Free days per week input on sidebar
free_days_per_week = st.sidebar.number_input("Freie Tage pro Woche", 0, 7, 0)

# Days left to exam
days_left = examdate - datetime.date.today()

# Cards done
cards_done = total_cards - cards_left

# free days left
free_days_left = (days_left.days / 7) * free_days_per_week

# cards per day
cards_per_day = cards_left / (days_left.days - free_days_left)

# days till cards finished
days_till_cards_finished = cards_left / cards_per_day + free_days_left

# main view
col1, col2, col3 = st.columns(3)
col1.metric("Tage bis zur Prüfung", days_left.days)
col2.metric("Karten pro Tag", round(cards_per_day, 2))
col3.metric("übrige freie Tage", round(free_days_left, 2))

st.divider()

# detailed view
col1, col2 = st.columns(2)

with col1:
    st.write("fertige Karten: ", cards_done)

with col2:
    st.write("übrige freie Tage: ", round(free_days_left, 2))
