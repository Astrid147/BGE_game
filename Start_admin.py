# Import of Python packages
import dash
from dash import html, Output, Input
import dash_bootstrap_components as dbc
import style

# Initialize app
app = dash.Dash(__name__)


# Define content that is in every tab
tab_about_content = html.Div([html.H3("Something about how the game works", style=style.text_style),
                              html.Br(),
                              html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod "
                                     "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis "
                                     "nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
                                     "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu "
                                     "fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
                                     "culpa qui officia deserunt mollit anim id est laborum.", style=style.text_style)])

tab_data_content = html.Div([html.H3("Something about that you can download the data", style=style.text_style)])

tab_newgame_content = html.Div([html.H3("Here you can start a new game, maybe even change parameters", style=style.text_style)])

# Create the inner rectangle and the tabs
def inner_panel():
    tabs = html.Div(
        children=[
            dbc.ButtonGroup(
                children=[
                    dbc.Button('About', id='button_about', style = style.tab_admin_style),
                    dbc.Button('Data', id='button_data', style = style.tab_admin_style),
                    dbc.Button('New game', id='button_newgame', style = style.tab_admin_style),
                ],
            ),
            html.Div(id="content_innerpanel"),
        ]
    )
    return html.Div(
        children=[tabs],
        style= style.rectangle_admin_style,
    )



# Layout
app.layout = html.Div(
    style=style.background_admin_style,
    children=[
        inner_panel(),
        html.Img(
            src="/assets/GRC.png",
            style=style.grc_bottom_img
        )
    ],

)

# Callback of the tabs. The makes sure that clicking on a tab shows the content of only that tab
@app.callback(
    Output("content_innerpanel", "children"),
    [Input('button_about', 'n_clicks'),
     Input('button_data', 'n_clicks'),
     Input('button_newgame', 'n_clicks')]
)
def display_content(n_clicks_about, n_clicks_data, n_clicks_newgame):
    ctx = dash.callback_context

    if not ctx.triggered:
        return tab_about_content

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'button_about':
        return tab_about_content
    elif button_id == 'button_data':
        return tab_data_content
    elif button_id == 'button_newgame':
        return tab_newgame_content
    else:
        return tab_about_content

# Run app.
if __name__ == "__main__":
    app.run_server(debug=True)
