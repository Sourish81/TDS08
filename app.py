import streamlit as st
import pandas as pd

st.header('Find the Largest Number.')

st.write("""Enter three numbers and find the largest among them

""")



def compute_max(a,b,c):
    l=list([a,b,c])
    return max(l)
