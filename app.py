from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('merged_data.csv', low_memory=False)
df['Timestamp'] = pd.to_datetime(df['VariableKey'])
tank_list = df.Tank.unique()
sorted_tank_list = sorted(tank_list)

app = Dash(__name__)

app.layout = html.Div([html.Div([
    html.H1(children='AMBR Data Viz', style={'textAlign':'center'}), 
]),
html.Div([
    dcc.Dropdown(sorted_tank_list, 1, id='dropdown-selection',style={'width':'300px'}),
],style={'display':'flex','justify-content':'center','alingn-items':'center','width':'100%'}),
html.Div([
    dcc.Graph(id='DO', style={'width':'50%'}),
    dcc.Graph(id='pH', style={'width':'50%'}),
    dcc.Graph(id='Agitation', style={'width':'50%'})],
    style={'display':'inline-flex','flex-wrap':'wrap'})])

@callback(
    Output('DO', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_DO(value):
    dff = df[df.Tank==value]
    return px.line(dff, x='Timestamp', y='DO (% air sat.)')

@callback(
    Output('pH', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_pH(value):
    dff = df[df.Tank==value]
    return px.line(dff, x='Timestamp', y='pH (pH)')

@callback(
    Output('Agitation', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_Agitation(value):
    dff = df[df.Tank==value]
    return px.line(dff, x='Timestamp', y='Stir speed (rpm)')

if __name__ == '__main__':
    app.run(debug=True)

    


