def html_tags(tag, text):
    """
    This will generate html tag
    """
    elements =['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ol', 'ul', 'li']
    if tag not in elements:
        print('Error! This not html tag.')
        return '---'
    generated_tag = f'<{tag}>{text}</{tag}>'
    return generated_tag



def html_tags1(tag1, text1):
    """
    This will generate html tag
    """
    elements1 =['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ol', 'ul', 'li']
    if tag1 in elements1:
        generated_tag1 = f'<{tag1}>{text1}</{tag1}>'
        return generated_tag1
    else:
        print('Nope, This is not html tag format')
        return '---'
