import sys

if len(sys.argv) != 2:
    print('Invalid syntax. Correct syntax: python set_current_appveyor.py [py_stringmatching/py_stringsimjoin/magellan]')
    exit(-1)

option = sys.argv[1].lower()

if option not in ['py_stringmatching', 'py_stringsimjoin', 'magellan']:
    print('Invalid syntax. Correct syntax: python set_current_appveyor.py [py_stringmatching/py_stringsimjoin/magellan]')
    exit(-1)

appveyor_file_name = 'appveyor_' + option + '.yml'
with open(appveyor_file_name, 'r') as file_handle:
    app_data = file_handle.read()

with open('appveyor.yml', 'w') as file_handle:
    file_handle.write(app_data)    
