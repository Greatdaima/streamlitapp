import plotly.graph_objs as go
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
st.set_page_config(page_title="3D爱心散炫", page_icon=":heart:", layout='centered')

st.title("2D爱心散炫")


def draw_heart():
    x_coords = np.linspace(-10, 10, 200)
    y_coords = np.linspace(-10, 10, 200)
    points = []
    for y in y_coords:
        for x in x_coords:
            if ((x*0.03)**2+(y*0.03)**2-1)**3-(x*0.03)**2*(y*0.03)**3 <= 0:
                points.append({"x": x, "y": y})
    heart_x = list(map(lambda point: point["x"], points))
    heart_y = list(map(lambda point: point["y"], points))

    fig = go.Scatter(
        x=heart_x,
        y=heart_y,
        mode='markers',
        marker=dict(
            size=10,
            opacity=0.5
        )
    )

    layout = go.Layout(
        width=700,
        height=700,
        showlegend=False,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
    )

    fig_data = [fig]
    fig_layout = go.Figure(data=fig_data, layout=layout)

    st.plotly_chart(fig_layout, use_container_width=True)


def main():
    if st.button('DRAW'):
        draw_heart()


if __name__ == "__main__":
    main()
