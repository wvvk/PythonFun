import unittest
from nato_phonetics import NATOPhonetics


class TestNATOPhonetics(unittest.TestCase):
    def setUp(self):
        self.filename = "nato_phonetic_alphabet.csv"
        self.nato_phonetics = NATOPhonetics(self.filename)

    def test_name_to_code(self):
        name = "John"
        expected_code_list = ['Juliet', 'Oscar', 'Hotel', 'November']
        actual_code_list = self.nato_phonetics.name_to_code(name)
        self.assertEqual(actual_code_list, expected_code_list)

        with self.assertRaises(ValueError):
            self.nato_phonetics.name_to_code('J0hn')

        with self.assertRaises(ValueError):
            self.nato_phonetics.name_to_code('')


if __name__ == '__main__':
    unittest.main()
