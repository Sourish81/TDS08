import streamlit as st
import pandas as pd
from sklearn import datasets

st.write("""
# Find the Largest Number
""")
#Get Input

st.header('Enter three numbers and find the largest among them.')
St.number_input()
#Input 3 numbers

def compute_max(a,b,c):
    l=list([a,b,c])
    return max(l)
st.button("Largest Number")
