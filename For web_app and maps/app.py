import dash
from dash import html, dcc, Input, Output
import average_ready_in_time
import ingredients_variety
import GDP_per_capita

app = dash.Dash(__name__)
app.title = "Country Data Visualization"

# Define the app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Define the callback to update the page content based on the URL
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/average':
        return average_ready_in_time.layout
    elif pathname == '/gdp':
        return GDP_per_capita.layout
    elif pathname == '/ingredients':
        return ingredients_variety.layout
    else:
        return html.Div([
            html.H1("Welcome to the Country Data Visualization App"),
            html.Div([
                html.H3("Select a map to view:"),
                html.Ul([
                    html.Li(dcc.Link('Average Ready In Time per Recipe', href='/average')),
                    html.Li(dcc.Link('GDP per capita', href='/gdp')),
                    html.Li(dcc.Link('Ingredients Variety', href='/ingredients'))
                ])
            ])
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
