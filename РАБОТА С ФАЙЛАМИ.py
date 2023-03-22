
import os

BASE_PATCH = os.getcwd()
log_dir = 'logs'
file_name = 'logs.txt'

full_patch = os.path.join(BASE_PATCH, log_dir, file_name)
print(f'====> {full_patch}')


file_name = 'data.txt'


def file_worker(file_name: str):
    with open(file_name) as file:
        data = file.read()
    return data


result = (file_worker(file_name))
print(result)

print('---------------------------')

g = open('data.txt')
f = g.read()
print(f)

print('---------------------------')


def file_worker(file_name: str):
    with open(file_name) as file:
        print(file.readline())
        print(file.readline().strip())
        print(file.readline())
result = (file_worker(file_name))

print('---------------------------')


def file_worker(file_name: str):
    with open(file_name) as file:
        data = file.readlines()
        print(data[2])
result = (file_worker(file_name))

print('---------------------------')


def file_worker(file_name: str):
    with open(file_name) as file:
        for line in file:
            print(line.strip())
result = (file_worker(file_name))

# print('---------------------------')
#
#
# with open('data.txt', 'a') as f:
#     f.write('Первая строка! \n')
# with open('data.txt', 'a') as f:
#     f.write('Вторая строка! \n')


