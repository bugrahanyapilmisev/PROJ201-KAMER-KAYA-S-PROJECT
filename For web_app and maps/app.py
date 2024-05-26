import dash
from dash import html, dcc, Input, Output, State
import joblib
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import average_ready_in_time
import ingredients_variety
import GDP_per_capita

# Ensure NLTK data is downloaded (if needed for other parts of the application)
nltk.download('stopwords')
nltk.download('wordnet')

# Load the saved model and vectorizer (ensure these are correct paths)
model = joblib.load('trained_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Country Data Visualization"

# Text preprocessing functions
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

lemmatizer = WordNetLemmatizer()
def lemmatize_text(text):
    return ' '.join([lemmatizer.lemmatize(word) for word in text.split()])

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
    elif pathname == '/predict':
        return html.Div([
            html.H1("Predict Country from Ingredients"),
            dcc.Textarea(
                id='ingredients-input',
                placeholder='Enter ingredients, separated by commas...',
                style={'width': '100%', 'height': 100},
            ),
            html.Button('Predict', id='predict-button', n_clicks=0),
            html.Div(id='prediction-output')
        ])
    else:
        return html.Div([
            html.H1("Welcome to the Country Data Visualization App"),
            html.Div([
                html.H3("Select a map to view:"),
                html.Ul([
                    html.Li(dcc.Link('Average Ready In Time per Recipe', href='/average')),
                    html.Li(dcc.Link('GDP per capita', href='/gdp')),
                    html.Li(dcc.Link('Ingredients Variety', href='/ingredients')),
                    html.Li(dcc.Link('Predict Country from Ingredients', href='/predict'))
                ])
            ])
        ])

# Callback for prediction
@app.callback(
    Output('prediction-output', 'children'),
    [Input('predict-button', 'n_clicks')],
    [State('ingredients-input', 'value')]
)
def predict_country(n_clicks, ingredients):
    if n_clicks > 0 and ingredients:
        ingredients = preprocess_text(ingredients)
        ingredients = lemmatize_text(ingredients)
        ingredients_vector = vectorizer.transform([ingredients])
        prediction = model.predict(ingredients_vector)
        return html.Div([
            html.H3(f'The predicted country for the given ingredients is: {prediction[0]}')
        ])
    return ''


app.run_server(debug=True)
