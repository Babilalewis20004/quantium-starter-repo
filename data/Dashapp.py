import pandas as pd
from datetime import datetime

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# ------------------------------------------------------------------------------
# Load and prepare data
# ------------------------------------------------------------------------------
df = pd.read_csv("formatted_data.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

PRICE_INCREASE_DATE = datetime(2021, 1, 15)

# ------------------------------------------------------------------------------
# Create Dash app
# ------------------------------------------------------------------------------
app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(
            "Soul Foods Pink Morsel Sales Visualiser",
            style={
                "textAlign": "center",
                "color": "#6A1B9A",
                "marginBottom": "10px"
            }
        ),

        html.P(
            "Explore how Pink Morsel sales changed over time and by region. "
            "The dashed line marks the price increase on 15 January 2021.",
            style={
                "textAlign": "center",
                "fontSize": "16px",
                "color": "#444",
                "marginBottom": "30px"
            }
        ),

        html.Div(
            children=[
                html.Label(
                    "Select Region:",
                    style={
                        "fontWeight": "bold",
                        "marginRight": "15px"
                    }
                ),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={"fontSize": "14px"}
                )
            ],
            style={
                "textAlign": "center",
                "marginBottom": "25px"
            }
        ),

        dcc.Graph(
            id="sales-line-chart"
        )
    ],
    style={
        "maxWidth": "1000px",
        "margin": "0 auto",
        "padding": "20px",
        "backgroundColor": "#FAF7FB",
        "borderRadius": "12px",
        "boxShadow": "0px 4px 12px rgba(0, 0, 0, 0.1)"
    }
)

# ------------------------------------------------------------------------------
# Callback to update chart based on selected region
# ------------------------------------------------------------------------------
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
        title_region = "All Regions"
    else:
        filtered_df = df[df["region"] == selected_region]
        title_region = selected_region.capitalize()

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales Over Time ({title_region})",
        labels={
            "date": "Date",
            "sales": "Total Sales ($)"
        }
    )

    fig.add_vline(
        x=PRICE_INCREASE_DATE,
        line_dash="dash",
        line_color="red",
        annotation_text="Price Increase<br>15 Jan 2021",
        annotation_position="top right"
    )

    fig.update_layout(
        title_font_size=20,
        plot_bgcolor="white",
        paper_bgcolor="#FAF7FB",
        margin=dict(l=40, r=40, t=80, b=40)
    )

    return fig

# ------------------------------------------------------------------------------
# Run app
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
