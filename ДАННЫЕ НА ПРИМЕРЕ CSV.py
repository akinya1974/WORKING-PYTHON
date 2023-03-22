
import csv

file_name = 'only_last.csv'
file_name_new = '2022-03-03_new.csv'

def read_csv(file_name):
    with open(file_name) as csv_file:
        reader = csv.reader(csv_file)
        print(list(reader))

read_csv(file_name)



import csv

file_name = 'only_last.csv'
file_name_new = '2022-03-03_new.csv'


def read_csv(file_name):
    with open(file_name) as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)

    header = data.pop(0)
    return header, data


def write_csv(in_file_name, out_file_name):
    header, data = read_csv(in_file_name)
    with open(out_file_name, 'w') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(header)
        writer.writerows(data)


write_csv(file_name, file_name_new)


import csv

file_name = 'only_last.csv'
file_name_new = '2022-03-03_new.csv'


def read_csv(file_name):
    with open(file_name) as csv_file:
        reader = csv.DictReader(csv_file)
        for item in reader:
            print(item)

read_csv(file_name)

import csv

file_name = 'only_last.csv'
file_name_new = '2022-03-03_new.csv'

def read_csv(file_name):
    with open(file_name) as csv_file:
        reader = csv.reader(csv_file)
        print(list(reader))

read_csv(file_name)



import csv

file_name = 'only_last.csv'
file_name_new = '2022-03-03_new.csv'


def read_csv(file_name):
    with open(file_name) as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)

    header = data.pop(0)
    return header, data


def write_csv(in_file_name, out_file_name):
    header, data = read_csv(in_file_name)
    with open(out_file_name, 'w') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(header)
        writer.writerows(data)


write_csv(file_name, file_name_new)


import csv

file_name = 'only_last.csv'
file_name_new = '2022-03-03_new.csv'


def read_csv(file_name):
    with open(file_name) as csv_file:
        reader = csv.DictReader(csv_file)
        for item in reader:
            print(item)

read_csv(file_name)
