import unittest

import address_book


class AddressBookTests(unittest.TestCase):
    def setUp(self):
        self.address_book = address_book.AddressBook(filename="test.yml")
        self.p1 = address_book.Person("One", "one@example.com")
        self.p2 = address_book.Person("Two", "two@example.com")

    def tearDown(self):
        self.address_book.clear()

    def test_add_person(self):
        self.address_book.add_record(self.p1)
        self.assertIn(self.p1, self.address_book)

    def test_add_two_people(self):
        self.address_book.add_record(self.p1)
        self.address_book.add_record(self.p2)
        self.assertEqual(len(self.address_book), 2)

    def test_add_repeat(self):
        self.address_book.add_record(self.p1)
        self.address_book.add_record(self.p1)
        self.assertEqual(len(self.address_book), 1)

    def test_remove(self):
        self.address_book.add_record(self.p1)
        self.address_book.remove_record(self.p1)
        self.assertNotIn(self.p1, self.address_book)

    def test_shortcut(self):
        self.address_book.add_record("Kenneth")