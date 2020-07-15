import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.graph_objects as go
from django_plotly_dash import DjangoDash

from DBTables.GDPTable import GDP
from global_session import postgres_session

np.random.seed(1)

N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 5

app = DjangoDash("gdp_app")

fig = go.Figure()

fig.add_trace(go.Scatter(x = [data.year for data in postgres_session.query(GDP).filter_by(country = "cn").all()],
                         y = [data.gdp for data in postgres_session.query(GDP).filter_by(country = "cn").all()],
                         mode = 'lines',
                         name = 'lines'))
fig.add_trace(go.Scatter(x = [data.year for data in postgres_session.query(GDP).filter_by(country = "us").all()],
                         y = [data.gdp for data in postgres_session.query(GDP).filter_by(country = "us").all()],
                         mode = 'lines+markers',
                         name = 'lines+markers'))
fig.add_trace(go.Scatter(x = [data.year for data in postgres_session.query(GDP).filter_by(country = "in").all()],
                         y = [data.gdp for data in postgres_session.query(GDP).filter_by(country = "in").all()],
                         mode = 'markers', name = 'markers'))

app.layout = html.Div([
    dcc.Graph(
        id = 'example',
        figure = fig,
        responsive = True
    ),

])
#
# app.layout = html.Div([
#     dcc.Graph(
#         id = 'example',
#         figure = {
#             'data': [
#                 {'x': [1, 2, 3, 1], 'y': [4, 1, 2, 9], 'type': 'bar', 'name': 'SF'},
#                 {'x': [1, 2, 3, 1], 'y': [2, 4, 5, 100], 'type': 'bar', 'name': u'Montréal'},
#             ],
#             'layout': {
#                 'title': 'Dash Data Visualization',
#             }
#         },
#         responsive = True
#     ),
#
# ])
