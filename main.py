import streamlit as st
import datetime

# Header
st.title("Exam Countdown")

# Subheader
st.caption("This is a simple countdown to my exam. It calculates how many days I have left to my exam and how many days I have left to finish my Anki cards. It also calculates how many days I have left to study for my exam without having to do Anki cards.")

# Exam date
examdate = datetime.date(2023, 9, 27)

# Start Date
startdate = datetime.date(2023, 7, 26)

# Total cards
total_cards = 3772

# Cards left input on sidebar
cards_left = st.sidebar.number_input("Cards left", 0, total_cards, total_cards)

# Cards per day
cards_per_day = 79

# Days left to exam
days_left = examdate - datetime.date.today()

# Cards done
cards_done = total_cards - cards_left

# days till cards finished
days_till_cards_finished = cards_left / cards_per_day

# free days left
free_days_left = days_left.days - days_till_cards_finished

# days just for reviews
days_just_for_reviews = (free_days_left / 2) - 1

# days completely free
days_completely_free = (free_days_left - days_just_for_reviews) - 2 # minus 2 weil drüber minus 1

# main view
col1, col2, col3 = st.columns(3)
col1.metric("Days left", days_left.days)
col2.metric("finished in", round(days_till_cards_finished, 2))
col3.metric("free Days", round(days_completely_free, 2))

st.divider()

# detailed view
col1, col2 = st.columns(2)

with col1:
    st.write("Days left to exam: ", days_left.days)
    st.write("Cards done: ", cards_done)
    st.write("Days till cards finished: ", round(days_till_cards_finished, 2))

with col2:
    st.write("Free days left: ", round(free_days_left, 2))
    st.write("Days just for reviews: ", round(days_just_for_reviews, 2))
    st.write("Days completely free: ", round(days_completely_free, 2))
