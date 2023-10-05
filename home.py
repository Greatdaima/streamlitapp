import time
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objs as go

# 设置页面配置
st.set_page_config(page_title="个人展示仓库", page_icon=":chart_with_upwards_trend:",
                   layout="centered",  # centered  wide
                   initial_sidebar_state="expanded")
# 初始化 session_state
if 'pwd' not in st.session_state:
    st.session_state['pwd'] = ''

# woden
with st.container():
    st.write('展示3D图')

    pwd = st.text_input('告诉我密码:')

    # 处理用户输入的密码
    if pwd != '':
        if pwd != st.__name__:
            st.write(pwd + '$你被骗了，哈哈！')
        else:
            st.write('恭喜你，哈哈！')
