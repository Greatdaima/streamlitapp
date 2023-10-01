import streamlit as st
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import plotly.graph_objs as go

st.set_page_config(page_title="3D爱心散点图",
                   page_icon=":heart:", layout='centered')

# 太卡了，不对劲


def draw_heart():
    # start generating points
    x_lim = np.linspace(-10, 10, 1000)
    y_lim = np.linspace(-10, 10, 1000)
    z_lim = np.linspace(-10, 10, 1000)
    X_points = []  # 用来存放绘图点X坐标
    Y_points = []  # 用来存放绘图点Y坐标
    Z_tmp = []
    Z_points = []  # 用来存放绘图点Z坐标
    for y in y_lim:
        for x in x_lim:
            for z in z_lim:
                k = (x**2+(9/4)*y**2+z**2-1)**3-(9/80)*y**2*z**3-x**2*z**3
                if k <= 0:
                    Z_tmp.append(z)
                    if y <= -0.55 or y >= 0.55:
                        X_points.append(x)
                        Y_points.append(y)
                        Z_points.append(z)
            if Z_tmp:
                X_points.append(x)
                Y_points.append(y)
                Z_points.append(max(Z_tmp))
                X_points.append(x)
                Y_points.append(y)
                Z_points.append(min(Z_tmp))
                Z_tmp.clear()

    fig = go.Figure(data=go.Scatter3d(
        x=X_points,
        y=Y_points,
        z=Z_points,
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


def main():
    st.title("3D爱心散点图")
    if st.button('DRAW'):
        draw_heart()


if __name__ == "__main__":
    main()
