import os

import yaml

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f'{self.name}: {self.email}'


class AddressBook(set):
    def __init__(self, iterable=None, filename=None):
        self.file = os.path.join(CURRENT_DIR, filename or 'address_book.yml')
        self._load_all()
        super().__init__(iterable or [])

    def _load_all(self):
        try:
            with open(self.file, 'r+') as file:
                records = yaml.load(file.read())
        except FileNotFoundError:
            pass
        else:
            for record in records:
                self.add(record)

    def _save(self):
        with open(self.file, 'w+') as file:
            file.write(yaml.dump(self))

    def clear(self):
        try:
            os.unlink(self.file)
        except FileNotFoundError:
            pass

    def search(self, name):
        return filter(lambda p: p.name == name, self)

    def add_record(self, person):
        self.add(person)
        self._save()

    def remove_record(self, person):
        self.remove(person)
        self._save()

