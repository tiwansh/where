import dash_core_components as dcc
import dash_html_components as html

from django_plotly_dash import DjangoDash

app = DjangoDash("gdp_app")

app.layout = html.Div([
    dcc.Graph(
        id = 'example',
        figure = {
            'data': [
                {'x': [1, 2, 3, 1], 'y': [4, 1, 2, 9], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3, 1], 'y': [2, 4, 5, 100], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
            }
        },
        responsive = True
    ),

])
