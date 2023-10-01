import streamlit as st
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import math
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def main():
    st.title("3D爱心三点图")

    if st.button("Draw"):
        draw_heart()


def draw_heart():
    # start generating points
    x_lim = np.linspace(-10, 10, 200)
    y_lim = np.linspace(-10, 10, 200)
    z_lim = np.linspace(-10, 10, 200)
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

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_zlim(-1, 1)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.scatter(X_points, Y_points, Z_points)
    # 设置相机角度
    ax.view_init(elev=20, azim=-60)

    st.write(fig)


if __name__ == "__main__":
    main()
