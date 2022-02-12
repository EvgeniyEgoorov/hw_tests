import unittest
from unittest.mock import patch
from main import show_document_info

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]


class TestFunctions(unittest.TestCase):
    def test_show_document_info(self):
        expected_result = [
            'passport "2207 876234" "Василий Гупкин"',
            'invoice "11-2" "Геннадий Покемонов"',
            'insurance "10006" "Аристарх Павлов"'
        ]
        result = [show_document_info(i) for i in documents]
        self.assertListEqual(result, expected_result)

    # @patch('__builtin__.input')
    # def test_add_new_doc(self):
    #     pass
    #
    # @patch('__builtin__.input')
    # def test_delete_doc(self):
    #     pass


