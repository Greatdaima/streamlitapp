import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def draw_heart():
    # start generating points
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sqrt(X**2 + Y**2) + np.sin(X**2 + Y**2)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(X, Y, c=Z, cmap='viridis', s=5)
    ax.set_title('3D爱心散点图')
    ax.grid(True)

    # 将 Matplotlib 图形显示在 Streamlit 中
    st.pyplot(fig)


def main():
    with st.expander('3D爱心散点图'):
        if st.button('绘制'):
            draw_heart()


if __name__ == '__main__':
    main()
