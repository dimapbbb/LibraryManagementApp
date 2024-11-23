import json
from os.path import abspath


class JsonWorkerMixin:
    path = abspath('./data/books_warehouse.json')

    def read_file(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            return json.loads(file.read())

    def write_file(self, data):
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)