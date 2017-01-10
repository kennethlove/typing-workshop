import unittest

import address_book


class AddressBookTests(unittest.TestCase):
    def setUp(self):
        self.address_book = address_book.AddressBook("test.yml")

    def tearDown(self):
        # self.address_book.clear()
        pass

    def test_add_person(self):
        self.address_book.add("Kenneth Love", "kenneth@teamtreehouse.com")
        self.assertIn("Kenneth Love", self.address_book)