# Import of Python packages
import dash
from dash import html
import dash_bootstrap_components as dbc
import style

# Initialize app
app = dash.Dash(__name__)


# Define content
text = html.Div([html.H1("Welcome!", style={'fontSize': '18px',
                                            'marginLeft': '50px',
                                            'marginRight': '50px',
                                            'marginTop': '20px',
                                            'font-weight': 'bold',}),
                              html.Br(),
                              html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod "
                                     "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis "
                                     "nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
                                     "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu "
                                     "fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
                                     "culpa qui officia deserunt mollit anim id est laborum.", style={**style.text_style, 'color': style.COLOR_BLACK} )])

# Create the inner rectangle
def inner_panel():
    return html.Div(
        style= style.rectangle_part_style,
        children=text,
    )

# Combine the layout
app.layout = html.Div(
    style=style.background_part_style,
    children=[
        inner_panel(),
        html.Img(
            src="/assets/GRC.png",
            style=style.grc_bottom_img
        ),
        dbc.Button("Next", color=style.COLOR_BLACK, id="button_next",
                   n_clicks=0,
                   style= style.next_part_style),
    ]
)

# Run app
if __name__ == "__main__":
    app.run_server(debug=True)
