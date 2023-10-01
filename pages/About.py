import time
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objs as go
# 设置页面配置
st.set_page_config(page_title="我的论文", page_icon=":chart_with_upwards_trend:",
                   layout="centered",  # centered  wide
                   initial_sidebar_state="expanded")

views = ['首页', '表格', '画图']
# 在侧边栏显示视图选择框
selection = st.sidebar.radio('导航', views)

# 根据选择的视图展示不同的内容
if selection == '首页':
    st.title('这是ABOUT中的首页')

elif selection == '表格':
    st.title('这是表格页面')
    df = pd.DataFrame(
        [
            {"command": "st.selectbox", "rating": 4, "is_widget": True},
            {"command": "st.balloons", "rating": 5, "is_widget": False},
            {"command": "st.time_input", "rating": 3, "is_widget": True},
        ]
    )
    edited_df = st.data_editor(
        df, num_rows="command", use_container_width=True)

else:
    st.title('画图')
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
