import requests


def multiplication_int(a, b):
    return a * b
def multiplication_string(line, n):
    return line * n
def get_name_hero_by_id(_id):
    r = requests.get(f'https://superheroapi.com/api/2619421814940190/{_id}')
    result = r.json()
    if 'name' in result:
        name = result['name']
        return name
print(get_name_hero_by_id(70))
# name = input('Введите имя ')
#
# assert name, 'пустое имя'
#
# print('End file')