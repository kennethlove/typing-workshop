import os

import yaml

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self.__dict__)

    def toJSON(self):
        return json.dumps(self.__dict__)


class AddressBook:
    def __init__(self, filename):
        self.file = os.path.join(CURRENT_DIR, filename)
        self.records = self._load_all()

    def _load_all(self):
        try:
            with open(self.file, 'r') as file:
                records = yaml.load(file.read())
        except FileNotFoundError:
            return []
        else:
            return [Person(person['name'], **person) for person in records]

    def _save(self):
        with open(self.file, 'a') as file:
            file.write(yaml.dump(self.records))

    def __iter__(self):
        yield from self.records

    def __contains__(self, person):
        return len(list(self.search(person)))

    def clear(self):
        os.unlink(self.file)

    def search(self, name):
        return filter(lambda p: p.name == name, self)

    def add(self, name, email):
        if name in self:
            raise KeyError("{} already exists".format(name))
        else:
            self.records.append(Person(name, email))
        self._save()

