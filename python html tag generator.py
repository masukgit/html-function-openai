def heading_one(text):
    """
    This will generate heading one
    """
    return f'<h1>{text}</h1>'

def heading_two(text):
    """
    This will generate heading two
    """
    return f'<h2>{text}</h2>'

def heading_three(text):
    """
    This will generate heading three
    """
    return f'<h3>{text}</h3>'

def heading_four(text):
    """
    This will generate heading four
    """
    return f'<h4>{text}</h4>'

def heading_five(text):
    """
    This will generate heading five
    """
    return f'<h5>{text}</h5>'

def heading_six(text):
    """
    This will generate heading six
    """
    return f'<h6>{text}</h6>'

def html_tags_generator(tag, text):
    return f'<{tag}>{text}</{tag}>'

heading = html_tags_generator('h3', 'I Love Python')

print(heading)
