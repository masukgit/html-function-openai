students = ['Ananta', 'Akash', 'Batash', 'Nill', 'Bill', 'Haor']
temp = ['<ul>']
for student in students:
    temp.append(f'<li>{student}</li>')
temp.append('</ul>')
my_string = ' '.join(temp)
print(my_string)

def list_html(data_list, list_type='ul'):
    temp = [f'<{list_type}>']
    for data in data_list:
        temp.append(f'<li>{data}</li>')
    temp.append(f'</{list_type}>')
    my_string = ' '.join(temp)
    return my_string
d = list_html(students,'ol')
print(d)

