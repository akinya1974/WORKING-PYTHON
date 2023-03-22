

import json

file_name = 'data.json'
file_name_new = 'data_new.json'

def read_json(file_name: str):
    with open(file_name) as file_name:
        data = json.load(file_name)
        print(data)

read_json(file_name)

def write_json(in_file_name, out_file_name):
    data = read_json(in_file_name)
    with open(out_file_name, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

write_json(file_name, file_name)
