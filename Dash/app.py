from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import numpy as np

app = Dash()
X =np.linspace(0, 10, 100)
sinus = px.line(x= X, y= np.sin(X))
cosinus = px.line(x= X, y= np.cos(X))

app.layout = html.Div(className='parent', children=[
    html.Div(className='child',children=dcc.Graph(figure=sinus)),
    html.Div(className='child',children=dcc.Graph(figure=cosinus))
    ]
    html.Div(className='row', children=[
    dcc.RadioItems(options=[10, 20, 50, 100],
                    value= 10,
                    inline=True,
                    id='my-radio-buttons-final')
    ]
    )
)



if __name__ == '__main__':
    app.run(debug=True)