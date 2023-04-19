import streamlit as st
import pandas as pd

import pickle

st.header('Find the Largest Number.')

st.write("""Enter three numbers and find the largest among them

""")
"""
def user_input_features():
     data={'Enter Number 1': a,
           'Enter Number 2': b,
           'Enter Number 3': c,
          }
     features = pd.DataFrame(data, index=[0])
     return features
df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())
imort streamlit as st 
"""
A=int(input("Enter first number: "))
B=int(input("Enter second number: "))
C=int(input("Enter third number: "))
if (A >= B) and (A >= C):
 largest = A
elif (B >= A) and (B >= C):
 largest = B
else:
 largest = C
print("The largest number between",A,",",B,"and",C,"is",largest)
