
# Colors
COLOR_LIGHTBLUE = '#c9daf0'
COLOR_DARKGRAY = '#222423'
COLOR_DARKGREEN = '#034B4D'
COLOR_EXPRES = '#ef8338'
COLOR_BLACK = '#000000'
COLOR_WHITE = '#FFFFFF'

# Input settings
INPUT_WIDTH_LOGIN = '200px'
INPUT_HEIGHT_LOGIN = '30px'


# Styles

# full_style defines the space that a whole page should take up.
full_style = {
    'height': '100vh',
    'width': '100vw'
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
    'paddingLeft': '8%',
    'paddingTop': '8%',
    'fontSize': '30px',
    'fontWeight': 'bold'
}

# Next to the login input field are the text that indicate what should be in the field. These are the login-text
login_text_style = {
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
            'width': '25%',
}