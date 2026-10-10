import streamlit as st
if "students" not in st.session_state:
 st.session_state.students = []
with st.form("add"):
 name = st.text_input("Name")
 mark = st.number_input("Mark", min_value=0, max_value=100)
 if st.form_submit_button("Add"):
  ...
if st.session_state.students:
 st.table(...)
 st.metric(...)
