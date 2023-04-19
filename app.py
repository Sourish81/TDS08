import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle


st.header('Enter three numbers and find the largest among them.')

def compute_max(a,b,c):
    l=list([a,b,c])
    return max(l)
