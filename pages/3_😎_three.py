import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Draw a Heart using Streamlit", page_icon=":heart:", layout="wide")


def draw_heart():
    # 生成x和y的数据
    t = np.linspace(0, 2*np.pi, 100)
    x = 16 * np.power(np.sin(t), 3)
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

    # 创建画布和子图
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(x, y, 'r')  # 绘制爱心曲线
    ax.set_aspect('equal')  # 设置等比例缩放

    # 移除坐标轴
    ax.axis('off')

    # 显示图形
    st.pyplot(fig)

# 在Streamlit应用程序中调用绘制函数
def main():
    st.title("Draw a Heart using Streamlit")

    st.write("Click the button below to draw a heart:")

    if st.button("Draw"):
        draw_heart()

if __name__ == "__main__":
    main()

