import pytest
from dash.testing.application_runners import import_app
# can't check anything. i hate this machine
@pytest.fixture
def app():
    app = import_app('dash_app')
    return app

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element('#header')
    assert header.text == "Soul Foods Sales Visualization"

def test_visualization_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element('#sales-line-chart')
    assert graph is not None

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    radio_items = dash_duo.find_element('#region-filter')
    assert radio_items is not None
