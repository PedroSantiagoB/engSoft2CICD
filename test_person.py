import unittest
from person import Person

class TestPerson(unittest.TestCase):
    def test_get_name(self):
        p = Person("Pedro", 20, 123456, 10000.0)
        self.assertEqual(p.get_name(), "Pedro")

    def test_get_age(self):
        p = Person("Pedro", 20, 123456, 10000.0)
        self.assertEqual(p.get_age(), 20)

    def test_get_net_worth(self):
        p = Person("Pedro", 20, 123456, 10000.0)
        self.assertEqual(p.get_net_worth(), 10000.0)

    def test_set_net_worth(self):
        p = Person("Pedro", 20, 123456, 10000.0)
        p.set_net_worth(20000.0)
        self.assertEqual(p.get_net_worth(), 20000.0)

if __name__ == "__main__":
    unittest.main()
