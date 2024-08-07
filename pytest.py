import pytest
from dash import Dash
from dash.testing.application_runners import import_app
# can't check anything. i hate this machine
@pytest.fixture
def app():
    # Import and create an instance of the Dash app
    app = import_app('app')  # Make sure 'app' matches your script name
    return app

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    # Check if the header text is present in the layout
    header = dash_duo.find_element('#header')
    assert header.text == "Soul Foods Sales Visualization"

def test_visualization_present(dash_duo):
    dash_duo.start_server(app)
    # Check if the line chart (graph) is present in the layout
    graph = dash_duo.find_element('#sales-line-chart')
    assert graph is not None

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    # Check if the radio items (region picker) are present in the layout
    radio_items = dash_duo.find_element('#region-filter')
    assert radio_items is not None
