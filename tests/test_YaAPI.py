import unittest
import YaAPI


class TestFunctions(unittest.TestCase):
    def test_create_folder(self):
        result = YaAPI.new_folder('any_name')
        self.assertEqual(201, result)

    def test_name_conflict(self):
        with self.assertRaises(ValueError) as ex:
            YaAPI.new_folder('any_name')
        self.assertEqual('Папка с таким названием уже существует', ex.exception.args[0])
