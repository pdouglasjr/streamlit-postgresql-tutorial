# app.py

import streamlit as st

# Initialize connection
conn = st.connection("postgresql", type="sql")

print(conn)