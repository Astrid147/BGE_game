# Import of Python packages
import dash
from dash import html
import dash_bootstrap_components as dbc
import style

# Initialize app
app = dash.Dash(__name__)

# Build right side of the login page

def render_right_panel():
    return html.Div(
        # Color and settings background
        style={**style.right_style, 'right': '0', 'backgroundColor': style.COLOR_DARKGREEN},
        # Set location of input fields and login button
        children=html.Div(
            style={
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
                'flexDirection': 'column',
            },
            children=[
                # Define username text and input field
                html.Div(
                    style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '20px'},
                    children=[
                        html.Div("Username", style= style.login_text_style),
                        dbc.Input(id='input-username', style={"width": style.INPUT_WIDTH_LOGIN, "height": style.INPUT_HEIGHT_LOGIN})
                    ]
                ),
                # Define password text and input field
                html.Div(
                    style={'display': 'flex', 'alignItems': 'center'},
                    children=[
                        html.Div("Password", style=style.login_text_style),
                        dbc.Input(id='input-password', type='password', style={"width": style.INPUT_WIDTH_LOGIN, "height": style.INPUT_HEIGHT_LOGIN})
                    ]
                ),
                html.Br(),
                # Define Experiment ID text and input field
                html.Div(
                    style={'display': 'flex', 'alignItems': 'center'},
                    children=[
                        html.Div("Experiment ID", style=style.login_text_style),
                        dbc.Input(id='input-experimentID', type='text',
                                  style={"width": style.INPUT_WIDTH_LOGIN, "height": style.INPUT_HEIGHT_LOGIN})
                    ]
                ),
                html.Br(),
                # Define the log in button
                html.Div(
                    style={'display': 'flex', 'alignItems': 'center'},
                    children=[
                        dbc.Button("Log in", color=style.COLOR_DARKGREEN, id="button-login", n_clicks=0, style={**style.login_button_style, "backgroundColor": style.COLOR_EXPRES}),
                    ]
                ),
                html.Br(),
                # Define the switch button
                html.Div(
                    style={'display': 'flex', 'alignItems': 'center'},
                    children=[
                        dbc.Button("Switch to user module", color=style.COLOR_DARKGREEN, id="button-switch", n_clicks=0, style={**style.switch_button_style, "backgroundColor": style.COLOR_EXPRES}),
                    ]
                )
            ]
        )
    )

# Build left side of the login page

def render_left_panel():
    return html.Div(
        children=[
            # Create top left part of page
            html.Div(
                style={'position': 'absolute', 'top': '0', 'left': '0', 'width': '50%', 'height': '50%', 'backgroundColor': style.COLOR_DARKGRAY},
                children=html.Div("Classroom log in", style= {**style.title_style,     'color': style.COLOR_WHITE})
            ),
            # Create bottom left part of page
            html.Div(style={'position': 'absolute', 'bottom': '0', 'left': '0', 'width': '25%', 'height': '50%', 'backgroundColor': style.COLOR_DARKGRAY}),
            # Create bottom middle diagonal line
            html.Div(
                style={
                    'position': 'absolute',
                    'bottom': '0',
                    'left': '25%',
                    'width': '25%',
                    'height': '50%',
                    'background': f'linear-gradient(to bottom right, {style.COLOR_DARKGRAY} 50%, {style.COLOR_DARKGREEN} 50%)',
                }
            ),
        ]
    )


# Layout of entire page
app.layout = html.Div(
    # Load complete page style
    style=style.full_style,
    # Add left and right page and picture on page.
    children=[
        render_right_panel(),
        render_left_panel(),
        # Image
        html.Div(
            style=style.grc_bottom_img,
            children=[
                html.Img(src="/assets/GRC.png", style={'width': '100%', 'height': 'auto', 'borderRadius': '15px'})
            ]
        ),
    ]
)

# Run app.
if __name__ == "__main__":
    app.run_server(debug=True)
