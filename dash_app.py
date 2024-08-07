import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from datetime import datetime
# *should* work. can't check, local machine always struggles with dependencies
dates = []
sales = []

with open('formatted_output.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        date = datetime.strptime(row['date'], '%Y-%m-%d')
        sale = float(row['sales'].replace('$', '').replace(',', ''))

        dates.append(date)
        sales.append(sale)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Sales"),
    dcc.Graph(
        id='sales-line-chart',
        figure={
            'data': [
                go.Scatter(
                    x=dates,
                    y=sales,
                    mode='lines+markers',
                    name='Sales'
                )
            ],
            'layout': go.Layout(
                title='Sales Over Time',
                xaxis={'title': 'Date'},
                yaxis={'title': 'Sales ($)'},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
