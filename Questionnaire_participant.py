import dash
from dash import dcc, html, Output, Input, State
import dash_bootstrap_components as dbc
import style

# Initialize app
app = dash.Dash(__name__)

# Define the start screen
start = html.Div([
    html.H6("START", style = {**style.text_style,  'fontSize': '20px', 'font-weight': 'bold'})
])

# Define the questions
q1 = html.Div([
    html.H6("What is your gender?", style = {**style.text_style,  'fontSize': '20px', 'font-weight': 'bold'}),
    html.Hr(style=style.question_line_style),
    html.Div(
    dbc.RadioItems(
        id="input_q1",
        options=[
            {"label": "Male", "value": "1"},
            {"label": "Female", "value": "2"},
            {"label": "Other/rather not say", "value": "3"},
        ]
    ),        style={**style.text_question_style, "backgroundColor": "white"}
    )

], id="div_q1", style={"display": "none"})  # Hidden initially

q2 = html.Div([
    html.H6("What is your year of birth? (1950-2024)", style = {**style.text_style,  'fontSize': '20px', 'font-weight': 'bold'}),
    html.Hr(style=style.question_line_style),
    html.Div(
    dbc.Input(type = "number", min = 1950, max = 2024, step =1,
        id="input_q2",

    ),        style={**style.text_question_style, "backgroundColor": "white"}
    )
], id="div_q2", style={"display": "none"})  # Hidden initially

q3 = html.Div([
    html.H6("Do you have professional working experience?", style = {**style.text_style,  'fontSize': '20px', 'font-weight': 'bold'}),
    html.Hr(style=style.question_line_style),
    html.Div(
    dbc.RadioItems(
        id="input_q3",
        options=[
            {"label": "Yes", "value": "1"},
            {"label": "No", "value": "0"},
        ]
    ),        style={**style.text_question_style, "backgroundColor": "white"}
    )

], id="div_q3", style={"display": "none"})  # Hidden initially

q4 = html.Div([
    html.H6("Have you been in a management position?", style = {**style.text_style,  'fontSize': '20px', 'font-weight': 'bold'}),
    html.Hr(style=style.question_line_style),
    html.Div(
    dbc.RadioItems(
        id="input_q4",
        options=[
            {"label": "Yes", "value": "1"},
            {"label": "No", "value": "0"},
        ]
    ),        style={**style.text_question_style, "backgroundColor": "white"}
    )

], id="div_q4", style={"display": "none"})  # Hidden initially

q5 = html.Div([
    html.H6(
        "How do you see yourself: are you a person who is generally willing to take risks, or do you try to avoid taking risks?",
            style = {**style.text_style,  'fontSize': '20px', 'font-weight': 'bold'}
    ),
    html.Hr(style=style.question_line_style),
    html.Div(
        [html.Span("0 - Completely unwilling to take risks", style = {'float': 'left', 'position': 'relative', 'top': '-10px'}),
         html.Span("10 = Very willing to take risks", style = {'float': 'right', 'position': 'relative', 'top': '-10px'}),
         ],
        style={**style.text_question_style, "backgroundColor": "white", 'marginBottom': '30px', 'line-height': '1.5'}

    ),
    dcc.Slider(id="input_q5",
                    min=0,
                    max=10,
                    step=1,
                    marks = {i: str(i) for i in range(11)}
    )

], id="div_q5", style={**style.text_question_style, "backgroundColor": "white", "display": "none"})  # Hidden initially




def inner_panel():
    return html.Div(
        style= {
            **style.rectangle_part_style,
            'backgroundColor': style.COLOR_DARKGREEN,
                },
        children= [        html.Div(id="start_id", children=start),  # Start block
        html.Div(id="question_container", children=[q1, q2, q3, q4, q5]),  # Container for all questions

        dbc.Button("Next", color="primary", id="button_next", n_clicks=0, style = {**style.question_next_button_style, }),
        # Hidden div to store the current question index
        html.Div(id='current_step', children=0, style={'display': 'none'}),]
    )


# Layout
app.layout = html.Div(
    style=style.background_part_style,
    children=[
        inner_panel(),
        html.Img(
            src="/assets/GRC.png",
            style=style.grc_bottom_img
        ),

    ]
)

# Callback to update questions based on button clicks
@app.callback(
    [Output("div_q1", "style"),
     Output("div_q2", "style"),
     Output("div_q3", "style"),
     Output("div_q4", "style"),
     Output("div_q5", "style"),
     Output("start_id", "children"),
     Output('current_step', 'children')],
    Input("button_next", "n_clicks"),
    State("input_q1", "value"),
    State("input_q2", "value"),
    State("input_q3", "value"),
    State("input_q4", "value"),
    State("input_q5", "value"),
    State('current_step', 'children')
)
def update_question(n_clicks, q1_value, q2_value, q3_value, q4_value, q5_value, current_step):
    if current_step == 0:
        return {"display": "none"}, {"display": "none"}, {"display": "none"}, {"display": "none"}, {"display": "none"}, start, 1
    elif current_step == 1:
        if q1_value:
            return {"display": "none"}, {"display": "block"}, {"display": "none"}, {"display": "none"}, {"display": "none"}, None, 2
        else:
            return {"display": "block"}, {"display": "none"}, {"display": "none"}, {"display": "none"}, {"display": "none"}, None, 1
    elif current_step == 2:
        if q2_value:
            return {"display": "none"}, {"display": "none"}, {"display": "block"}, {"display": "none"}, {"display": "none"}, None, 3
        else:
            return {"display": "none"}, {"display": "block"}, {"display": "none"}, {"display": "none"}, {"display": "none"}, None, 2
    elif current_step == 3:
        if q3_value:
            return {"display": "none"}, {"display": "none"}, {"display": "none"}, {"display": "block"}, {"display": "none"}, None, 4
        else:
            return {"display": "none"}, {"display": "none"}, {"display": "block"}, {"display": "none"}, {"display": "none"}, None, 3
    elif current_step == 4:
        if q4_value:
            return {"display": "none"}, {"display": "none"}, {"display": "none"}, {"display": "none"}, {"display": "block"}, None, 5
        else:
            return {"display": "none"}, {"display": "none"}, {"display": "none"}, {"display": "block"}, {"display": "none"}, None, 4
    else:
        if q5_value:
            return {"display": "none"}, {"display": "none"}, {"display": "none"}, {"display": "none"}, {"display": "none"}, html.H6(
                    "Survey Completed. Thank you!", style = {**style.text_style,  'fontSize': '20px', 'font-weight': 'bold'}), 6
        else:
             return {"display": "none"}, {"display": "none"}, {"display": "block"}, {"display": "none"}, {"display": "none"}, None, 5


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)