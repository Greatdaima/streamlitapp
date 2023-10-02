import time
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objs as go

# 设置页面配置
st.set_page_config(page_title="个人展示仓库", page_icon=":chart_with_upwards_trend:",
                   layout="centered",  # centered  wide
                   initial_sidebar_state="expanded")

st.header('这是首页')


def draw_scatter3d():

    x, y, z = np.random.multivariate_normal(
        np.array([0, 0, 0]), np.eye(3), 5000).transpose()

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
        paper_bgcolor='#00f4f0',
    ))

    st.write(fig, use_container_width=True)


with st.container():
    st.write('展示3D图')

    draw_scatter3d()

with st.expander('这是后面的内定', expanded=True):
    draw_scatter3d()
