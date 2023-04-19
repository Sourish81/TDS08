import streamlit as st
import pandas as pd

st.header('Find the Largest Number.')

st.write("""Enter three numbers and find the largest among them

""")
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

def compute_max(a,b,c):
    l=list([a,b,c])
    return max(l)
