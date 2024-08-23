
# Colors
COLOR_LIGHTBLUE = '#c9daf0'
COLOR_DARKGRAY = '#222423'
COLOR_DARKGREEN = '#274249'
COLOR_EXPRES = '#f2a359'
COLOR_BLACK = '#000000'
COLOR_WHITE = '#eff3f5'
COLOR_DARKBLUE = "#0E2841"

# Input settings
INPUT_WIDTH_LOGIN = '200px'
INPUT_HEIGHT_LOGIN = '30px'


# Styles
base_text_style = {
    'fontFamily': 'Arial, sans-serif',  # Font family applied globally

}

# full_style defines the space that a whole page should take up.
full_style = {
    'height': '100vh',
    'width': '100vw'
}

# Style of the text on the screen
text_style = {
    **base_text_style,
    'color': COLOR_WHITE,
    'fontSize': '15px',
    'marginLeft': '50px',
    'marginRight': '50px',
    'marginTop': '20px',
    'font-weight': 'normal',
}

text_question_style = {
    **base_text_style,
    'fontSize': '15px',
    'marginLeft': '50px',
    'marginRight': '50px',
    'marginTop': '20px',
    'font-weight': 'normal',
    'width': '80%',
    'backgroundColor': COLOR_WHITE,
    'color': COLOR_BLACK,
    'padding': '15px',
    'borderRadius': '8px',  # Rounded corners for a softer look
    'boxShadow': '0px 4px 6px rgba(0, 0, 0, 0.1)',  # Subtle shadow for depth
    'border': '1px solid #ddd',  # Light border for definition
    'margin': '0 auto',  # Center the radio buttons container
}



# In the log in and the end pages there is a specific style. These dictionarys help to build the right and left panel of those pages.
right_style = {
    'width': '50%',
    'height': '100%',
    'position': 'absolute',
    'display': 'flex',
    'justifyContent': 'center',
    'alignItems': 'center',
    'right': '0',
    'top': '0',
}

left_style = {
    'position': 'absolute',
    'left': '0',
    'width': '25%',
    'height': '50%',
}

# The title of a page
title_style = {
    **base_text_style,
    'paddingLeft': '8%',
    'paddingTop': '8%',
    'fontSize': '30px',
    'fontWeight': 'bold'
}

# Next to the login input field are the text that indicate what should be in the field. These are the login-text
login_text_style = {
    **base_text_style,
    'color': COLOR_WHITE,
    'width': '120px',
    'marginRight': '40px',
    'fontSize': '20px'
}

# The button you have to click to log-in
login_button_style = {
    "color": COLOR_BLACK,
    "width": '100px',
    "height": '30px',
    'fontSize': '15px',
    'marginLeft': '50px'
}

# In the log-in page of the admin and participant module there is an option to switch to the other (admin or participant) module
switch_button_style = {
    **base_text_style,
    "color": COLOR_BLACK,
    'fontSize': '15px',
    'marginLeft': '50px',
    'position': 'absolute',
    'bottom': '0',
    'right': '0',
    'marginBottom': '20px',
    'marginRight': '20px',
    'width': '150px',
    'height': '40px'
}

# The picture of GRC in the bottom of the page
grc_bottom_img = {
            'position': 'absolute',
            'bottom': '0',
            'left': '50%',
            'transform': 'translateX(-50%)',
            'width': '20%',
}

# Furthest background of admin module
background_admin_style = {
    'height': '100vh',
    'width': '100vw',
    'backgroundColor': COLOR_LIGHTBLUE,
    'display': 'flex',
    'alignItems': 'center',
    'justifyContent': 'center',
    'position': 'relative',
}

# Rectangle in admin module
rectangle_admin_style = {
    'backgroundColor': COLOR_DARKBLUE,
    'width': '80%',
    'height': '70%',
    'borderRadius': '15px',

}

# Tabs in admin module
tab_admin_style = {
    **base_text_style,
    "backgroundColor": COLOR_EXPRES,
    "color": COLOR_BLACK,
    "width": '150px',
    "height": '40px',
    'fontSize': '18px',
    'font-weight': 'bold',
    'marginLeft': '20px',
    'marginTop': '0px',
    'border': 'none',
    'borderRadius': '5px',
    'cursor': 'pointer'
}

# Furthest background of participant module
background_part_style = {
    'height': '100vh',
    'width': '100vw',
    'backgroundColor': COLOR_DARKGREEN,
    'display': 'flex',
    'alignItems': 'center',
    'justifyContent': 'center',
    'position': 'relative',
    'flexDirection': 'column',
    'padding': '20px',
    'overflow': 'hidden'  # Disable scrolling
}

# Rectangle in particpant module
rectangle_part_style = {
    'backgroundColor': COLOR_WHITE,
    'width': '80%',
    'height': '70%',
    'boxShadow': '20px 20px 8px rgba(0 , 0, 0, 0.2)',
    'padding': '40px',  # More padding to create space inside the panel
    'borderRadius': '12px',  # Rounded corners for the panel
    'maxWidth': '600px',  # Set a max-width for a more controlled layout
    'margin': 'auto',  # Center the panel on the page
    'border': '1px solid black',


}

# Next Button Participants
next_part_style = {
    **base_text_style,
    "color": COLOR_BLACK,
    'fontSize': '15px',
    'position': 'absolute',
    'bottom': '8%',
    'right': '10%',
    'width': '150px',
    'height': '40px',
    'backgroundColor': COLOR_EXPRES,
    'borderRadius': '10px'}

# Next Button questionnaire Participants
question_next_button_style = {
    ** base_text_style,
    "color": COLOR_BLACK,
    'fontSize': '15px',
    'position': 'absolute',
    'margin-top':"20px",
    'bottom': '50%',
    'right': '40%',
    'width': '150px',
    'height': '40px',
    'backgroundColor': COLOR_EXPRES,
    'borderRadius': '10px'}

# White line below question
question_line_style={
    'borderTop': '2px solid white',
    'width': '100%',
    'marginBottom': '20px',
    'opacity': '0.8',
}
