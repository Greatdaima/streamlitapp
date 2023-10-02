import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "col1": np.random.randn(1000) / 500 + 34.81732,
    "col2": np.random.randn(1000) / 500 + 113.535807,
    "col3": np.random.randn(1000) * 10,
    "col4": np.random.rand(1000, 4).tolist(),
})

st.map(df,
       latitude='col1',
       longitude='col2',
       size='col3',
       color='col4')
