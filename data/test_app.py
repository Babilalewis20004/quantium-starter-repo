import pytest
from dash.testing.application_runners import import_app


@pytest.fixture
def app():
    # Import the Dash app from the module
    return import_app("data.pink_morsel_visualizer")


def test_header_present(dash_duo, app):
    dash_duo.start_server(app)

    # Check that the header element exists
    header = dash_duo.find_element("#header")
    assert header.text == "Pink Morsel Visualizer"


def test_visualization_present(dash_duo, app):
    dash_duo.start_server(app)

    # Check that the graph is present
    graph = dash_duo.find_element("#visualization")
    assert graph is not None


def test_region_picker_present(dash_duo, app):
    dash_duo.start_server(app)

    # Check that the region picker radio buttons exist
    region_picker = dash_duo.find_element("#region_picker")
    assert region_picker is not None
