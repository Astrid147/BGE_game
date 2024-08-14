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
        style={**style.right_style, 'backgroundColor': style.COLOR_BLACK},
        # Set location of input fields and login button
        children=html.Div(
            style={
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
                'flexDirection': 'column',
            },
            children=[
                # Define admin name text and input field
                html.Div(
                    style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '20px'},
                    children=[
                        html.Div("Admin name", style=style.login_text_style),
                        dbc.Input(id='input-adminname-admin', style={"width": style.INPUT_WIDTH_LOGIN, "height": style.INPUT_HEIGHT_LOGIN})
                    ]
                ),
                # Define password text and input field
                html.Div(
                    style={'display': 'flex', 'alignItems': 'center'},
                    children=[
                        html.Div("Password", style=style.login_text_style),
                        dbc.Input(id='input-password-admin', type='password', style={"width": style.INPUT_WIDTH_LOGIN, "height": style.INPUT_HEIGHT_LOGIN})
                    ]
                ),
                html.Br(),
                # Define the log in button
                html.Div(
                    style={'display': 'flex', 'alignItems': 'center'},
                    children=[
                        dbc.Button("Log in", color=style.COLOR_BLACK, id="button-login-admin", n_clicks=0, style={**style.login_button_style,
                                                                                                            'backgroundColor': style.COLOR_LIGHTBLUE}),
                    ]
                ),
                html.Br(),
                # Define the switch button
                html.Div(
                    style={'display': 'flex', 'alignItems': 'center'},
                    children=[
                        dbc.Button("Switch to user module", color=style.COLOR_BLACK, id="button-switch-admin", n_clicks=0, style= {**style.switch_button_style,
                                                                                                                             'backgroundColor': style.COLOR_LIGHTBLUE}),
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
                style={**style.left_style,
                       'top': '0',
                       'width': '50%',
                       'backgroundColor': style.COLOR_LIGHTBLUE},
                children=html.Div("Admin Module", style= style.title_style)
            ),
            # Create bottom left part of page
            html.Div(style={**style.left_style,
                            'bottom': '0',
                            'backgroundColor': style.COLOR_LIGHTBLUE}),
            # Create bottom middle diagonal line
            html.Div(
                style={**style.left_style,
                       'left': '25%',
                       'bottom': '0',
                       'background': f'linear-gradient(to bottom right, {style.COLOR_LIGHTBLUE} 50%, {style.COLOR_BLACK} 50%)',
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
            style= style.grc_bottom_img,
            children=[
                html.Img(src="/assets/GRC.png", style={'width': '100%', 'height': 'auto', 'borderRadius': '15px'})
            ]
        ),
    ]
)

# Run app. 
if __name__ == "__main__":
    app.run_server(debug=True)
