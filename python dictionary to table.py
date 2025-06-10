my_dict = {'Name': 'Alice', 'Age': '30', 'City': 'New York',
           'Home Town': 'Wasington DC', 'Neighborhood': 'Vienna'}

def dic_html_table(my_dict):
    """
    This will convert python list to html table
    :param: A python dictionary
    :return: Html string
    """
    table_list = ['<figure class="wp-block-table"><table class="has-fixed-layout"><tbody><tr>']
    for key in my_dict.keys():
        table_list.append(f'<td>{key}</td>')
    table_list.append('</tr><tr>')
    for value in my_dict.values():
        table_list.append(f'<td>{value}</td>')
    table_list.append('</tr></tbody></table></figure>')
    my_str = ''.join(table_list)
    return my_str

print(dic_html_table(my_dict))