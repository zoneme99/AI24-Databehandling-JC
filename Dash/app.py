from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import numpy as np

app = Dash()
X =np.linspace(0, 10, 100)
sinus = px.line(x= X, y= np.sin(X))
cosinus = px.line(x= X, y= np.cos(X))

app.layout = html.Div(className='parent', children=[
    html.Div(className='child',children=dcc.Graph(figure={}, id="sin")),
    html.Div(className='child',children=dcc.Graph(figure=cosinus, id="cos"))
    ]
), html.Div(className='row', children=[
    dcc.RadioItems(options=[*range(5, 55, 5)],
                    value= 5,
                    inline=True,
                    id='my-radio-buttons-final')
    ]
    )

@callback(
    [Output(component_id='sin', component_property='figure'),
     Output(component_id='cos', component_property='figure')],
    Input(component_id='my-radio-buttons-final', component_property='value')
)

def update_graphs(samples_chosen):
    X = np.linspace(0, 10, samples_chosen)
    sinus = px.line(x= X, y= np.sin(X))
    cosinus = px.line(x= X, y= np.cos(X))
    return sinus, cosinus



if __name__ == '__main__':
    app.run(debug=True)