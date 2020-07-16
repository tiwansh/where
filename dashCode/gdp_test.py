from random import randrange

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from django_plotly_dash import DjangoDash

from DBTables.GDPTable import GDP, HistoricalGDP
from sqlalchemy_globals import postgres_session

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

new_app = DjangoDash("gdp_historic_share_app")

fig1 = go.Figure()

regions = [data.region for data in postgres_session.query(HistoricalGDP).with_entities(HistoricalGDP.region).distinct()]
year_list = sorted(
    [data.year for data in postgres_session.query(HistoricalGDP).with_entities(HistoricalGDP.year).distinct()])
for region in regions:
    fig1.add_trace(go.Scatter(x = year_list, y = [data.percent * 100.0 for data in
                                                  postgres_session.query(HistoricalGDP).filter_by(
                                                      region = region).order_by(HistoricalGDP.year.asc())],
                              mode = 'lines',
                              line = dict(width = 0.5,
                                          color = f'rgb({randrange(0, 255)}, {randrange(0, 255)}, {randrange(0, 255)})'),
                              stackgroup = 'one',
                              name = region))

new_app.layout = html.Div([
    dcc.Graph(
        id = 'example1',
        figure = fig1,
        responsive = True,
        config = {
            'displayModeBar': False,
            # 'modeBarButtonsToRemove': ['select2d', 'resetScale2d', 'pan2d', 'lasso2d']
        }

    ),

])
