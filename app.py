import streamlit as st
import pandas as pd


st.write("""Enter three numbers and find the largest among them

""")

st.header('Find the Largest Number.')

def compute_max(a,b,c):
    l=list([a,b,c])
    return max(l)
