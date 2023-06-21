import streamlit as st
from main_page import main_page
from pages.page2 import page2

def run_page(page_function):
    page_function()

pages = {
    "Main page": main_page,
    "Page 2": page2,
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(pages.keys()))

page_function = pages[selection]

run_page(page_function)
