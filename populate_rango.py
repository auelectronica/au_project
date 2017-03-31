import os
import string
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "au_project.settings")

import django
django.setup()

from au_search.models import Part

FILE_SUFIXES = string.digits + string.ascii_lowercase
DB_DIR = './db_files/'
FILE_PREFIX = 'db_'

def read_file(filename):
    file_content = ''
    with open(filename, 'r') as f:
        file_content = f.read()
    return file_content

def read_db_file(sufix):
    return read_file(DB_DIR + FILE_PREFIX  + sufix + '.json')

def get_parsed_db_file(sufix):
    db_string = read_db_file(sufix)
    db_object = json.loads(db_string) 
    return db_object

def populate():
    for  sufix in FILE_SUFIXES:
        list_of_parts = get_parsed_db_file(sufix)
        for part in list_of_parts:
            print_part(part)

def save_part_to_django_db(part):

def print_part(part):
    print('part no: {:<25} price: {:<10} stock:{:<6}'.format(part['id'],part['price']['1'],part['stock']))

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
