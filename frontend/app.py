# A minimal dash app
#
# The following code snippet shows a minimal Dash app that displays a simple line chart:

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(
        figure=px.line(x=[1, 2, 3], y=[1, 3, 2])
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)



