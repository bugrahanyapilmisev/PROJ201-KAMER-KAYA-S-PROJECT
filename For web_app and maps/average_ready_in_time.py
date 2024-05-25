import pandas as pd
import plotly.express as px
from dash import html, dcc, callback, Input, Output
import dash


def create_ready_in_time_map():
    df = pd.read_csv(r'Country_ISO_Average Ready In_Geocultural Region Mini Dataset.csv')
    fig = px.choropleth(
        df,
        locations="ISO-3",
        color="Average Ready In Per Recipe",
        hover_name="Country",
        color_continuous_scale=px.colors.sequential.Plasma,
        range_color=(55.762019230769226, 298.47842744291285),
        color_continuous_midpoint=155,
        projection="natural earth",
        title="Average Ready In Time per Recipe by Countries"
    )
    return fig

layout = html.Div([
    html.H1('Average Ready in Time Map'),
    dcc.Graph(figure=create_ready_in_time_map())
])
