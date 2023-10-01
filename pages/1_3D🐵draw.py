import time
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objs as go

st.title('3D散点图')
x, y, z = np.random.multivariate_normal(
    np.array([0, 0, 0]), np.eye(3), 1000).transpose()

fig = go.Figure(data=go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode="markers",
    marker=dict(
        size=5,
        color=z,
        colorscale="Viridis",
        opacity=0.8,
    )
), layout=go.Layout(
    height=650,
    paper_bgcolor='#00f4f0',
))

st.write(fig, use_container_width=True)
