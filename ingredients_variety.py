import pandas as pd
import plotly.express as px
from dash import html, dcc, callback, Input, Output
import dash

"""_name_="ingredients_variety"
dash.register_page("update_ingredients_map")"""

def create_ingredients_variety_map():
    df = pd.read_csv(r'C:\Users\kosot\OneDrive\Masaüstü\PROJ201\pages\ingredients_variety.csv')
    custom_color_scale = [
        (0.0, "rgb(12,51,131)"),
        (0.1, "rgb(10,136,186)"),
        (0.2, "rgb(242,211,56)"),
        (0.3, "rgb(242,143,56)"),
        (0.4, "rgb(217,30,30)"),
        (0.5, "rgb(179,0,0)"),
        (0.6, "rgb(128,0,38)"),
        (0.7, "rgb(179,88,6)"),
        (0.8, "rgb(248,184,139)"),
        (0.9, "rgb(140,81,10)"),
        (1.0, "rgb(84,48,5)")
    ]
    fig = px.choropleth(
        df,
        locations="ISO-3 Code",
        color="Ingredients Variety",
        hover_name="Country",
        color_continuous_scale=custom_color_scale,
        range_color=(df["Ingredients Variety"].min(), df["Ingredients Variety"].max()),
        color_continuous_midpoint=df["Ingredients Variety"].median(),
        projection="natural earth",
        title="Ingredients Variety per Countries"
    )
    return fig

layout = html.Div([
    html.H1('Ingredients Variety per Countries Map'),
    dcc.Graph(figure=create_ingredients_variety_map())
])
