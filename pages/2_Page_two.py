import streamlit as st
import plotly.graph_objects as go
import numpy as np

def draw_scatter3d():
    # 生成随机数据
    np.random.seed(42)
    x = np.random.rand(10000)
    y = np.random.rand(10000)
    z = np.random.rand(10000)

    # 创建散点图
    fig = go.Figure(data=go.Scatter3d(x=x, y=y, z=z, mode='markers',
                                      marker=dict(size=5, color=z, colorscale='Viridis', opacity=0.8)))

    # 设置布局和样式
    fig.update_layout(scene=dict(xaxis=dict(visible=False),
                                 yaxis=dict(visible=False),
                                 zaxis=dict(visible=False)),
                      margin=dict(l=0, r=0, b=0, t=0))

    # 显示图形
    st.plotly_chart(fig, use_container_width=True)

# 在Streamlit应用程序中调用绘制函数
def main():
    st.title("Draw a 3D Scatter Plot using Streamlit")

    st.write("Click the button below to draw a 3D scatter plot:")

    if st.button("Draw"):
        draw_scatter3d()

if __name__ == "__main__":
    main()
