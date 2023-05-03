from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash_draggable

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection', style={'width': '45%'}),
    dcc.Dropdown(['lifeExp', 'pop', 'gdpPercap'], 'pop', id = 'dropdown-column', style={'width': '45%'}),
    dcc.Dropdown(sorted(df.year.unique()), 2007, id='dropdown-year', style={'width': '45%'}),
    dash_draggable.GridLayout(
        id='draggable',
        children=[dcc.Graph(id='graph-content'), html.Div(id='graph2')]
    )
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value'),
    Input('dropdown-column', 'value'),
    #prevent_initial_call = True
)
def draw_line(country, column):
    dff = df[df.country==country]
    return px.line(dff, x='year', y=column)
@callback(
    Output('graph2', 'children'),
    Input('dropdown-column', 'value'),
    Input('dropdown-year', 'value')
)
def draw_bar(column, year):
    dff = df[df.year==year]
    if column == 'lifeExp':
        df_temp = dff.groupby('continent').mean()
    else:
        df_temp = dff.groupby('continent').sum()
    return dcc.Graph(figure = px.bar(df_temp, x=df_temp.index, y=column), id='bar-content')
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader = False)