import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from datetime import datetime

# Read and process the CSV data
dates = []
sales = []
regions = []

with open('formatted_output.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        date = datetime.strptime(row['date'], '%Y-%m-%d')
        sale = float(row['sales'].replace('$', '').replace(',', ''))
        region = row['region']

        dates.append(date)
        sales.append(sale)
        regions.append(region)

# Create a Dash application
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Soul Foods Sales Visualization", style={'textAlign': 'center', 'color': '#333'}),

    html.Div([
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'All Regions', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'}
            ],
            value='all',
            style={'margin': '10px'}
        )
    ], style={'textAlign': 'center'}),

    dcc.Graph(
        id='sales-line-chart',
        style={'height': '70vh', 'width': '90vw', 'margin': '0 auto'}
    )
], style={'fontFamily': 'Arial, sans-serif', 'backgroundColor': '#f5f5f5', 'padding': '20px'})

# Define the callback to update the graph based on the selected region
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    filtered_dates = []
    filtered_sales = []

    if selected_region == 'all':
        filtered_dates = dates
        filtered_sales = sales
    else:
        for date, sale, region in zip(dates, sales, regions):
            if region == selected_region:
                filtered_dates.append(date)
                filtered_sales.append(sale)

    figure = {
        'data': [
            go.Scatter(
                x=filtered_dates,
                y=filtered_sales,
                mode='lines+markers',
                name='Sales',
                line=dict(color='#007bff')
            )
        ],
        'layout': go.Layout(
            title=f'Sales Over Time ({selected_region.capitalize() if selected_region != "all" else "All Regions"})',
            xaxis={'title': 'Date'},
            yaxis={'title': 'Sales ($)'},
            hovermode='closest'
        )
    }

    return figure

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
